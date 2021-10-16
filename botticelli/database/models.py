import enum
import typing

from sqlalchemy import Column, String, Integer, Boolean, Enum, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from sqlalchemy_mixins import TimestampsMixin

from . import Base

from bcrypt import checkpw as bcrypt_check


class JSONSerializableMixin:
    #: Map hybrid property names to their underlying columns
    remappings = {}

    @classmethod
    def from_dict(cls, init_dict):
        remapped = {cls.remappings.get(k, k): v for (k, v) in init_dict.items()}
        return cls(**remapped)

    def to_dict(self):
        inverted_remappings = {v: k for (k, v) in self.remappings.items()}
        return {
            inverted_remappings.get(c.name, c.name): getattr(
                self, inverted_remappings.get(c.name, c.name)
            )
            for c in self.__table__.columns
        }


class Gender(enum.Enum):
    male = "male"
    female = "female"
    analog = "analog"


tag_table = Table(
    "entity_tags",
    Base.metadata,
    Column("entity_id", ForeignKey("entities.id")),
    Column("tag_id", ForeignKey("tags.id")),
)


class Fact(JSONSerializableMixin, TimestampsMixin, Base):
    __tablename__ = "facts"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    entity = relationship("Entity", back_populates="facts")
    entity_id = Column(Integer, ForeignKey("entities.id"))


class Tag(JSONSerializableMixin, TimestampsMixin, Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    tagged = relationship("Entity", secondary=tag_table, back_populates="tags")

    def to_dict(self, include_tagged=False):
        base = super().to_dict()
        if include_tagged:
            base["tagged"] = list(e.id for e in self.tagged)
        return base


class Entity(JSONSerializableMixin, TimestampsMixin, Base):
    __tablename__ = "entities"

    remappings = {"alphabetized_as": "_alphabetized_as"}

    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    nickname = Column(String)
    surname = Column(String)
    _alphabetized_as = Column(String)
    is_real = Column(Boolean)
    is_living = Column(Boolean)
    birth_year = Column(String)
    gender = Column(Enum(Gender))
    score = Column(Integer, default=0)
    description = Column(String)
    wikipedia_url = Column(String)
    image_url = Column(String)
    tags = relationship(Tag, secondary=tag_table, back_populates="tagged")
    facts = relationship(Fact, back_populates="entity")

    @hybrid_property
    def alphabetized_as(self):
        for maybe in ("_alphabetized_as", "nickname", "surname", "given_name"):
            maybe = getattr(self, maybe)
            if maybe is not None:
                return maybe[0]

    @alphabetized_as.setter
    def alphabetized_as(self, new_val: str):
        self._alphabetized_as = new_val[0]

    def to_dict(self):
        base = super().to_dict()
        base["facts"] = list(f.to_dict() for f in self.facts)
        base["tags"] = list(t.to_dict() for t in self.tags)
        return base


class User(JSONSerializableMixin, TimestampsMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def check_password(self, password: str):
        return bcrypt_check(password.encode("utf-8"), self.password.encode("utf-8"))

    def to_dict(self):
        base = super().to_dict()
        base.pop("password")
        return base

from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

# from open_alchemy import init_yaml

URL = "sqlite:///botticelli.db"

engine = create_engine(
    URL, echo=True, future=True, connect_args={"check_same_thread": False}
)
Base = declarative_base()
Session = scoped_session(sessionmaker(bind=engine))


def _retarget_engine(new_url):
    global engine
    global Session
    engine = create_engine(
        new_url, echo=True, future=True, connect_args={"check_same_thread": False}
    )
    Session = scoped_session(sessionmaker(bind=engine))
    Base.metadata.create_all(engine)


# _parent_dir = Path(__file__).parent.parent
# _spec_file = _parent_dir.joinpath("openapi", "openapi.yaml")
# _models_file = _parent_dir.joinpath("database", "models_autogenerated.py")

# init_yaml(_spec_file, base=Base, models_filename=_models_file)

from botticelli.database.models import *

Base.metadata.create_all(engine)

from botticelli.database.default_items import *


def add_item(cls: Base, init_params, *, session=Session()) -> int:
    init_params.pop("id", None)
    created = cls.from_dict(init_params)
    session.add(created)
    session.flush()
    cached_id = created.id
    session.commit()
    return cached_id


def get_item(cls, item_id: int, *, session=Session()):
    maybe_item = session.query(cls).get(item_id)
    if maybe_item is not None:
        return maybe_item.to_dict()
    return f"No such {cls.__name__}: {item_id}", 404


def delete_item(cls, item_id: int, *, session=Session()):
    maybe_item = session.query(cls).get(item_id)
    if maybe_item is not None:
        session.delete(maybe_item)
        session.commit()
        return [item_id]
    return f"No such {cls.__name__}: {item_id}", 404


def update_item(cls, item_id: int, new_data, *, session=Session()):
    maybe_item = session.query(cls).get(item_id)
    if maybe_item is not None:
        for (k, v) in new_data.items():
            if isinstance(v, list):
                getattr(maybe_item, k).clear()
                for item in v:
                    getattr(maybe_item, k).append(item)
            else:
                setattr(maybe_item, k, v)
        session.commit()
        return [item_id]
    return f"No such {cls.__name__}: {item_id}", 404

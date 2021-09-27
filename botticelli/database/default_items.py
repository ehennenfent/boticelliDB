from . import Session, User, Tag

DEFAULT_TAGS = {
    "Actor/Actress",
    "Animal",
    "Athlete",
    "Author",
    "Deity",
    "Musician",
    "Politician",
    "Religious Figure",
    "Scientist",
}

DEFAULT_USERS = (
    {
        "username": "ehennenfent",
        "password_hash": "$2b$12$O7VHSaYpaV8RVE2KB3dZ5OKepzFTVMtcVhLrRveDNNHzQkMydeIRG",
    },
    {
        "username": "wikibot",
        "password_hash": "$2b$12$8FKYPPj1npjAhv3rw7PLHuIjLXgvaTLV2.fY26pqPgxqji0VOHZMy",
    },
)


def create_default_tags():
    session = Session()
    for tag in DEFAULT_TAGS:
        if session.query(Tag).filter(Tag.name == tag).count() == 0:
            session.add(Tag(name=tag))
    session.commit()


def create_default_users():
    session = Session()
    for user in DEFAULT_USERS:
        uname = user["username"]
        if session.query(User).filter(User.username == uname).count() == 0:
            session.add(User(username=uname, password=user["password_hash"]))

    session.commit()


create_default_tags()
create_default_users()

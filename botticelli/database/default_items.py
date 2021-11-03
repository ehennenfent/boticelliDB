from . import Session, User, Tag

DEFAULT_TAGS = {
    # Qualifiers for non-real entities
    "Human",
    "Alien",
    "Deity",
    "Cryptid",

    # Profession
    "Actor/Actress",
    "Artist",
    "Athlete",
    "Author",
    "Musician",
    "Politician",
    "Religious Figure",
    "Scientist",
    "Business Person",
    "Inventor",
    "Physician",
    "Newscaster",
    "Chef",
    "Military Figure",
    "Social Media Personality",

    # Continent of Origin
    "North American",
    "South American",
    "African",
    "European",
    "Asian",
    "Australian",
    "Antarctic",  # you never know

    # Modern Country of Origin
    "American",
    "Canadian",
    "Mexican",
    "Chinese",
    "Japanese",
    "Indian",
    "Korean",
    "Filipino",
    "Indonesian",
    "Pakistani",
    "Russian",
    "French",
    "Spanish",
    "Portugese",
    "Italian",
    "English",
    "Irish",
    "Scottish",
    "German",
    "Brazilian",
    "South African",

    # Ancient Civilizations
    "Egyptian",
    "Greek",
    "Roman",
    "Persian",
    "Babylonian",
    "Byzantine",
    "Mayan",
    "Aztec",

    # Race
    "European Descent",
    "African Descent",
    "East Asian Descent",
    "South Asian Descent",
    "Middle-Eastern Descent",
    "Indigenous American",
    "Indigenous Australian",
    "Pacific Islander",

    # Gender & Sexuality
    "Heterosexual",
    "Homosexual",
    "Bisexual",
    "Transgender",

    # Awards
    "Nobel Prize",
    "Turing Award",
    "Fields Medal",
    "Medal of Honor",
    "Medal of Freedom",

    # Types of Animals
    "Dog",
    "Cat",
    "Horse",
    "Rabbit",

    # Religions
    "Christian",
    "Jewish",
    "Muslim",
    "Hindu",
    "Buddhist",

    # Popular works of fiction
    "Lord of the Rings",
    "The Chronicles of Narnia",
    "Harry Potter",
    "Game of Thrones",
    "The Witcher",
    "Star Wars",
    "Star Trek",
    "The Expanse",
    "Marvel Cinematic Universe",

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

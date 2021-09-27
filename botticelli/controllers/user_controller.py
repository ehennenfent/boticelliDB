import connexion
import six

from random import getrandbits

from botticelli import util
from botticelli.database import Session, User
from botticelli.database.sessions import active_sessions


def get_user_by_name(username):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param username: The name that needs to be fetched. Use user1 for testing.
    :type username: str

    :rtype: User
    """
    maybe_item = Session().query(User).filter(User.username == username).first()
    if maybe_item is not None:
        return maybe_item.to_dict()
    return f"No such user: {username}", 404


def login_user():  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param user: User Data for log in
    :type user: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        as_dict = connexion.request.get_json()
        username = as_dict.pop("username", None)
        password = as_dict.pop("password", None)
        user = Session().query(User).filter(User.username == username).first()

        if user is None or username is None or password is None:
            return "Bad request", 405

        if not user.check_password(password):
            return "Incorrect Password", 401

        new_session_key = f"{getrandbits(128):x}"
        active_sessions[new_session_key] = {"associated_username": username}

        return new_session_key


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    print("Logging out", connexion.context["token_info"]["associated_username"])
    del active_sessions[connexion.request.headers["api_key"]]

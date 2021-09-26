import connexion
import six

from botticelli import util


def get_user_by_name(username):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param username: The name that needs to be fetched. Use user1 for testing.
    :type username: str

    :rtype: User
    """
    return "do some magic!"


def login_user(user):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param user: User Data for log in
    :type user: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return "do some magic!"


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    return "do some magic!"

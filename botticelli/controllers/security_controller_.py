from typing import List
from botticelli.database.sessions import active_sessions

defined_oauth_tokens = {
    # "FakeOauthToken": {"scopes": ["write:entries"], "uid": "user_id"}
}


def info_from_apiKey(apiKey, required_scopes):
    """
    Check and retrieve authentication information from apiKey.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.

    :param apiKey API key provided by Authorization header
    :type apiKey: str
    :param required_scopes Always None. Used for other authentication method
    :type required_scopes: None
    :return: Information attached to provided apiKey or None if apiKey is invalid or does not allow access to called API
    :rtype: dict | None
    """
    return active_sessions.get(apiKey, None)


def info_from_boticelli_auth(token):
    """
    Validate and decode token.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.
    'scope' or 'scopes' will be passed to scope validation function.

    :param token Token provided by Authorization header
    :type token: str
    :return: Decoded token information or None if token is invalid
    :rtype: dict | None
    """
    return defined_oauth_tokens.get(token, None)


def validate_scope_boticelli_auth(required_scopes, token_scopes):
    """
    Validate required scopes are included in token scope

    :param required_scopes Required scope to access called API
    :type required_scopes: List[str]
    :param token_scopes Scope present in token
    :type token_scopes: List[str]
    :return: True if access to called API is allowed
    :rtype: bool
    """
    return set(required_scopes).issubset(set(token_scopes))

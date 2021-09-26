import connexion
import six

from botticelli import util
from botticelli.database import Fact, Session, add_item, get_item, delete_item


def add_fact(entity_id, body):  # noqa: E501
    """Add a new fact to the database

     # noqa: E501

    :param entity_id: ID of entity to get facts for
    :type entity_id: int
    :param body: Fact object that needs to be added to the database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        return [add_item(Fact, connexion.request.get_json())]


def delete_fact(fact_id, entity_id):  # noqa: E501
    """Deletes a fact

     # noqa: E501

    :param fact_id: Fact id to delete
    :type fact_id: int
    :param entity_id: ID of entity this fact belongs to
    :type entity_id: int

    :rtype: None
    """
    return delete_item(Fact, fact_id)


def get_entity_facts(entity_id):  # noqa: E501
    """Returns all entities from the system

     # noqa: E501

    :param entity_id: ID of entity to get facts for
    :type entity_id: int

    :rtype: List[Entity]
    """
    return "do some magic!"


def get_fact_by_id(fact_id, entity_id):  # noqa: E501
    """Find fact by ID

    Returns a single fact # noqa: E501

    :param fact_id: ID of fact to return
    :type fact_id: int
    :param entity_id: ID of entity this fact belongs to
    :type entity_id: int

    :rtype: Fact
    """
    return get_item(Fact, fact_id)


def update_fact(entity_id, body):  # noqa: E501
    """Update an existing fact

     # noqa: E501

    :param entity_id: ID of entity to get facts for
    :type entity_id: int
    :param body: Fact object that needs to be added to the database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Fact.from_dict(connexion.request.get_json())  # noqa: E501
    return "do some magic!"


def update_fact_with_form(fact_id, entity_id, name=None, status=None):  # noqa: E501
    """Updates a fact in the database with form data

     # noqa: E501

    :param fact_id: ID of fact that needs to be updated
    :type fact_id: int
    :param entity_id: ID of entity this fact belongs to
    :type entity_id: int
    :param name: Updated name of the fact
    :type name: str
    :param status: Updated status of the fact
    :type status: str

    :rtype: None
    """
    return "do some magic!"

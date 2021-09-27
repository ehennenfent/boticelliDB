import connexion
import six

from botticelli import util
from botticelli.database import (
    Fact,
    Entity,
    Session,
    add_item,
    get_item,
    delete_item,
    update_item,
)


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
        session = Session()
        maybe_entity = session.query(Entity).get(entity_id)
        if maybe_entity is not None:
            args = connexion.request.get_json()
            args["entity"] = maybe_entity
            return [add_item(Fact, args, session=session)]
        return f"No such Entity: {entity_id}", 404


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
    maybe_entity = Session().query(Entity).get(entity_id)
    if maybe_entity is not None:
        return list(f.to_dict() for f in maybe_entity.facts)
    return f"No such Entity: {entity_id}", 404


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


def update_fact(fact_id, entity_id):  # noqa: E501
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
    if connexion.request.is_json:
        as_dict = connexion.request.get_json()
        _entity_id = as_dict.pop("entity_id", entity_id)
        _fact_id = as_dict.pop("id", fact_id)

        if _fact_id != fact_id:
            return "ID is immutable", 400
        if _entity_id != entity_id:
            return "Entity ID is immutable", 400

        return update_item(Fact, fact_id, as_dict)

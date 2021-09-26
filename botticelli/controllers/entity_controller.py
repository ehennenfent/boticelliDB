import connexion
import six

from botticelli import util
from botticelli.database import (
    Entity,
    Session,
    add_item,
    get_item,
    delete_item,
    update_item,
)


def add_entity(body):  # noqa: E501
    """Add a new entity to the database

     # noqa: E501

    :param body: Entity object that needs to be added to the database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        return [add_item(Entity, connexion.request.get_json())]


def delete_entity(entity_id):  # noqa: E501
    """Deletes a entity

     # noqa: E501

    :param entity_id: Entity id to delete
    :type entity_id: int

    :rtype: None
    """
    return delete_item(Entity, entity_id)


def get_all_entities(
    offset=None, limit=None, updated_since=None, created_since=None
):  # noqa: E501
    """Returns all entities from the system

     # noqa: E501

    :param offset: The number of items to skip before starting to collect the result set
    :type offset: int
    :param limit: The numbers of items to return
    :type limit: int
    :param updated_since: Only return entities with changes past this date
    :type updated_since: str
    :param created_since: Only return entities created after this date
    :type created_since: str

    :rtype: List[Entity]
    """
    updated_since = util.deserialize_datetime(updated_since)
    created_since = util.deserialize_datetime(created_since)
    query = Session().query(Entity).order_by(Entity.score.desc())
    if created_since is not None:
        query = query.filter(Entity.created_at > created_since)
    if updated_since is not None:
        query = query.filter(Entity.updated_at > updated_since)
    if offset is not None:
        query = query.offset(offset)
    if limit is not None:
        query = query.limit(limit)
    return list(e.to_dict() for e in query.all())


def get_entity_by_id(entity_id):  # noqa: E501
    """Find entity by ID

    Returns a single entity # noqa: E501

    :param entity_id: ID of entity to return
    :type entity_id: int

    :rtype: Entity
    """
    return get_item(Entity, entity_id)


def update_entity(body):  # noqa: E501
    """Update an existing entity

     # noqa: E501

    :param body: Entity object that needs to be added to the database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        as_dict = connexion.request.get_json()
        entity_id = as_dict.pop("id")
        return update_item(Entity, entity_id, as_dict)


def update_entity_with_form(entity_id, body):  # noqa: E501
    """Update this entity

     # noqa: E501

    :param entity_id: ID of this entity
    :type entity_id: int
    :param body: Entity object that needs to be added to the database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        as_dict = connexion.request.get_json()
        _entity_id = as_dict.pop("id", entity_id)
        if _entity_id != entity_id:
            return "ID is immutable", 400
        return update_item(Entity, entity_id, as_dict)

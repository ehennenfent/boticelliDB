import connexion
import six

from botticelli import util
from botticelli.database import (
    Entity,
    Tag,
    Session,
    add_item,
    get_item,
    delete_item,
    update_item,
)


def add_tag(body):  # noqa: E501
    """Add a new tag to the database

     # noqa: E501

    :param body: Tag object that needs to be added to the database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        return [add_item(Tag, connexion.request.get_json())]


def delete_tag(tag_id):  # noqa: E501
    """Deletes a tag

     # noqa: E501

    :param tag_id: Tag id to delete
    :type tag_id: int
    :param api_key:
    :type api_key: str

    :rtype: None
    """
    return delete_item(Tag, tag_id)


def get_all_tags():  # noqa: E501
    """Returns all tags

     # noqa: E501


    :rtype: List[Tag]
    """
    return list(t.to_dict() for t in Session().query(Tag).all())


def get_tag_by_id(tag_id):  # noqa: E501
    """Find tag by ID

    Returns a single tag # noqa: E501

    :param tag_id: ID of tag to return
    :type tag_id: int

    :rtype: Tag
    """
    session = Session()
    maybe_item = session.query(Tag).get(tag_id)
    if maybe_item is not None:
        return maybe_item.to_dict(include_tagged=True)
    return f"No such Tag: {tag_id}", 404


def tag_entity(entity_id, tag_id):  # noqa: E501
    """Assign a tag to an entity

     # noqa: E501

    :param entity_id: ID of entity to add tag to
    :type entity_id: int
    :param tag_id: ID of tag to add to this entity
    :type tag_id: int

    :rtype: None
    """
    session = Session()
    tag = session.query(Tag).get(tag_id)
    if tag is None:
        return "No such Tag", 404
    entity = session.query(Entity).get(entity_id)
    if entity is None:
        return "No such Entity", 404
    entity.tags.append(tag)
    session.commit()
    return tag_id


def untag_entity(entity_id, tag_id):  # noqa: E501
    """Remove a tag from an entity

     # noqa: E501

    :param entity_id: ID of entity to remove tag from
    :type entity_id: int
    :param tag_id: ID of tag to remove from this entity
    :type tag_id: int
    :param api_key:
    :type api_key: str

    :rtype: None
    """
    session = Session()
    tag = session.query(Tag).get(tag_id)
    if tag is None:
        return "No such Tag", 404
    entity = session.query(Entity).get(entity_id)
    if entity is None:
        return "No such Entity", 404
    try:
        entity.tags.remove(tag)
    except ValueError:
        return "Entity does not have this tag", 400
    session.commit()
    return tag_id


def update_tag(tag_id):  # noqa: E501
    """Updates a tag in the database with form data

     # noqa: E501

    :param tag_id: ID of tag that needs to be updated
    :type tag_id: int
    :param name: Updated name of the tag
    :type name: str
    :param status: Updated status of the tag
    :type status: str

    :rtype: None
    """
    if connexion.request.is_json:
        as_dict = connexion.request.get_json()
        _tag_id = as_dict.pop("id", tag_id)
        if _tag_id != tag_id:
            return "ID is immutable", 400
        return update_item(Tag, tag_id, as_dict)

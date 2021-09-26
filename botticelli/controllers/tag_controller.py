import connexion
import six

from botticelli import util
from botticelli.database import Tag, Session, add_item, get_item, delete_item


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
    return get_item(Tag, tag_id)


def tag_entity(entity_id, tag_id):  # noqa: E501
    """Assign a tag to an entity

     # noqa: E501

    :param entity_id: ID of entity to add tag to
    :type entity_id: int
    :param tag_id: ID of tag to add to this entity
    :type tag_id: int

    :rtype: None
    """
    return "do some magic!"


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
    return "do some magic!"


def update_tag(body):  # noqa: E501
    """Update an existing tag

     # noqa: E501

    :param body: Tag object that needs to be added to the database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Tag.from_dict(connexion.request.get_json())  # noqa: E501
    return "do some magic!"


def update_tag_with_form(tag_id, name=None, status=None):  # noqa: E501
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
    return "do some magic!"

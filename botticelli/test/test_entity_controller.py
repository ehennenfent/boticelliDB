# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from botticelli.test import BaseTestCase


class TestEntityController(BaseTestCase):
    """EntityController integration test stubs"""

    def test_add_entity(self):
        """Test case for add_entity

        Add a new entity to the database
        """
        body = {
            "is_real": true,
            "alphabetized_as": "O",
            "is_living": true,
            "gender": "male",
            "given_name": "Shaquille",
            "description": "American former basketball player and sports analyst on TNT",
            "facts": [],
            "tags": [],
            "score": 6,
            "birth_year": "1972",
            "surname": "O'Neal",
            "nickname": "Shaq",
            "id": 0,
        }
        headers = {
            "Content-Type": "application/json",
            "api_key": "special-key",
            "Authorization": "Bearer special-key",
        }
        response = self.client.open(
            "/v1/entity",
            method="POST",
            headers=headers,
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_delete_entity(self):
        """Test case for delete_entity

        Deletes a entity
        """
        headers = {
            "api_key": "api_key_example",
            "api_key": "special-key",
            "Authorization": "Bearer special-key",
        }
        response = self.client.open(
            "/v1/entity/{entity_id}".format(entity_id=56),
            method="DELETE",
            headers=headers,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_all_entities(self):
        """Test case for get_all_entities

        Returns all entities from the system
        """
        query_string = [
            ("offset", 56),
            ("limit", 56),
            ("updated_since", "2013-10-20T19:20:30+01:00"),
            ("created_since", "2013-10-20T19:20:30+01:00"),
        ]
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/v1/entity", method="GET", headers=headers, query_string=query_string
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_entity_by_id(self):
        """Test case for get_entity_by_id

        Find entity by ID
        """
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/v1/entity/{entity_id}".format(entity_id=56), method="GET", headers=headers
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_update_entity(self):
        """Test case for update_entity

        Update an existing entity
        """
        body = {
            "is_real": true,
            "alphabetized_as": "O",
            "is_living": true,
            "gender": "male",
            "given_name": "Shaquille",
            "description": "American former basketball player and sports analyst on TNT",
            "facts": [],
            "tags": [],
            "score": 6,
            "birth_year": "1972",
            "surname": "O'Neal",
            "nickname": "Shaq",
            "id": 0,
        }
        headers = {
            "Content-Type": "application/json",
            "api_key": "special-key",
            "Authorization": "Bearer special-key",
        }
        response = self.client.open(
            "/v1/entity",
            method="PUT",
            headers=headers,
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    @unittest.skip("application/x-www-form-urlencoded not supported by Connexion")
    def test_update_entity_with_form(self):
        """Test case for update_entity_with_form

        Updates a entity in the database with form data
        """
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "api_key": "special-key",
            "Authorization": "Bearer special-key",
        }
        data = dict(name="name_example", status="status_example")
        response = self.client.open(
            "/v1/entity/{entity_id}".format(entity_id=56),
            method="POST",
            headers=headers,
            data=data,
            content_type="application/x-www-form-urlencoded",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from botticelli.test import BaseTestCase


class TestFactController(BaseTestCase):
    """FactController integration test stubs"""

    def test_add_fact(self):
        """Test case for add_fact

        Add a new fact to the database
        """
        body = {"id": 1, "text": "text", "entity_id": 5}
        headers = {
            "Content-Type": "application/json",
            "api_key": "special-key",
            "Authorization": "Bearer special-key",
        }
        response = self.client.open(
            "/v1/entity/{entity_id}/facts".format(entity_id=56),
            method="POST",
            headers=headers,
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_delete_fact(self):
        """Test case for delete_fact

        Deletes a fact
        """
        headers = {
            "api_key": "api_key_example",
            "api_key": "special-key",
            "Authorization": "Bearer special-key",
        }
        response = self.client.open(
            "/v1/entity/{entity_id}/facts/{fact_id}".format(fact_id=56, entity_id=56),
            method="DELETE",
            headers=headers,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_entity_facts(self):
        """Test case for get_entity_facts

        Returns all entities from the system
        """
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/v1/entity/{entity_id}/facts".format(entity_id=56),
            method="GET",
            headers=headers,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_fact_by_id(self):
        """Test case for get_fact_by_id

        Find fact by ID
        """
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/v1/entity/{entity_id}/facts/{fact_id}".format(fact_id=56, entity_id=56),
            method="GET",
            headers=headers,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_update_fact(self):
        """Test case for update_fact

        Update an existing fact
        """
        body = {"id": 1, "text": "text", "entity_id": 5}
        headers = {
            "Content-Type": "application/json",
            "api_key": "special-key",
            "Authorization": "Bearer special-key",
        }
        response = self.client.open(
            "/v1/entity/{entity_id}/facts".format(entity_id=56),
            method="PUT",
            headers=headers,
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()

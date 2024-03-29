# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from botticelli.test import BaseTestCase


class TestTagController(BaseTestCase):
    """TagController integration test stubs"""

    def test_add_tag(self):
        """Test case for add_tag

        Add a new tag to the database
        """
        body = {"name": "name", "id": 0}
        headers = {
            "Content-Type": "application/json",
            "apiKey": "special-key",
            "Authorization": "Bearer special-key",
        }
        response = self.client.open(
            "/v1/tag",
            method="POST",
            headers=headers,
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_delete_tag(self):
        """Test case for delete_tag

        Deletes a tag
        """
        headers = {
            "apiKey": "apiKey_example",
            "apiKey": "special-key",
            "Authorization": "Bearer special-key",
        }
        response = self.client.open(
            "/v1/tag/{tag_id}".format(tag_id=56), method="DELETE", headers=headers
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_all_tags(self):
        """Test case for get_all_tags

        Returns all tags
        """
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open("/v1/tag", method="GET", headers=headers)
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_tag_by_id(self):
        """Test case for get_tag_by_id

        Find tag by ID
        """
        headers = {
            "Accept": "application/json",
            "apiKey": "special-key",
        }
        response = self.client.open(
            "/v1/tag/{tag_id}".format(tag_id=56), method="GET", headers=headers
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_update_tag(self):
        """Test case for update_tag

        Update an existing tag
        """
        body = {"name": "name", "id": 0}
        headers = {
            "Content-Type": "application/json",
            "apiKey": "special-key",
            "Authorization": "Bearer special-key",
        }
        response = self.client.open(
            "/v1/tag",
            method="PUT",
            headers=headers,
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()

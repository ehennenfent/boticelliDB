# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from botticelli.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_get_user_by_name(self):
        """Test case for get_user_by_name

        Get user by user name
        """
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/v1/user/{username}".format(username="username_example"),
            method="GET",
            headers=headers,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_login_user(self):
        """Test case for login_user

        Logs user into the system
        """
        query_string = [
            ("username", "username_example"),
            ("password", "password_example"),
        ]
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/v1/user/login", method="GET", headers=headers, query_string=query_string
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_logout_user(self):
        """Test case for logout_user

        Logs out current logged in user session
        """
        headers = {}
        response = self.client.open("/v1/user/logout", method="GET", headers=headers)
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()

import logging

import connexion
from flask_testing import TestCase

from botticelli.encoder import JSONEncoder
from botticelli.database import _retarget_engine

_retarget_engine("sqlite:///test.db")


class BaseTestCase(TestCase):
    def create_app(self):
        logging.getLogger("connexion.operation").setLevel("ERROR")
        app = connexion.App(__name__, specification_dir="../openapi/")
        app.app.json_encoder = JSONEncoder
        app.add_api("openapi.yaml", pythonic_params=True)
        return app.app

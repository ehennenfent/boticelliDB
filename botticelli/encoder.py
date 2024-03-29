from connexion.apps.flask_app import FlaskJSONEncoder
import six

from botticelli.database import Base, Gender


class JSONEncoder(FlaskJSONEncoder):
    include_nulls = False

    def default(self, o):
        if isinstance(o, Base):
            dikt = {}
            for attr, _ in six.iteritems(o.openapi_types):
                value = getattr(o, attr)
                if value is None and not self.include_nulls:
                    continue
                attr = o.attribute_map[attr]
                dikt[attr] = value
            return dikt
        if isinstance(o, Gender):
            return o.value
        return FlaskJSONEncoder.default(self, o)

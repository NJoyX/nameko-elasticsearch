from elasticsearch import SerializationError
from elasticsearch.compat import string_types
from elasticsearch.serializer import JSONSerializer as ElasticBaseJSONSerializer, DEFAULT_SERIALIZERS

from .utils import json


class JSONSerializer(ElasticBaseJSONSerializer):
    def loads(self, s):
        try:
            return json.loads(s)
        except (ValueError, TypeError) as e:
            raise SerializationError(s, e)

    def dumps(self, data):
        # don't serialize strings
        if isinstance(data, string_types):
            return data

        try:
            return json.dumps(data, default=self.default, ensure_ascii=False)
        except (ValueError, TypeError) as e:
            raise SerializationError(data, e)


DEFAULT_SERIALIZERS[JSONSerializer.mimetype] = JSONSerializer()

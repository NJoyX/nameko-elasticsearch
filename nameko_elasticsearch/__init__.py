import os

from elasticsearch import Elasticsearch
from elasticsearch_dsl import DocType
from elasticsearch_dsl.connections import connections as dsl_connections
from nameko.extensions import DependencyProvider
from .serializers import JSONSerializer, DEFAULT_SERIALIZERS

__author__ = 'Fill Q'
__all__ = ['ElasticSearch']

ELASTICSEARCH_HOSTS = 'ELASTICSEARCH_HOSTS'


class ElasticSearch(DependencyProvider):
    connections = dsl_connections

    def __init__(self, model=None, index=None, using=None):
        self.model = model if isinstance(model, DocType) else None
        self.using = using
        self.index = index

    def setup(self):
        hosts = os.environ.get(ELASTICSEARCH_HOSTS, 'elasticsearch')
        connection = Elasticsearch(
            map(
                lambda x: x.strip(),
                map(
                    lambda z: z.strip(),
                    filter(None, self.container.config.get(ELASTICSEARCH_HOSTS, hosts).split(','))
                )
            ),
            sniff_on_start=True,
            sniffer_timeout=10,
            sniff_on_connection_fail=True,
            serializer=JSONSerializer(),
            serializers=DEFAULT_SERIALIZERS
        )
        self.connections.add_connection('default', conn=connection)
        if self.model and hasattr(self.model, 'init'):
            self.model.init(index=self.index, using=self.using)

    def get_dependency(self, worker_ctx):
        return self.connections.get_connection()

    def stop(self):
        self.connections.remove_connection('default')

    def kill(self):
        self.stop()

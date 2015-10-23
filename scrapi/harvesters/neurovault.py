"""
NeuroVault (neurovault.org) harvester of public images and collections for the
SHARE Notification Service.

Example API query: http://neurovault.org/api/images/1263/?format=json
"""

from __future__ import unicode_literals

import json
import logging
# from datetime import date, timedelta, datetime
import re
from scrapi import requests
# from scrapi import settings
from scrapi.base import JSONHarvester
from scrapi.linter.document import RawDocument
from scrapi.base.helpers import (build_properties, datetime_formatter,
                                 default_name_parser)

logger = logging.getLogger(__name__)


def process_contributors(authors):

    authors = re.split(',\s|\sand\s', authors)
    return default_name_parser([a for a in authors])


class NeuroVaultHarvester(JSONHarvester):
    short_name = 'neurovault'
    long_name = 'NeuroVault.org'
    url = 'http://www.neurovault.org/'
    count = 0

    @property
    def schema(self):
        return {
            'contributors': ('/authors', process_contributors),
            'uris': {
                'canonicalUri': '/url',
                'objectUri': '/paper_url'
            },
            'title': '/name',
            'providerUpdatedDateTime': ('/modify_date', datetime_formatter),
            'description': '/description',
            'otherProperties': build_properties(
                ('owner_name', '/owner_name'),
                ('doi', '/DOI'),
            )
        }

    def harvest(self, start_date=None, end_date=None):

        api_url = self.url + 'api/collections/?format=json'

        record_list = []

        while True:

            records = requests.get(api_url).json()
            for record in records['results']:
                record_list.append(
                    RawDocument(
                        {
                            'doc': json.dumps(record),
                            'source': self.short_name,
                            'docID': record['id'],
                            'filetype': 'json'
                        }
                    )
                )

        return record_list

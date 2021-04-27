# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"""

import pymongo
from pymongo import MongoClient
from hpOneView.oneview_client import OneViewClient
from st2common.runners.base_action import Action

class HpeOVBaseAction(Action):
    def __init__(self,config):
        super(HpeOVBaseAction, self).__init__(config=config)
        self.client = self._get_client()

    def _get_client(self):
        authx = {
            "ip": self.config['ipaddress'],
            "credentials": {
                "userName": self.config['username'],
                "password": self.config['password']
            }
        }

        client = OneViewClient(authx)

        return client

class MongoBaseAction(Action):
    def __init__(self,config):
        super(MongoBaseAction, self).__init__(config=config)
        self.dbclient = self._get_db_client()

    def _get_db_client(self):
        dbuser = self.config['dbuser']
        dbpass = self.config['dbpass']

        dbclient = MongoClient('mongodb://%s:%s@localhost:27017/' % (dbuser,dbpass))

        return dbclient

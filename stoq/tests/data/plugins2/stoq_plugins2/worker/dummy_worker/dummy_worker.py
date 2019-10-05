#!/usr/bin/env python3

#   Copyright 2014-2018 PUNCH Cyber Analytics Group
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from typing import Optional

from stoq.data_classes import Payload, Request, WorkerResponse
from stoq.plugins import WorkerPlugin


class DummyWorker(WorkerPlugin):

    plugin_name = 'dummy_worker'
    __author__ = 'Marcus LaFerrera'
    __version__ = '0.1-DUP'
    __website__ = 'https://github.com/PUNCH-Cyber/stoq-plugins-public'
    __description__ = (
        'Plugin with duplicate name as dummy_worker for use in test_plugin_override'
    )

    PLUGINS2_DUP_MARKER = True

    async def scan(
        self, payload: Payload, request: Request
    ) -> Optional[WorkerResponse]:
        return None

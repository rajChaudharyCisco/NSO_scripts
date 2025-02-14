#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

NSO Auto check-sync

Copyright (c) 2025 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Rajesh Chaudhary"
__email__ = "rachaud2@cisco.com"
__version__ = "1.1"
__copyright__ = "Copyright (c) 2025 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"


import ncs
import time
import sys
import logging

# Run check-sync on all services
def run_services_check_sync():
    with ncs.maapi.Maapi() as m:
        with ncs.maapi.Session(m, 'admin', 'python'):
            root = ncs.maagic.get_root(m)
            output = root.services.check_sync()
            return (output)
        

def main():
    op = run_services_check_sync()
    for result in op.sync_result:
        print('sync-result {')
        print(' service-id  %s' % result.service_id)
        print(' in-sync %s' % result.in_sync)
        print('}')

if __name__ == '__main__':
    main()

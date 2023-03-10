# coding: utf-8

"""
    MDM API V3

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import mdmv3
from mdmv3.api.devices_v3_api import DevicesV3Api  # noqa: E501
from mdmv3.rest import ApiException


class TestDevicesV3Api(unittest.TestCase):
    """DevicesV3Api unit test stubs"""

    def setUp(self):
        self.api = mdmv3.api.devices_v3_api.DevicesV3Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_devices_v3_get_by_uuid_async(self):
        """Test case for devices_v3_get_by_uuid_async

        New - Get basic details about the device.  # noqa: E501
        """
        pass

    def test_devices_v3_search_async(self):
        """Test case for devices_v3_search_async

        New - Searches the device using the query information provided.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

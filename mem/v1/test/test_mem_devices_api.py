# coding: utf-8

"""
    MEM API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import memv1
from memv1.api.mem_devices_api import MEMDevicesApi  # noqa: E501
from memv1.rest import ApiException


class TestMEMDevicesApi(unittest.TestCase):
    """MEMDevicesApi unit test stubs"""

    def setUp(self):
        self.api = memv1.api.mem_devices_api.MEMDevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_m_em_devices_search(self):
        """Test case for m_em_devices_search

        Searches for the MEM Devices.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
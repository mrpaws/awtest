# coding: utf-8

"""
    MDM API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import mdmv1
from mdmv1.api.device_smart_groups_api import DeviceSmartGroupsApi  # noqa: E501
from mdmv1.rest import ApiException


class TestDeviceSmartGroupsApi(unittest.TestCase):
    """DeviceSmartGroupsApi unit test stubs"""

    def setUp(self):
        self.api = mdmv1.api.device_smart_groups_api.DeviceSmartGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_device_smart_groups_get_smart_groups_assigned_to_device_async(self):
        """Test case for device_smart_groups_get_smart_groups_assigned_to_device_async

        Retrieves all the smart groups associated with the device.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

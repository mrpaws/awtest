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
from mdmv1.api.device_state_metadata_v1_api import DeviceStateMetadataV1Api  # noqa: E501
from mdmv1.rest import ApiException


class TestDeviceStateMetadataV1Api(unittest.TestCase):
    """DeviceStateMetadataV1Api unit test stubs"""

    def setUp(self):
        self.api = mdmv1.api.device_state_metadata_v1_api.DeviceStateMetadataV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_device_state_metadata_v1_get_device_state_metadata_async(self):
        """Test case for device_state_metadata_v1_get_device_state_metadata_async

        New - Get device state attribute metadata for an Organization Group.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

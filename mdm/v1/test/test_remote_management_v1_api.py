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
from mdmv1.api.remote_management_v1_api import RemoteManagementV1Api  # noqa: E501
from mdmv1.rest import ApiException


class TestRemoteManagementV1Api(unittest.TestCase):
    """RemoteManagementV1Api unit test stubs"""

    def setUp(self):
        self.api = mdmv1.api.remote_management_v1_api.RemoteManagementV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_remote_management_v1_get_device_rm_registration_status(self):
        """Test case for remote_management_v1_get_device_rm_registration_status

        New - Gets the device's RM registration information.  # noqa: E501
        """
        pass

    def test_remote_management_v1_initiate_rm_session(self):
        """Test case for remote_management_v1_initiate_rm_session

        New - Initiates a Remote Management session.  # noqa: E501
        """
        pass

    def test_remote_management_v1_register_device_for_rm(self):
        """Test case for remote_management_v1_register_device_for_rm

        New - Registers the device with RM4 server.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

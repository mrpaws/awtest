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
from mdmv1.api.apple_v1_api import AppleV1Api  # noqa: E501
from mdmv1.rest import ApiException


class TestAppleV1Api(unittest.TestCase):
    """AppleV1Api unit test stubs"""

    def setUp(self):
        self.api = mdmv1.api.apple_v1_api.AppleV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_apple_v1_create_remote_view_destination_by_location_group_id(self):
        """Test case for apple_v1_create_remote_view_destination_by_location_group_id

        New - Add a destination for Remote View  # noqa: E501
        """
        pass

    def test_apple_v1_delete_remote_view_destination_by_id(self):
        """Test case for apple_v1_delete_remote_view_destination_by_id

        New - Delete a Remote View destination for the device  # noqa: E501
        """
        pass

    def test_apple_v1_get_remote_view_destination_by_id(self):
        """Test case for apple_v1_get_remote_view_destination_by_id

        New - Gets Remote View destination details for the device  # noqa: E501
        """
        pass

    def test_apple_v1_get_remote_view_destination_by_location_group_id(self):
        """Test case for apple_v1_get_remote_view_destination_by_location_group_id

        New - Gets the list of Remote View destinations configured in the organization group  # noqa: E501
        """
        pass

    def test_apple_v1_update_remote_view_destination_by_id(self):
        """Test case for apple_v1_update_remote_view_destination_by_id

        New - Update the destination details of a previously configured Remote View destination.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
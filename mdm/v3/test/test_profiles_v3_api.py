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
from mdmv3.api.profiles_v3_api import ProfilesV3Api  # noqa: E501
from mdmv3.rest import ApiException


class TestProfilesV3Api(unittest.TestCase):
    """ProfilesV3Api unit test stubs"""

    def setUp(self):
        self.api = mdmv3.api.profiles_v3_api.ProfilesV3Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_profiles_v3_create_device_profile_async(self):
        """Test case for profiles_v3_create_device_profile_async

        New - Create a new profile  # noqa: E501
        """
        pass

    def test_profiles_v3_delete_device_profile_async(self):
        """Test case for profiles_v3_delete_device_profile_async

        New - Delete a Profile  # noqa: E501
        """
        pass

    def test_profiles_v3_get_device_profile_details_async(self):
        """Test case for profiles_v3_get_device_profile_details_async

        New - Retrieve details of a specific profile  # noqa: E501
        """
        pass

    def test_profiles_v3_get_device_profiles(self):
        """Test case for profiles_v3_get_device_profiles

        Get all device profiles as per search filter  # noqa: E501
        """
        pass

    def test_profiles_v3_search_async(self):
        """Test case for profiles_v3_search_async

        New - Search API to Retrieve a list of profiles.  # noqa: E501
        """
        pass

    def test_profiles_v3_update_device_profile(self):
        """Test case for profiles_v3_update_device_profile

        New - Updates Device Profile.  # noqa: E501
        """
        pass

    def test_profiles_v3_upload_profile_payload(self):
        """Test case for profiles_v3_upload_profile_payload

        Uploads a completed (already built for device) profile  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

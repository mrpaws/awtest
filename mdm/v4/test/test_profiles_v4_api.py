# coding: utf-8

"""
    MDM API V4

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import mdmv4
from mdmv4.api.profiles_v4_api import ProfilesV4Api  # noqa: E501
from mdmv4.rest import ApiException


class TestProfilesV4Api(unittest.TestCase):
    """ProfilesV4Api unit test stubs"""

    def setUp(self):
        self.api = mdmv4.api.profiles_v4_api.ProfilesV4Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_profiles_v4_get_device_profile_details_async(self):
        """Test case for profiles_v4_get_device_profile_details_async

        New - Retrive profile details from Profile Id.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

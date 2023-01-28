# coding: utf-8

"""
    System API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import systemv2
from systemv2.api.scim_v2_groups_api import ScimV2GroupsApi  # noqa: E501
from systemv2.rest import ApiException


class TestScimV2GroupsApi(unittest.TestCase):
    """ScimV2GroupsApi unit test stubs"""

    def setUp(self):
        self.api = systemv2.api.scim_v2_groups_api.ScimV2GroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_scim_v2_groups_create_group_async(self):
        """Test case for scim_v2_groups_create_group_async

        New - Create a group.  # noqa: E501
        """
        pass

    def test_scim_v2_groups_get_user_group_by_uuid(self):
        """Test case for scim_v2_groups_get_user_group_by_uuid

        New - Get the group details by UUID  # noqa: E501
        """
        pass

    def test_scim_v2_groups_get_user_groups(self):
        """Test case for scim_v2_groups_get_user_groups

        New - Get a group list  # noqa: E501
        """
        pass

    def test_scim_v2_groups_group_actions_async(self):
        """Test case for scim_v2_groups_group_actions_async

        New - Operations on groups.  # noqa: E501
        """
        pass

    def test_scim_v2_groups_search_groups(self):
        """Test case for scim_v2_groups_search_groups

        New - Search for groups.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
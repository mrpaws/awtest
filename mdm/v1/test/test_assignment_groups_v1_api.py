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
from mdmv1.api.assignment_groups_v1_api import AssignmentGroupsV1Api  # noqa: E501
from mdmv1.rest import ApiException


class TestAssignmentGroupsV1Api(unittest.TestCase):
    """AssignmentGroupsV1Api unit test stubs"""

    def setUp(self):
        self.api = mdmv1.api.assignment_groups_v1_api.AssignmentGroupsV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_assignment_groups_v1_get_assignment_groups_by_search_context(self):
        """Test case for assignment_groups_v1_get_assignment_groups_by_search_context

        New - Returns a list of Assignment Groups matching the search criteria  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
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
from mdmv1.api.admin_action_v1_api import AdminActionV1Api  # noqa: E501
from mdmv1.rest import ApiException


class TestAdminActionV1Api(unittest.TestCase):
    """AdminActionV1Api unit test stubs"""

    def setUp(self):
        self.api = mdmv1.api.admin_action_v1_api.AdminActionV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_action_v1_bulk_admin_action_async(self):
        """Test case for admin_action_v1_bulk_admin_action_async

        New - Executes the admin action for the set of devices after performing necessary checks like command accessibility, device enrollment status, support for command on device etc.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
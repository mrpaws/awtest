# coding: utf-8

"""
    System API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import systemv1
from systemv1.api.admin_identity_v1_api import AdminIdentityV1Api  # noqa: E501
from systemv1.rest import ApiException


class TestAdminIdentityV1Api(unittest.TestCase):
    """AdminIdentityV1Api unit test stubs"""

    def setUp(self):
        self.api = systemv1.api.admin_identity_v1_api.AdminIdentityV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_identity_v1_get_admin_identity(self):
        """Test case for admin_identity_v1_get_admin_identity

        New - Provides identity required to create token for basic and directory admin user.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

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
from mdmv1.api.policies_v1_api import PoliciesV1Api  # noqa: E501
from mdmv1.rest import ApiException


class TestPoliciesV1Api(unittest.TestCase):
    """PoliciesV1Api unit test stubs"""

    def setUp(self):
        self.api = mdmv1.api.policies_v1_api.PoliciesV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_policies_v1_post_async(self):
        """Test case for policies_v1_post_async

        New - Create an Android Update Policy.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

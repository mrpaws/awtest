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
from mdmv1.api.templates_v1_api import TemplatesV1Api  # noqa: E501
from mdmv1.rest import ApiException


class TestTemplatesV1Api(unittest.TestCase):
    """TemplatesV1Api unit test stubs"""

    def setUp(self):
        self.api = mdmv1.api.templates_v1_api.TemplatesV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_templates_v1_get_all_async(self):
        """Test case for templates_v1_get_all_async

        New - Fetch GPO templates  # noqa: E501
        """
        pass

    def test_templates_v1_get_policy_async(self):
        """Test case for templates_v1_get_policy_async

        New - Fetch a policy with it's recommended values  # noqa: E501
        """
        pass

    def test_templates_v1_search_template_async(self):
        """Test case for templates_v1_search_template_async

        New - Find a vendor template  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

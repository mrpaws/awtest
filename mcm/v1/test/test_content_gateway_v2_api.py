# coding: utf-8

"""
    MCM API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import mcmv1
from mcmv1.api.content_gateway_v2_api import ContentGatewayV2Api  # noqa: E501
from mcmv1.rest import ApiException


class TestContentGatewayV2Api(unittest.TestCase):
    """ContentGatewayV2Api unit test stubs"""

    def setUp(self):
        self.api = mcmv1.api.content_gateway_v2_api.ContentGatewayV2Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_content_gateway_v2_content_gateway_configuration_bulk_delete_async(self):
        """Test case for content_gateway_v2_content_gateway_configuration_bulk_delete_async

        New - Deletes Content Gateway configurations.  # noqa: E501
        """
        pass

    def test_content_gateway_v2_content_gateway_configuration_delete_async(self):
        """Test case for content_gateway_v2_content_gateway_configuration_delete_async

        New - Deletes a Content Gateway configuration.  # noqa: E501
        """
        pass

    def test_content_gateway_v2_create_content_gateway_configuration_async(self):
        """Test case for content_gateway_v2_create_content_gateway_configuration_async

        New - Creates a Content Gateway Configuration  # noqa: E501
        """
        pass

    def test_content_gateway_v2_get_content_gateway_configuration_custom_settings_by_id_async(self):
        """Test case for content_gateway_v2_get_content_gateway_configuration_custom_settings_by_id_async

        New - Gets the content gateway configurations and the certificate details with custom settings.  # noqa: E501
        """
        pass

    def test_content_gateway_v2_get_content_gateway_configurations_async(self):
        """Test case for content_gateway_v2_get_content_gateway_configurations_async

        New - Gets the content gateway configurations  # noqa: E501
        """
        pass

    def test_content_gateway_v2_get_content_gateway_configurations_by_id_async(self):
        """Test case for content_gateway_v2_get_content_gateway_configurations_by_id_async

        New - gets the content gateway configurations and the certificate details  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

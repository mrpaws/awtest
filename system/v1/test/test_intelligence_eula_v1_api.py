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
from systemv1.api.intelligence_eula_v1_api import IntelligenceEulaV1Api  # noqa: E501
from systemv1.rest import ApiException


class TestIntelligenceEulaV1Api(unittest.TestCase):
    """IntelligenceEulaV1Api unit test stubs"""

    def setUp(self):
        self.api = systemv1.api.intelligence_eula_v1_api.IntelligenceEulaV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_intelligence_eula_v1_accept_eula_async(self):
        """Test case for intelligence_eula_v1_accept_eula_async

        New - Accept intelligence EULA details.  # noqa: E501
        """
        pass

    def test_intelligence_eula_v1_get_eula_async(self):
        """Test case for intelligence_eula_v1_get_eula_async

        New - Gets EULA for Intelligence of given organization group.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

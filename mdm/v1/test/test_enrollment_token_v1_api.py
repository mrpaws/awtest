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
from mdmv1.api.enrollment_token_v1_api import EnrollmentTokenV1Api  # noqa: E501
from mdmv1.rest import ApiException


class TestEnrollmentTokenV1Api(unittest.TestCase):
    """EnrollmentTokenV1Api unit test stubs"""

    def setUp(self):
        self.api = mdmv1.api.enrollment_token_v1_api.EnrollmentTokenV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_enrollment_token_v1_create_async(self):
        """Test case for enrollment_token_v1_create_async

        New - Creates device enrollment token based on registration type  # noqa: E501
        """
        pass

    def test_enrollment_token_v1_delete_by_id_async(self):
        """Test case for enrollment_token_v1_delete_by_id_async

        New - Delete device enrollment token  # noqa: E501
        """
        pass

    def test_enrollment_token_v1_get_by_criteria_async(self):
        """Test case for enrollment_token_v1_get_by_criteria_async

        New - Returns a list of enrollment tokens that match the search criteria  # noqa: E501
        """
        pass

    def test_enrollment_token_v1_get_by_id_async(self):
        """Test case for enrollment_token_v1_get_by_id_async

        New - Get device enrollment token details  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

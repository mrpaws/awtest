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
from systemv1.api.enrollment_customization_settings_v1_api import EnrollmentCustomizationSettingsV1Api  # noqa: E501
from systemv1.rest import ApiException


class TestEnrollmentCustomizationSettingsV1Api(unittest.TestCase):
    """EnrollmentCustomizationSettingsV1Api unit test stubs"""

    def setUp(self):
        self.api = systemv1.api.enrollment_customization_settings_v1_api.EnrollmentCustomizationSettingsV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_enrollment_customization_settings_v1_get_enrollment_customizations_settings_for_og_async(self):
        """Test case for enrollment_customization_settings_v1_get_enrollment_customizations_settings_for_og_async

        New - Get Enrollment Customizations settings for the given Organization Group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

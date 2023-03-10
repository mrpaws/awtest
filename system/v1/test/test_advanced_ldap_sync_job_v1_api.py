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
from systemv1.api.advanced_ldap_sync_job_v1_api import AdvancedLdapSyncJobV1Api  # noqa: E501
from systemv1.rest import ApiException


class TestAdvancedLdapSyncJobV1Api(unittest.TestCase):
    """AdvancedLdapSyncJobV1Api unit test stubs"""

    def setUp(self):
        self.api = systemv1.api.advanced_ldap_sync_job_v1_api.AdvancedLdapSyncJobV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_advanced_ldap_sync_job_v1_advanced_ldap_sync_job_details_async(self):
        """Test case for advanced_ldap_sync_job_v1_advanced_ldap_sync_job_details_async

        New - Gets Advanced Ldap Sync job details for a particular Organization group. Allows admins to preview the all the job details for a specific OG.  # noqa: E501
        """
        pass

    def test_advanced_ldap_sync_job_v1_approve_or_decline_advanced_ldap_sync_job_async(self):
        """Test case for advanced_ldap_sync_job_v1_approve_or_decline_advanced_ldap_sync_job_async

        New - Approves or declines the created LDAP sync job.  # noqa: E501
        """
        pass

    def test_advanced_ldap_sync_job_v1_create_advanced_ldap_sync_job_async(self):
        """Test case for advanced_ldap_sync_job_v1_create_advanced_ldap_sync_job_async

        New - Creates a new LDAP sync job.  # noqa: E501
        """
        pass

    def test_advanced_ldap_sync_job_v1_get_job_status_async(self):
        """Test case for advanced_ldap_sync_job_v1_get_job_status_async

        New - Gets LDAP sync job details.  # noqa: E501
        """
        pass

    def test_advanced_ldap_sync_job_v1_preview_advanced_ldap_sync_job_async(self):
        """Test case for advanced_ldap_sync_job_v1_preview_advanced_ldap_sync_job_async

        New - Gets LDAP sync job details. Allows admins to preview the changes to enrollment user attributes.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

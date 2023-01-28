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
from mdmv1.api.certificates_api import CertificatesApi  # noqa: E501
from mdmv1.rest import ApiException


class TestCertificatesApi(unittest.TestCase):
    """CertificatesApi unit test stubs"""

    def setUp(self):
        self.api = mdmv1.api.certificates_api.CertificatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_certificates_get_certificates_by_alternate_id(self):
        """Test case for certificates_get_certificates_by_alternate_id

        Retrieves certificate details of the device identified by the alternate Id's.  # noqa: E501
        """
        pass

    def test_certificates_get_certificates_by_device(self):
        """Test case for certificates_get_certificates_by_device

        Retrieves certificate details of the device identified by device Id.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

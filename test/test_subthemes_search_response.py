# coding: utf-8

"""
    Querido Diário

    API to access the gazettes from all Brazilian cities

    The version of the OpenAPI document: 0.17.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from quedapi.models.subthemes_search_response import SubthemesSearchResponse  # noqa: E501

class TestSubthemesSearchResponse(unittest.TestCase):
    """SubthemesSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubthemesSearchResponse:
        """Test SubthemesSearchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubthemesSearchResponse`
        """
        model = SubthemesSearchResponse()  # noqa: E501
        if include_optional:
            return SubthemesSearchResponse(
                subthemes = [
                    ''
                    ]
            )
        else:
            return SubthemesSearchResponse(
                subthemes = [
                    ''
                    ],
        )
        """

    def testSubthemesSearchResponse(self):
        """Test SubthemesSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

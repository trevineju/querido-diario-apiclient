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

from quedapi.models.gazette_search_response import GazetteSearchResponse  # noqa: E501

class TestGazetteSearchResponse(unittest.TestCase):
    """GazetteSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GazetteSearchResponse:
        """Test GazetteSearchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GazetteSearchResponse`
        """
        model = GazetteSearchResponse()  # noqa: E501
        if include_optional:
            return GazetteSearchResponse(
                total_gazettes = 56,
                gazettes = [
                    quedapi.models.gazette_item.GazetteItem(
                        territory_id = '', 
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        scraped_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        url = '', 
                        territory_name = '', 
                        state_code = '', 
                        excerpts = [
                            ''
                            ], 
                        edition = '', 
                        is_extra_edition = True, 
                        txt_url = '', )
                    ]
            )
        else:
            return GazetteSearchResponse(
                total_gazettes = 56,
                gazettes = [
                    quedapi.models.gazette_item.GazetteItem(
                        territory_id = '', 
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        scraped_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        url = '', 
                        territory_name = '', 
                        state_code = '', 
                        excerpts = [
                            ''
                            ], 
                        edition = '', 
                        is_extra_edition = True, 
                        txt_url = '', )
                    ],
        )
        """

    def testGazetteSearchResponse(self):
        """Test GazetteSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

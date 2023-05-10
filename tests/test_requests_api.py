from smardwrapper import requests_api as api
import itertools


def test_get_timestamps():
    for filter_number, region, resolution in itertools.product(*[api.FILTER_LIST, api.REGION_LIST, api.RESOLUTION_LIST]):
        print(api.get_timestamps(filter_number=filter_number, region=region, resolution=resolution))
        assert api.get_timestamps(filter_number=filter_number, region=region, resolution=resolution).status_code == 200

import requests

# List of all possible filters
FILTER_LIST = [1223, 1224, 1225, 1226, 1227, 1228, 4066, 4067, 4068, 4069, 4070, 4071, 410, 4359, 4387, 4169, 5078,
               4996, 4997, 4170, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 3791, 123, 125, 715, 5097, 122]

# List of all possible regions
REGION_LIST = ['DE', 'AT', 'LU', 'DE-LU', 'DE-AT-LU', '50Hertz', 'Amprion', 'TenneT', 'TransnetBW', 'APG', 'Creos']

# List of all possible resolutions
RESOLUTION_LIST = ['hour', 'quarterhour', 'day', 'week', 'month', 'year']


def get_timestamps(filter_number, region, resolution):
    url = "https://smard.api.proxy.bund.dev/app/chart_data/" + str(filter_number) + "/" + str(region) + "/index_" + str(
        resolution) + ".json"
    return requests.get(url)


def get_chart_data(filter_number, region, resolution, int_timestamp):
    url = "https://smard.api.proxy.bund.dev/app/chart_data/" + str(filter_number) + "/" + str(region) + "/" + str(
        filter_number) + "_" + str(region) + "_" + str(resolution) + "_" + str(int_timestamp) + ".json"
    return requests.get(url)


def get_table_data(filter_number, region, int_timestamp):
    url = "https://smard.api.proxy.bund.dev/app/table_data/" + str(filter_number) + "/" + str(region) + "/" + str(
        filter_number) + "_" + str(region) + "_quarterhour_" + str(int_timestamp) + ".json"
    return requests.get(url)

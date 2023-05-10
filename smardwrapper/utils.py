import pandas as pd
import numpy as np


def int_to_datetime(timestamp):
    return pd.to_datetime(timestamp, unit='ms')


def datetime_to_int(timestamp):
    return int(timestamp.value / 1e6)


def clip_timestamp_list(timestamp_list, start_datetime_int, end_datetime_int):
    lower_bound_idx = np.argmin(np.abs(timestamp_list - start_datetime_int))
    if (timestamp_list[lower_bound_idx] > start_datetime_int) & (lower_bound_idx > 0):
        lower_bound_idx -= 1

    upper_bound_idx = np.argmin(np.abs(timestamp_list - end_datetime_int))
    if (timestamp_list[upper_bound_idx] < end_datetime_int) & (upper_bound_idx < len(timestamp_list) - 1):
        upper_bound_idx += 2

    return timestamp_list[lower_bound_idx:upper_bound_idx]


def extract_energy_data_from_json(energy_json):
    data = []
    for el in energy_json['series']:
        if el['versions'][0]['value'] is None:  # no value for timestamp
            continue
        data.append([el['timestamp'], el['versions'][0]['value']])
    return data

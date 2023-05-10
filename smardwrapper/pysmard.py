import pandas as pd
import numpy as np
import itertools

from . import requests_api, utils


def get_energy_data(filter_number, region, resolution, start_datetime=None, end_datetime=None, convert_datetime=True):
    if type(filter_number) is int:
        filter_number = [filter_number]
    if type(region) is str:
        region = [region]

    start_datetime_int = utils.datetime_to_int(pd.to_datetime(start_datetime))
    end_datetime_int = utils.datetime_to_int(pd.to_datetime(end_datetime))

    all_timestamps = requests_api.get_timestamps(filter_number[0], region[0], resolution).json()['timestamps']
    all_timestamps = np.array(all_timestamps)

    # rough clipping of timestamps - prevents unnecessary api calls
    clipped_timestamps = utils.clip_timestamp_list(all_timestamps, start_datetime_int, end_datetime_int)

    full_energy_df = pd.DataFrame(columns=['filter', 'region', 'timestamp', 'value'])

    for fn, r, ts in itertools.product(filter_number, region, clipped_timestamps):
        energy_data = requests_api.get_chart_data(
            filter_number=fn,
            region=r,
            resolution=resolution,
            int_timestamp=ts
        ).json()['series']
        energy_df = pd.DataFrame(energy_data, columns=['timestamp', 'value'])
        energy_df['filter'] = fn
        energy_df['region'] = r
        full_energy_df = pd.concat([full_energy_df, energy_df])

    full_energy_df.reset_index(drop=True, inplace=True)
    # fine granular clip of timestamps
    fine_granular_condition = (full_energy_df['timestamp'] >= start_datetime_int) & (
            full_energy_df['timestamp'] <= end_datetime_int)
    full_energy_df.drop(full_energy_df[(~fine_granular_condition)].index, inplace=True)

    if convert_datetime:
        full_energy_df['timestamp'] = pd.to_datetime(full_energy_df['timestamp'],
                                                     unit='ms')

    return full_energy_df.reset_index(drop=True)

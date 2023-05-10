# SMARD Wrapper

A (better) python wrapper for [SMARD API](https://smard.api.bund.dev/).

## Installation

Install python package via pip:
```shell
pip install "git+https://github.com/eric-kaufmann/smardwrapper.git"
```

## Usage

```python
from smardwrapper.pysmard import get_energy_data

get_energy_data(
    filter_number: int or list[int],
    region: str or list[str],
    resolution: str in ['hour', 'quarterhour', 'day', 'week', 'month', 'year'],
    start_datetime: str or pd.Timestamp,
    end_datetime: str or pd.Timestamp
) -> pd.DataFrame
```

### Input Values

- **filter_number:** (type: *int* or *list[int]*)

| filter number | description                                      |
|:-------------:|--------------------------------------------------|
|     1223      | Stromerzeugung: Braunkohle                       |
|     1224      | Stromerzeugung: Kernenergie                      |
|     1225      | Stromerzeugung: Wind Offshore                    |
|     1226      | Stromerzeugung: Wasserkraft                      |
|     1227      | Stromerzeugung: Sonstige Konventionelle          |
|     1228      | Stromerzeugung: Sonstige Erneuerbare             |
|     4066      | Stromerzeugung: Biomasse                         |
|     4067      | Stromerzeugung: Wind Onshore                     |
|     4068      | Stromerzeugung: Photovoltaik                     |
|     4069      | Stromerzeugung: Steinkohle                       |
|     4070      | Stromerzeugung: Pumpspeicher                     |
|     4071      | Stromerzeugung: Erdgas                           |
|      410      | Stromverbrauch: Gesamt (Netzlast)                |
|     4359      | Stromverbrauch: Residuallast                     |
|     4387      | Stromverbrauch: Pumpspeicher                     |
|     4169      | Marktpreis: Deutschland/Luxemburg                |
|     5078      | Marktpreis: Anrainer DE/LU                       |
|     4996      | Marktpreis: Belgien                              |
|     4997      | Marktpreis: Norwegen 2                           |
|     4170      | Marktpreis: Österreich                           |
|      252      | Marktpreis: Dänemark 1                           |
|      253      | Marktpreis: Dänemark 2                           |
|      254      | Marktpreis: Frankreich                           |
|      255      | Marktpreis: Italien (Nord)                       |
|      256      | Marktpreis: Niederlande                          |
|      257      | Marktpreis: Polen                                |
|      258      | Marktpreis: Polen                                |
|      259      | Marktpreis: Schweiz                              |
|      260      | Marktpreis: Slowenien                            |
|      261      | Marktpreis: Tschechien                           |
|      262      | Marktpreis: Ungarn                               |
|     3791      | Prognostizierte Erzeugung: Offshore              |
|      123      | Prognostizierte Erzeugung: Onshore               |
|      125      | Prognostizierte Erzeugung: Photovoltaik          |
|      715      | Prognostizierte Erzeugung: Sonstige              |
|     5097      | Prognostizierte Erzeugung: Wind und Photovoltaik |
|      122      | Prognostizierte Erzeugung: Gesamt                |

- **region** (type: *str* or *list[str]*)

|   region   | description                            |
|:----------:|----------------------------------------|
|     DE     | Land: Deutschland                      |
|     AT     | Land: Österreich                       |
|     LU     | Land: Luxemburg                        |
|   DE-LU    | Marktgebiet: DE/LU (ab 01.10.2018)     |
|  DE-AT-LU  | Marktgebiet: DE/AT/LU (bis 30.09.2018) |
|  50Hertz   | Regelzone (DE): 50Hertz                |
|  Amprion   | Regelzone (DE): Amprion                |
|   TenneT   | Regelzone (DE): TenneT                 |
| TransnetBW | Regelzone (DE): TransnetBW             |
|    APG     | SRegelzone (AT): APG                   |
|   Creos    | Regelzone (LU): Creos                  |

- **resolution** (type: *str*)

  - *hour*
  - *quarterhour*
  - *day*
  - *week*
  - *month*
  - *year*


### Output

**type:** *pd.DataFrame*

|   | filter | region | timestamp           | value   |
|---|--------|--------|---------------------|---------|
| 1 | 1223   | DE     | 2020-01-01 00:00:00 | 9419.00 |
| 2 | 1223   | DE     | 2020-01-01 01:00:00 | 9425.75 |
| 3 | 1224   | DE     | 2020-01-01 00:00:00 | 7214.45 |


### Example

```python
from smardwrapper import pysmard as api

result_df = api.get_energy_data(
    filter_number=[1223, 1224, 1225],
    region='DE',
    resolution='hour',
    start_datetime="2020-01-01",
    end_datetime="2020-02-01"
)
print(result_df)
```
*Out:*

|     | filter | region | timestamp           | value   |
|-----|--------|--------|---------------------|---------|
| 1   | 1223   | DE     | 2020-01-01 00:00:00 | 9419.00 |
| 2   | 1223   | DE     | 2020-01-01 01:00:00 | 9425.75 |
| 3   | 1223   | DE     | 2020-01-01 02:00:00 | 9497.25 |
| 4   | 1223   | DE     | 2020-01-01 03:00:00 | 9549.75 |
| 5   | 1223   | DE     | 2020-01-01 04:00:00 | 9466.75 |
| ... | ...    | ...    | ...                 | ...     |

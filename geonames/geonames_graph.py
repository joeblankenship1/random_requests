#! python3

"""
hierarchy: parentId, childId, type
The type 'ADM' stands for the admin hierarchy modeled by the admin1-4 codes.
The other entries are entered with the user interface.
The relation toponym-adm hierarchy is not included in the file, it can instead
be built from the admincodes of the toponym.

cities500: all cities with a population > 500 or seats of adm div down to
PPLA4 (ca 185.000), see 'geoname' table for columns
"""

# %%
import pandas as pd

# %%
hierarchy_raw = '~/Downloads/geonames/hierarchy.txt'
cities_500_raw = '~/Downloads/geonames/cities500.txt'
countries_raw = '~/Downloads/geonames/countryInfo.txt'

# %%
city_500_df = pd.read_csv(cities_500_raw, delimiter='\t', header=None)
city_ids_df = city_500_df[[0, 1, 4, 5]]
city_ids_df = city_ids_df.rename(columns={0: 'geonameid', 1: 'name', 4: 'latitude', 5: 'longitude'})

# %%
countryinfo_df = pd.read_csv(countries_raw, delimiter='\t')
country_ids_df = countryinfo_df[['ISO', 'geonameid']]

# %%
hierarchy_df = pd.read_csv(hierarchy_raw, delimiter='\t', header=None)
hierarchy_city = hierarchy_df.loc[hierarchy_df[2] == 'ADM']

# %%
city_ids_df.to_csv('city_nodes.csv')
hierarchy_city.to_csv('hierarchy_edges.csv')

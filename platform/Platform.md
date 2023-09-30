# Platform Subteam

### cities.json
- Contains city_name(city), population, state, and population_density information
- There are 624 different city elements
- The cities are only in Georgia
- There are no null values and it seems that every city is accounted for in the state of Georgia 
- The file is sorted by population density, most to least
- The data shows the total population of all the cities is ~4.6 million yet a simple Google search yields ~10.8 million so either there is missing data for the state of Georgia or the data is just really old (1970?)   
    - The mean population for the cities is ~7400
    - The median population for the cities is ~1500
    - Population is skewed right 
- Population density is probably in people per square miles
    - The mean population density for the cities is ~820
    - The median population density for the cities is ~560
    - Population density is skewed right

### FP_to_country.xlsx (from Advait)
- List of all 159 counties of GA
- County names in alphabetical order
- Two columns: FIPS code and associated county name

### ZIP_TRACT_122021.xlsx
- Contains zip code (zip), tract, usps_zip_pref_city, usps_zip_pref_state,
  res_ratio, bus_ratio, oth_ratio, and tot_ratio
- tract is the census tract which is a way of grouping geographic areas
    -there are multiple tracts per zip code
- There are 4818 total entries
    - each describes a unique census tract and are grouped by zip code/city
    - the cities are only Georgia cities (only 621) so there is not a one-to-one
      match with city data
- the ratios describe the ratio of deliveries for a given zip code that are in
  the given census tract
    - res is residential deliveries
    - bus is business deliveries
    - oth is other deliveries
    - tot is total deliveries
- there are no null values in the dataset but there are suspicious ones and
  zeroes that seem to act like null values as the 0's are probably for null and
  having multiple 1's in a row seems suspicious
    - if consider null values to be 0 or 1
    - null value for following columns are:
        - res: 3.28%
        - bus: 5.23%
        - oth: 7.16%
        - tot: 5.13%
- Mean and median for ratio columns
    - res mean/median: 0.169/0.0750
    - bus mean/median: 0.180/0.0458
    - oth mean/median: 0.166/0.0281
    - tot mean/median: 0.189/0.0801
        - skewed right
- Mean and median for ratio columns after removing rows with "null values"
    - res mean/median: 0.120/0.0679
    - bus mean/median: 0.118/0.0371
    - oth mean/median: 0.103/0.0211
    - tot mean/median: 0.121/0.0675
        - skewed right
- **Question:** How is it that the total ratio is greater than any of the
  individual ratios? Should it not be the case that since the total ratio is a
  weighted average of the other ratios it cannot be greater. This is true for
  any individual row but when calculate on entire column this fact seems to
  disappear. Any thoughts?
- **TODO:**
    - combine data for each city in some manner for better comparisons across
      different data files

### censusData.xlsx
- did not look at

### data.csv
- did not look at

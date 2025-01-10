import pandas as pd
import os

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


cwd = os.getcwd()
fileName = 'WORLD HERITAGE SITES 2024 UPDATED.csv'
dataPath = os.path.join(cwd,'data')
filePath = os.path.join(dataPath,fileName)

df = pd.read_csv(filePath)

# Initialize geolocator
geolocator = Nominatim(user_agent="unesco_site_locator")

# Function to get address based on Site Name and Country
def get_address(site_name, country):
    try:
        location = geolocator.geocode(f"{site_name}, {country}")
        if location:
            return location.address
        else:
            return "Address not found"
    except GeocoderTimedOut:
        return "Geocoding service timed out"

# Apply the function to each row to get the address
df['Address'] = df.apply(lambda row: get_address(row['Site Name'], row['Country']), axis=1)

print(df.head(100))

print('Finish')
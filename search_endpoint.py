import os
import requests
from requests.auth import HTTPBasicAuth

# our demo filter that filters by geometry, date and cloud cover
from filters import redding_reservoir

# Search API request object
search_endpoint_request = {
  "item_types": ["REOrthoTile",
"PSScene4Band",
"PSScene3Band",
"Sentinel1",
"REOrthoTile",
"MOD09GA",
"MYD09GA",
"PSOrthoTile"],
  "filter": redding_reservoir
}

result = \
  requests.post(
    'https://api.planet.com/data/v1/quick-search',
    auth=HTTPBasicAuth(os.environ['PL_API_KEY'], ''),
    json=search_endpoint_request)

print(result.text)

geo_json_geometry = {
"type": "Polygon",
        "coordinates": [
          [
            [
              -110.33260345458984,
              24.29940685014932
            ],
            [
              -110.32378435134888,
              24.29940685014932
            ],
            [
              -110.32378435134888,
              24.302398987537796
            ],
            [
              -110.33260345458984,
              24.302398987537796
            ],
            [
              -110.33260345458984,
              24.29940685014932
            ]
          ]
        ]
}

# filter for items the overlap with our chosen geometry
geometry_filter = {
  "type": "GeometryFilter",
  "field_name": "geometry",
  "config": geo_json_geometry
}

# filter images acquired in a certain date range
date_range_filter = {
  "type": "DateRangeFilter",
  "field_name": "acquired",
  "config": {
    "gte": "2016-07-01T00:00:00.000Z",
    "lte": "2016-08-01T00:00:00.000Z"
  }
}

# filter any images which are more than 50% clouds
cloud_cover_filter = {
  "type": "RangeFilter",
  "field_name": "cloud_cover",
  "config": {
    "lte": 0.5
  }
}

# create a filter that combines our geo and date filters
# could also use an "OrFilter"
redding_reservoir = {
  "type": "AndFilter",
  "config": [geometry_filter, date_range_filter, cloud_cover_filter]
}

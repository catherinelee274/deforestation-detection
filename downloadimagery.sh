#!/bin/bash


echo "What is your API_ID?"
read id

export PL_API_KEY=$id

echo "What is the starting date (in yyyy/mm/dd) for your search?"
read date1

echo "What is the ending date (in yyyy/mm/dd) for your search?"
read date2

planet data search --item-type PSScene4Band --geom lapaz.geojson --date acquired gte $date1 --date acquired lte $date2 --range cloud_cover lt .1


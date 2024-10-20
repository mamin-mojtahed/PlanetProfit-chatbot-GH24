import streamlit as st

st.title("Estimate your regional savings")

import requests
import geopandas as gpd
import pandas as pd

zipcode = st.text_input("Enter your postal code in Kitchener:", placeholder="e.g. N2G1H6 (Communitech, Kitchener)")
zipcode.replace(" ", "")

if st.button("Calculate") and zipcode.strip() != "":
	service_url = "https://services1.arcgis.com/qAo1OsXi67t7XgmS/arcgis/rest/services/TreeEquity_WFL1/FeatureServer/13/query?outFields=*&where=1%3D1&f=geojson"
	response = requests.get(service_url)
	data = response.json()

	# Putting coordinates into CSV file for quick lookup
	coordinates_list = []

	for feature in data['features']:
		if 'geometry' in feature and 'coordinates' in feature['geometry']:
			coordinates = feature['geometry']['coordinates']
			coordinates_list.append(coordinates)

	df = pd.DataFrame(coordinates_list, columns=['Coordinates'])
	df.to_csv('coordinates.csv', index=False)


	# Get coordinates from zip-code
	csv_path = 'CanadianPostalCodes.csv'
	cc = pd.read_csv(csv_path)
	cc = cc[['PostalCode', 'Latitude', 'Longitude']].rename(columns={'PostalCode': 'postcode', 'Latitude': 'lat', 'Longitude': 'lon'})
	mydata = pd.DataFrame({'postcode': [zipcode]})
	mydata_aug = pd.merge(mydata, cc, on="postcode", how="left")
	lon = mydata_aug['lon'].iloc[0]
	lat = mydata_aug['lat'].iloc[0]
	coordinate_tuple = (lon, lat)

	# Find which Kitchener region the zip code is in
	df = pd.read_csv('coordinates.csv')
	def is_point_inside_polygon(x, y, poly):
		"""
		Determine if a point is inside a polygon using the ray casting algorithm.

		Args:
		x (float): x-coordinate of the point
		y (float): y-coordinate of the point
		poly (list of tuples): List of tuples representing the vertices of the polygon

		Returns:
		bool: True if the point is inside the polygon, False otherwise
		"""
		n = len(poly)
		inside = False

		p1x, p1y = poly[0]
		for i in range(n + 1):
			p2x, p2y = poly[i % n]
			if y > min(p1y, p2y):
				if y <= max(p1y, p2y):
					if x <= max(p1x, p2x):
						if p1y != p2y:
							xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
						if p1x == p2x or x <= xinters:
							inside = not inside
			p1x, p1y = p2x, p2y

		return inside

	target_id = -1

	for index, row in df.iterrows():
		region_coordinates = eval(row['Coordinates'])
		if is_point_inside_polygon(coordinate_tuple[0], coordinate_tuple[1], region_coordinates):
			target_id = index + 1
			break
	else:
		st.write("The zip code is invalid or not inside Kitchener.")
		st.stop()


	# Pulling the desired data
	if target_id != -1:
		gdf = gpd.GeoDataFrame.from_features(data['features'])
		filtered_gdf = gdf.loc[gdf['OBJECTID'] == target_id]

		selected_columns = ['mean_surfacetemp', 'heat_disparity']
		filtered_properties = filtered_gdf[['OBJECTID'] + selected_columns]

		st.write(filtered_properties)

		# Save the selected properties to a CSV file
		filtered_properties.to_csv('filtered_line_data.csv', index=False)

	# 93.6 days of summer

	st.write("\"It's estimated to reduce energy costs by around 1-3% per degree for each 8-hour period\"")
	st.markdown('<small>~ <a href="https://thomasgalbraith.com" target="_blank">thomasgalbraith.com</a></small>', unsafe_allow_html=True)

	mean_surfacetemp = filtered_properties['mean_surfacetemp'].iloc[0]
	lowerBound = 93.6 * (mean_surfacetemp - 20) / 100

	higherBound = 3 * lowerBound

	col1, col2 = st.columns(2)
	with col1:
		st.write("Lower Bound Savings:")
		st.write("$", round(lowerBound, 2))
	with col2:
		st.write("Higher Bound Savings:")
		st.write("$", round(higherBound, 2))
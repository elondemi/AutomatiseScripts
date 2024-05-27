import json

# Load the JSON data from input.json
with open('new_input.json') as file:
    data = json.load(file)

# Filter out streets without a specified number of cars
filtered_streets = [street for street in data['streets'] if not 'number_of_cars' in street]

# Update the data with the filtered streets
data['streets'] = filtered_streets

# Write the modified JSON data to a new file
with open('filtered_input.json', 'w') as file:
    json.dump(data, file, indent=2)

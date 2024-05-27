import json
import random

# Load the JSON data from input.json
with open('input.json') as file:
    data = json.load(file)

# Load the JSON data from output.json
with open('output.json') as file:
    output_data = json.load(file)

# Function to generate random numbers
def generate_random_numbers():
    return random.randint(1, 100)

# Dictionary to store the sum of green times for each street
street_green_times = {}

# Loop through streets in output.json
for street_info in output_data['streets']:
    street_name = list(street_info.keys())[0]
    green_time = street_info[street_name]
    
    # Sum up green times for duplicate streets
    if street_name in street_green_times:
        street_green_times[street_name] += green_time
    else:
        street_green_times[street_name] = green_time

# Loop through streets in input.json
for street in data['streets']:
    street_name = street['name']
    if street_name in street_green_times:
        street['green_time'] = street_green_times[street_name]
        street['number_of_cars'] = random.randint(50, 200)

# Write the modified JSON data to a new file
with open('new_input.json', 'w') as file:
    json.dump(data, file, indent=2)

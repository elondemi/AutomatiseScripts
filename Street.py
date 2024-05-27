import json

# Load JSON files
with open('new_input.json', 'r') as file:
    data = json.load(file)

with open('numberOfCars.json', 'r') as file:
    number_of_cars_data = json.load(file)

with open('ExitRoads.json', 'r') as file:
    exit_roads_data = file.readlines()

# Create a dictionary mapping street names to the number of cars
number_of_cars_map = {key: value for key, value in number_of_cars_data.items()}

# Create a dictionary mapping street names to their exit road names
exit_roads_map = {}
for line in exit_roads_data:
    parts = line.strip().split()
    if len(parts) >= 3:  # Ensure there are enough parts in the split result
        street_id, street_name, exit_road_name = parts[0], parts[1], parts[2]
        exit_roads_map[street_name] = exit_road_name

streets = []
street_name_to_id = {}

# Generate street IDs and map street names to their IDs
for idx, street_data in enumerate(data['streets'], start=1):
    street_name = street_data['name']
    street_name_to_id[street_name] = idx

# Iterate over each street entry in the JSON data
for street_data in data['streets']:
    # Extract street data
    street_name = street_data['name']
    start_intersection_id = street_data['start']
    end_intersection_id = street_data['end']
    time = street_data['time']
    green_time = street_data.get('green_time', 0)  # Fetch green_time from JSON, defaulting to 0 if not present

    # Get the number of cars from the mapping dictionary
    number_of_cars = number_of_cars_map.get(street_name, 0)  # Default to 0 if not found

    # Determine the exit road ID
    exit_road_name = exit_roads_map.get(street_name, None)
    exit_road_id = street_name_to_id.get(exit_road_name, None) if exit_road_name else None

    # Add the street to the streets list
    street = {
        'Name': street_name,
        'StartIntersectionID': start_intersection_id,
        'EndIntersectionID': end_intersection_id,
        'Time': time,
        'NumberOfCars': number_of_cars,
        'GreenTime': green_time,
        'ExitRoad': exit_road_id
    }
    streets.append(street)

# Output the generated data for Street
print("public static List<Street> GetStreets()")
print("{")
print("    return new List<Street>")
print("    {")
for idx, street in enumerate(streets, start=1):
    exit_road_str = "null" if street['ExitRoad'] is None else street['ExitRoad']
    print(f"        new Street {{ StreetID = {idx}, Name = \"{street['Name']}\", StartIntersectionID = {street['StartIntersectionID']}, EndIntersectionID = {street['EndIntersectionID']}, Time = {street['Time']}, GreenTime = {street['GreenTime']}, NumberOfCars = {street['NumberOfCars']}, ExitRoad = {exit_road_str} }},")
print("    };")
print("}")

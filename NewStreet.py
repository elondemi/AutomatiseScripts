import json

# Load JSON files
with open('new_input.json', 'r') as file:
    data = json.load(file)

with open('numberOfCars.json', 'r') as file:
    number_of_cars_data = json.load(file)

with open('exit_roads_pr_fk.csv', 'r') as file:
    exit_roads = file.read().splitlines()

# Create a dictionary mapping street names to the number of cars
number_of_cars_map = {key: value for key, value in number_of_cars_data.items()}

streets = []

# First pass to create streets
for idx, street_data in enumerate(data['streets'], start=1):
    street_name = street_data['name']
    start_intersection_id = street_data['start']
    end_intersection_id = street_data['end']
    time = street_data['time']
    green_time = street_data.get('green_time', 0)  # Fetch green_time from JSON, defaulting to 0 if not present
    number_of_cars = number_of_cars_map.get(street_name, 0)  # Default to 0 if not found

    street = {
        'StreetID': idx,
        'Name': street_name,
        'StartIntersectionID': start_intersection_id,
        'EndIntersectionID': end_intersection_id,
        'Time': time,
        'NumberOfCars': number_of_cars,
        'GreenTime': green_time,
        'ExitRoad': None  # This will be set in the second pass
    }
    streets.append(street)

# Second pass to set ExitRoad
for exit_road in exit_roads:
    street_name, exit_street_name = exit_road.split(',')
    street_id = next((street['StreetID'] for street in streets if street['Name'] == street_name), None)
    exit_street_id = next((street['StreetID'] for street in streets if street['Name'] == exit_street_name), None)
    
    for street in streets:
        if street['StreetID'] == street_id:
            street['ExitRoad'] = exit_street_id

# Output the generated data for Street
print("public static List<Street> GetStreets()")
print("{")
print("    return new List<Street>")
print("    {")
for street in streets:
    print(f"        new Street {{ StreetID = {street['StreetID']}, Name = \"{street['Name']}\", StartIntersectionID = {street['StartIntersectionID']}, EndIntersectionID = {street['EndIntersectionID']}, Time = {street['Time']}, GreenTime = {street['GreenTime']}, NumberOfCars = {street['NumberOfCars']}, ExitRoad = {street['ExitRoad']} }},")
print("    };")
print("}")

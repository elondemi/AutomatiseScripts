import json
import random

# Load JSON file
with open('new_input.json', 'r') as file:
    data = json.load(file)

intersections = []

# Iterate over each street entry in the JSON data
for intersection_data in data['intersections']:
    # Extract street data
    id = intersection_data['id']
    name = intersection_data['name']
    lat = intersection_data['lat']
    lng = intersection_data['lng']
    pedestrain = intersection_data['pedestrian_phase_interval']
    allRed = intersection_data['all_red_phase_interval']


    intersection = {
            'IntersectionID': id,
            'Name': name,
            'Latitude': lat,
            'Longitude': lng,
            'PedestrainPhaseInterval': pedestrain,
            'AllRedPhaseInterval': allRed
        }
    intersections.append(intersection)

# Output the generated data for Intersection
print("public static List<Intersection> GetIntersections()")
print("{")
print("    return new List<Intersection>")
print("    {")
for idx, intersection in enumerate(intersections, start=1):
    print(f"        new Intersection {{ IntersectionID ={intersection['IntersectionID']}, Name = \"{intersection['Name']}\", Latitude = {intersection['Latitude']}, Longitude = {intersection['Longitude']}, PedestrainPhaseInterval={intersection['PedestrainPhaseInterval']}, AllRedPhaseInterval={intersection['AllRedPhaseInterval']}}},")
print("    };")
print("}")

import json

# Load JSON file
with open('input.json', 'r') as file:
    data = json.load(file)

streets = []

# Iterate over each street entry in the JSON data
for street_data in data['streets']:
    # Extract street data
    street_name = street_data['name']
    start_intersection_id = street_data['start']
    end_intersection_id = street_data['end']
    time = street_data['time']

    # Check if the street is already in the streets list
    if not any(street['Name'] == street_name for street in streets):
        street = {
            'Name': street_name,
            'StartIntersectionID': start_intersection_id,
            'EndIntersectionID': end_intersection_id,
            'Time': time
            # Add other properties as needed
        }
        streets.append(street)

# Output the generated data for Street
print("public static List<Street> GetStreets()")
print("{")
print("    return new List<Street>")
print("    {")
for idx, street in enumerate(streets, start=1):
    print(f"        new Street {{ StreetID = {idx}, Name = \"{street['Name']}\", StartIntersectionID = {street['StartIntersectionID']}, EndIntersectionID = {street['EndIntersectionID']}, Time = {street['Time']} }},")
print("    };")
print("}")

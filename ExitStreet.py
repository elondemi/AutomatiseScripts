import json

# Load JSON file
with open('input.json', 'r') as file:
    data = json.load(file)

street_exits = []
exit_id = 1
street_id_map = {}

# Generate street IDs
for idx, street_data in enumerate(data['streets'], start=1):
    street_id_map[street_data['name']] = idx

# Iterate over each street entry in the JSON data
for street_data in data['streets']:
    # Extract street ID and exit roads
    street_id = street_id_map[street_data['name']]
    exit_roads = street_data['exit_roads']

    # Iterate over each exit road
    for exit_road in exit_roads:
        # Find the street ID of the exit road
        exit_street_id = street_id_map.get(exit_road)
        if exit_street_id is not None:
            # Create a StreetExit object
            street_exit = {
                'StreetExitID': exit_id,
                'StreetID': street_id,
                'ExitStreetID': exit_street_id
            }
            street_exits.append(street_exit)
            exit_id += 1

# Output the generated data for StreetExit
print("public static List<StreetExit> GetStreetExit()")
print("{")
print("    return new List<StreetExit>")
print("    {")
for idx, street_exit in enumerate(street_exits, start=1):
    print(f"        new StreetExit {{ StreetExitID = {idx}, StreetID = {street_exit['StreetID']}, ExitStreetID = {street_exit['ExitStreetID']} }},")
print("    };")
print("}")

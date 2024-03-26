import json

# Load JSON file
with open('input.json', 'r') as file:
    data = json.load(file)

cars = data['cars']

# Generate a dictionary mapping street names to their IDs
street_id_map = {street['name']: street_id for street_id, street in enumerate(data['streets'], start=1)}

# Initialize a list to store car-street relations
car_street_relations = []

# Iterate over each car entry in the JSON data
for car_id, car_data in enumerate(cars, start=1):
    streets = car_data['path']

    # Map each street name to its corresponding street ID
    street_ids = [street_id_map[street] for street in streets]

    # Generate car-street relations
    for street_id in street_ids:
        relation = {
            'CarStreetRelationID': len(car_street_relations) + 1,
            'CarID': car_id,
            'StreetID': street_id
        }
        car_street_relations.append(relation)

# Output the generated data for CarStreetRelation
print("public static List<CarStreetRelation> GetCarStreetRelations()")
print("{")
print("    return new List<CarStreetRelation>")
print("    {")
for relation in car_street_relations:
    print(f"        new CarStreetRelation {{ CarStreetRelationID = {relation['CarStreetRelationID']}, CarID = {relation['CarID']}, StreetID = {relation['StreetID']} }},")
print("    };")
print("}")

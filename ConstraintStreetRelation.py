import json

# Load JSON file
with open('input.json', 'r') as file:
    data = json.load(file)

constraints = data['constraints']

# Generate a dictionary mapping street names to their IDs
street_id_map = {street['name']: street_id for street_id, street in enumerate(data['streets'], start=1)}

# Initialize a list to store constraint-street relations
constraint_street_relations = []

# Iterate over each constraint entry in the JSON data
for constraint_id, constraint_data in enumerate(constraints, start=1):
    streets = constraint_data['streets']

    # Map each street name to its corresponding street ID
    street_ids = [street_id_map[street] for street in streets]

    # Generate constraint-street relations
    for street_id in street_ids:
        relation = {
            'ConstraintStreetRelationID': len(constraint_street_relations) + 1,
            'ConstraintID': constraint_id,
            'StreetID': street_id
        }
        constraint_street_relations.append(relation)

# Output the generated data for ConstraintStreetRelation
print("public static List<ConstraintStreetRelation> GetConstraintStreetRelations()")
print("{")
print("    return new List<ConstraintStreetRelation>")
print("    {")
for relation in constraint_street_relations:
    print(f"        new ConstraintStreetRelation {{ ConstraintStreetRelationID = {relation['ConstraintStreetRelationID']}, ConstraintID = {relation['ConstraintID']}, StreetID = {relation['StreetID']} }},")
print("    };")
print("}")

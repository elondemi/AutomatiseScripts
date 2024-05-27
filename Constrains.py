import json

# Load JSON file
with open('input.json', 'r') as file:
    data = json.load(file)

constraints = []
constraint_id = 1

# Mapping of intersection names to IDs
intersection_id_map = {intersection['name'].replace(" ", ""): intersection['id'] for intersection in data['intersections']}

# Iterate over each constraint entry in the JSON data
for constraint_data in data['constraints']:
    # Extract constraint data
    constraint_type = constraint_data['type']
    intersection_name = constraint_data['intersection_name']

    # Get intersection ID
    intersection_id = intersection_id_map[intersection_name]

    # Check if interval exists
    interval = constraint_data.get('interval')

    # Create a new constraint
    constraint = {
        'ConstraintID': constraint_id,
        'Type': constraint_type,
        'Intersection': intersection_id,
        'Interval': interval if 'interval' in constraint_data else None  # Include interval only if it exists
    }
    constraints.append(constraint)
    constraint_id += 1

# Output the generated data for Constraint
print("public static List<Constraint> GetConstraints()")
print("{")
print("    return new List<Constraint>")
print("    {")
for constraint in constraints:
    # Include interval only if it exists
    if constraint['Interval'] is not None:
        print(f"        new Constraint {{ ConstraintID = {constraint['ConstraintID']}, Type = \"{constraint['Type']}\", Intersection = {constraint['Intersection']}, Interval = {constraint['Interval']} }},")
    else:
        print(f"        new Constraint {{ ConstraintID = {constraint['ConstraintID']}, Type = \"{constraint['Type']}\", Intersection = {constraint['Intersection']} }},")
print("    };")
print("}")

import json

def transform_json(input_file_path, output_file_path):
    # Read the input JSON file
    with open(input_file_path, 'r') as input_file:
        data = json.load(input_file)

    # Iterate through each intersection
    for intersection in data['intersections']:
        # Create a dictionary to group phases by their phase number
        phase_dict = {}
        
        # Iterate through each phase in the intersection
        for phase in intersection['phases']:
            phase_num = phase['phase']
            # Create a list in phase_dict for each phase number if it doesn't already exist
            if phase_num not in phase_dict:
                phase_dict[phase_num] = []
            # Append the street and its duration to the phase_dict
            # Remove the "phase" key from the original dictionary since it's redundant
            phase_street_duration = {key: value for key, value in phase.items() if key != 'phase'}
            phase_dict[phase_num].append(phase_street_duration)

        # Convert the phase_dict into the desired structure for each phase
        transformed_phases = []
        for phase_num, streets in phase_dict.items():
            transformed_phases.append({
                'phase': phase_num,
                'streets': streets
            })
        
        # Replace the original phases with the transformed phases
        intersection['phases'] = transformed_phases

    # Write the transformed data to the output JSON file
    with open(output_file_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)

# File paths
input_file_path = 'old_output.json'
output_file_path = 'new_output.json'

# Transform the JSON data
transform_json(input_file_path, output_file_path)

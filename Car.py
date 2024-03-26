import json

# Load JSON file
with open('input.json', 'r') as file:
    data = json.load(file)

# Generate Car data
cars = []
for i, car_data in enumerate(data['cars'], start=1):
    car_id = i
    car = {
        'CarID': car_id,
        'CarStreetRelations': []
    }
    cars.append(car)

# Output the generated data for Car
print("namespace GoogleMapAPI.Models")
print("{")
print("    public class Car")
print("    {")
print("        public int CarID { get; set; }")
print("        public ICollection<CarStreetRelation> CarStreetRelations { get; set; } = new List<CarStreetRelation>();")
print("    }")
print("}")
print("")
print("public static List<Car> GetCars()")
print("{")
print("    return new List<Car>")
print("    {")
for car in cars:
    print(f"        new Car {{ CarID = {car['CarID']} }},")
print("    };")
print("}")

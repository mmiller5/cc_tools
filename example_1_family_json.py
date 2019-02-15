#Make a family data structure

# list of parents
    # Each parent has a name
# list of kids
    # each kid has a name
    # each kid has an age

    
import json

with open("data/family.json", "r") as reader:
    family_data = json.load(reader)

print(family_data)

print("yo")
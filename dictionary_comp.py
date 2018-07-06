my_family = {
    'sister': {
        'name': 'Krista',
        'age': 42
    },
    'mother': {
        'name': 'Cathie',
        'age': 70
    }
}

family_set=set()
for member in my_family:
    family_set.add(f"My {member} {my_family[member]['name']} is {my_family[member]['age']} years old.")
    

def pick(member):
    print(f"My {member} {my_family[member]['name']} is {my_family[member]['age']}")

pick('mother')


print(family_set)
# 30.
studentList = [
    {'name': 'Alice', 'grade': 7},
    {'name': 'Bob', 'grade': 7},
    {'name': 'Carol', 'grade': 7},
    {'name': 'David', 'grade': 6},
]

# 31.
spam = [{'name': 'Alice', 'age': 3}, {'name': 'Zophie', 'age': 17}]
print(spam[1]['name'])

# 32.
print(spam[0]['age'])

# 33.
species = {'humans': ['Alice', 'Bob'], 'pets': ['Zophie', 'Pookah']}
print(species['pets'][0])

# 34.
pet_owners = {'Alice': ['Spot', 'Mittens'], 'Al': ['Zophie']}
for key, value in pet_owners.items():
    for index, item in enumerate(value):
        print(item)
        
# 35.
game = {'Home': {1:0, 2:0, 3:1, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
        'Visitor': {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}}

# 36. 
game = {'Home': {}, 'Visitor': {}}
for inning in range(1, 10):  # Loop from 1 to 9.
    game['Home'][inning] = 0
    game['Visitor'][inning] = 0
game['Home'][3] = 1  # Set one run in third inning.

# 37.
game = {'Home': {}, 'Visitor': {}}
for inning in range(1, 10000):  # Loop from 1 to 99,999.
    game['Home'][inning] = 0
    game['Visitor'][inning] = 0
game['Home'][3] = 1  # Set one run in third inning.
import json
'''
person = {"name":"Matt","age":26, "city":"Pittsburgh"}
personJSON = json.dumps(person, indent=4,sort_keys=True)
#print(personJSON)

# Dump into file
with open('person.json','w') as file:
    json.dump(person, file,indent=4)

# Decode JSON
with open('person.json','r') as file:
    person = json.loads(personJSON)
    print(person)
'''

# Custom class
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max',27)

# Encoding functin
def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name,'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')


from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o,User):
            return {'name': o.name,'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
userJSON = UserEncoder().encode(user)

user = json.loads(userJSON)
print(user)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'],age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(user.name)
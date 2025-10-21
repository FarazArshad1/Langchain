from typing import TypedDict

class Person(TypedDict):
    name : str
    age : int

new_person : Person = {
    'name' : "Hassan",
    'age' : 27
}

if __name__ == '__main__':
    print(new_person)
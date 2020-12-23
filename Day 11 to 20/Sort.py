#   List sorting in python

class Person(object) : 

    def __init__(self, name, age) : 
        self.name = name
        self.age = age

    def __str__(self) :
        return "Name = {} and age = {}".format(self.name, self.age)


if __name__ == "__main__":
    mylist = [
        Person('Ankit', 22),
        Person('Priya', 20),
        Person('Puneet', 20)
    ]

    mylist.sort(key = lambda item : item.name)

    for el in mylist : 
        print(el)
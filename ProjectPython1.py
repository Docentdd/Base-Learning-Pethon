class Person: # after the class we have enough space
    def __init__(self, name, age):
        self.name = name
        self.age = age
    job = 'Programmer' # here we have correctness of the variable assignment also it's a global variable

    def my_wife(self):
        wifeName = "Merge" # that variable is local
        print(f'my wife is {wifeName}')
        print(f'The job is {self.job}')

    def get_name(self):
        x = 'my wife name is Merge'
        print(x[16:100])
        return x[16:100]
    def get_cap_name(self):
        return self.name.capitalize()
class Main:
    person = Person('John', 20)
    Person.my_wife(person)
    x = person.get_name().upper()
    print(x)
    person = Person("diMa", 19)
    dima = person.get_cap_name()
    print(dima)





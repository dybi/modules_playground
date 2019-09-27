from my_package.a import foo, A_GLOBAL


class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age}."


def user_greets_foo():
    name = "John"
    age = A_GLOBAL
    user = User(name, age)
    print(user.greet())
    foo()


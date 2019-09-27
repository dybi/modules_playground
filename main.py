from random import randrange

from my_package.a import foo as foo_a
from random import randint
print("this is bad")
import my_module
from datetime import date
from very.nested.package import *
from my_package.b import foo as foo_b
from datetime import datetime


def main():
    my_module.user_greets_foo()
    print("-" * 10)
    foo_a()
    foo_b()

    print("-" * 10)
    print(f"I have a class from a very nested module {type(_first.First())}")
    print(f"I have a class from a very nested module {type(third.Third())}")


if __name__ == "__main__":
    # main()
    # print()
    print(f"Today is: {date.isoweekday(datetime.now())} day of the week "
          f"and your lucky number is: {randint(1, 100)}, "
          f"but beware this one: {randrange(45, 78)}")

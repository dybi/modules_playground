import my_module

from my_package.a import foo as foo_a
from my_package.b import foo as foo_b

from very.nested.package.third import Third


def main():
    my_module.user_greets_foo()
    print("-" * 10)
    foo_a()
    foo_b()

    print("-" * 10)
    print(f"I have a class from a very nested module {type(Third())}")


if __name__ == "__main__":
    main()

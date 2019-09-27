import my_module

from my_package.a import foo as foo_a
from my_package.b import foo as foo_b


def main():
    my_module.user_greets_foo()
    print("-" * 10)
    foo_a()
    foo_b()


if __name__ == "__main__":
    main()

﻿# Python Unit Testing

[![Unit Tests](https://github.com/chirbard/python-unit-testing/actions/workflows/Unit-Tests.yml/badge.svg)](https://github.com/chirbard/python-unit-testing/actions/workflows/Unit-Tests.yml)
[![Build-All-Platforms](https://github.com/chirbard/python-unit-testing/actions/workflows/Build-All-Platforms.yml/badge.svg)](https://github.com/chirbard/python-unit-testing/actions/workflows/Build-All-Platforms.yml)

A simple example of python unit testing and building executables with Github Actions.

Unit tests are run and the executables are built when changes are committed to main branch.

Awesome thing about the autobuild is that Windows defender will flag the executable as malicious.
I'm pretty sure the following code isn't malicious.
```python
def add(x, y):
    return x + y

def main():
    print(f'2 + 4 = {add(2, 4)}')
    print(f'hi + world = {add("hi", "world")}')

if __name__ == '__main__':
    main()
```

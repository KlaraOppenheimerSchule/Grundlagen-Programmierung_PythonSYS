import typing

def greeting(name: str) -> str:
    return 'Hello ' + name

print(greeting("Bianca"))

#Mit Typerror
print(greeting(23))
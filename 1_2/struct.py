from collections import namedtuple

MyStruct = namedtuple('MyStruct', 'field1 field2 field3')
m = MyStruct('foo', 'bar', 'baz')

print(m)

# python 3.7+
from dataclasses import dataclass

@dataclass
class Product:
    weight: int = None
    price: float = None

apple = Product()
apple.price = 10
from utils.helper import format_price_float_str

class Product:
    count: int = 1

    def __init__(self: object, name: str, price: float) -> None:
        self.__cod: int = Product.count
        self.__name: str = name
        self.__price: float = price
        Product.count += 1

    @property
    def cod(self: object) -> int:
        return self.__cod

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def price(self: object) -> float:
        return self.__price

    
    def __str__(self) -> str:
        return f' Code: {self.cod} \n Name: {self.name}\n Price: {format_price_float_str(self.price)}\n'

        
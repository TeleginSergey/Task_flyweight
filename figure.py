from typing import Iterable, Callable


def ensure(attr: str, functions: Iterable[Callable]) -> Callable:
    def add_property(class_: type) -> type:
        def getter(self):
            return getattr(self, f'_{attr}')

        def setter(self, value):
            for func in functions:
                func(value)
            setattr(self, f'_{attr}', value)
        setattr(class_, attr, property(getter, setter))
        return class_
    return add_property


def check_int(value: int) -> None:
    if not isinstance(value, int):
        raise TypeError(f"value {value} is expected to be int, not {type(value).__name__}")


def check_positive(value: int) -> None:
    if value < 0:
        raise ValueError(f"value {value} is expected to be positive")

class Figure:
    def perimeter(self):
        pass

    def area(self):
        pass

@ensure('radius', (check_int, check_positive))
class Circle(Figure):
    def __init__(self, radius: int):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__} radius={self.radius} perimeter={self.perimeter()} area={self.area()}'


@ensure('side_length', (check_int, check_positive))
class Square(Figure):
    def __init__(self, side_length: int):
        self.side_length = side_length

    def perimeter(self):
        return 4 * self.side_length

    def area(self):
        return self.side_length * self.side_length
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__} radius={self.side_length} perimeter={self.perimeter()} area={self.area()}'


class FigureFlyweight:
    _figures = {}

    @staticmethod
    def get_figure(figure_type, *args):
        if figure_type not in FigureFlyweight._figures:
            if figure_type == "Circle":
                FigureFlyweight._figures[figure_type] = Circle(*args)
            elif figure_type == "Square":
                FigureFlyweight._figures[figure_type] = Square(*args)
        return FigureFlyweight._figures[figure_type]

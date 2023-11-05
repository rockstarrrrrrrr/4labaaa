import math
class Circle:
    def __init__(self, radius):
        if radius<=0:
            raise ValueError("ошибка. должно быть положительное число")
        self.radius = radius
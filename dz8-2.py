#dz8-2

class Null:
    def __init__(self, div, den):
        self.div = div
        self.den = den

    @staticmethod
    def divide_by_null(div, den):
        try:
            return (div / den)
        except:
            return (f"Делить на 0 нельзя")


div = Null(5, 55)
print(Null.divide_by_null(5, 0))
print(Null.divide_by_null(5, 0.5))
print(div.divide_by_null(55, 0))
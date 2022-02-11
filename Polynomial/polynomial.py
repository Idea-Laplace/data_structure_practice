# class Polynomial without using list
class Polynomial:
    # terms[0] = degree, terms[1] = coefficient
    # If p =  Polynomial((3,4)), p.degree_3 = 4
    def __init__(self, *terms: tuple):
        self.__DEFAULT = 0    # A constant for operations
        self.__degree = 0
        for term in terms:
            if term[1]:
                self.__setattr__(f"degree_{term[0]}", term[1])
                self.__degree = term[0]

    def deg_of_pol(self):
        return self.__degree

    def __add__(self, other):
        addition = Polynomial()
        for idx in range(max(other.__degree, self.__degree) + 1):
            original = getattr(self, f"degree_{idx}", self.__DEFAULT)
            foreign = getattr(other, f"degree_{idx}", other.__DEFAULT)
            if (original or foreign) and original + foreign:
                addition.__setattr__(f"degree_{idx}", original+foreign)
                addition.__degree = idx
        return addition

    def __mul__(self, other):
        multiplication = Polynomial()
        for idx_s in range(self.__degree + 1):
            original = getattr(self, f"degree_{idx_s}", self.__DEFAULT)
            for idx_o in range(other.__degree + 1):
                foreign = getattr(other, f"degree_{idx_o}", other.__DEFAULT)
                if original and foreign:
                    multiplication = multiplication.__add__(Polynomial((idx_o + idx_s, original*foreign)))
        return multiplication

    def __repr__(self):
        expr = ''
        for idx in range(self.__degree + 1):
            value = getattr(self, f"degree_{idx}", self.__DEFAULT)
            if value:
                if idx == 1:
                    expr += f"+{value}x"
                elif idx != 0:
                    expr += f"+{value}x^{idx}"
                else:
                    expr += f"+{value}"

        return expr[1:]

if __name__ == '__main__':
    test1 = Polynomial((0, 1), (1, 2), (2, 4), (4, 8))
    test2 = Polynomial((1, 3), (2, 7), (3, 2))
    print(test1, test1.deg_of_pol())
    print(test2, test2.deg_of_pol())
    print(test1+test2, (test1+test2).deg_of_pol())
    print(test1*test2, (test1*test2).deg_of_pol())

class Rectangle:

    def __init__(self, length = 1, width = 1):
        if not isinstance(width, int):
            raise TypeError()
        elif not isinstance(length, int):
            raise TypeError()
        else:
            self.__width = width
            self.__length = length

    def __str__(self):
        return f"length = {self.__length}, width = {self.__width}"

    def set_length(self, lenght=1.0):

        if lenght > 0 and lenght < 21:
            self.__length = lenght
        else:
            raise ValueError()

    def set_width(self, width=1.0):
        if width > 0 and width < 21:
            self.__width = width
        else:
            print("Wrong variable")
            exit()

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_area(self):
        return self.get_width() * self.get_length()

    def get_perimetr(self):
        return 2 * (self.get_width() + self.get_length())


def main():
    try:
        my_rect = Rectangle()

        l = input('enter lenght: ')
        w = input('enter width: ')
        my_rect.set_length(int(l))
        my_rect.set_width(int(w))

        print('The length is', my_rect.get_length())
        print('The width is', my_rect.get_width())

        print('The area is', my_rect.get_area())
        print('The perimeter is', my_rect.get_perimetr())
        print(my_rect)

        input('press enter to continue')
    except Exception:
        print("Exeption!")
main()
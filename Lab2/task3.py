import sys
import os.path

class STUDENT:

    def __init__(self, name, surname, num_book, grades):
        if not isinstance(name, str):
            raise TypeError()
        elif not isinstance(surname, str):
            raise TypeError()
        elif not isinstance(num_book, int):
            raise TypeError()
        elif not isinstance(grades, list):
            raise TypeError()                                         
        else:
            self.__name = name
            self.__surname = surname
            self.__num_book = num_book
            self.__grades = grades
            self.__gpa = 0

    def get_info(self):
        a=len(self.__grades)
        b=sum(self.__grades)
        c=b/a
        return c

    def GPA(self):
        self.gpa = sum(self.__grades) / len(self.__grades)    

    def __str__(self):
        return f'Name = {self.__name}\nSurname = {self.__surname}\nNumber = {self.__num_book}\nGrades: {self.__grades}'                 

class GROUP:
    
    def __init__(self, *args):
            self.products = args

    def products(self, products):
        if any(not isinstance(product, STUDENT) for product in products):
            raise TypeError()
        self.__products = list(products) 

    def best_st(self):
        print(self.__products[1].__gpa)               

class main:
    #try:
        st1 = STUDENT("Vlad", "Mitl", 1, [8, 5, 6, 3])
        st1.GPA()
        st2 = STUDENT("Vlad", "Mitl", 2, [7, 5, 6, 9])
        st2.GPA()
        st3 = STUDENT("Alex", "Drain", 3, [5, 2, 7, 3])
        st3.GPA()
        st4 = STUDENT("Rita", "Brawl", 4, [8, 9, 6, 3])
        st4.GPA()
        st5 = STUDENT("Oleh", "Tiro", 5, [8, 9, 10, 10])
        st5.GPA()
        st6 = STUDENT("Max", "Drue", 6, [7, 5, 10, 2])
        st6.GPA()
        st7 = STUDENT("Mira", "Temp", 7, [5, 9, 6, 8])
        st7.GPA()
        gr = GROUP(st1, st2, st3, st4, st5, st6, st7)
        gr.products()
        gr.best_st()
    #except Exception:
        print("Exeption!")
main()       

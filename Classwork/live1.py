import math
class Rational:

    def __init__(self, numerator = 1, denumerator = 1):
        if(denumerator == 0):
            raise ZeroDivisionError()
        elif not isinstance(numerator, int):
            raise TypeError()
        elif not isinstance(denumerator, int):
            raise TypeError()   
        else: 
            self.__numenator = numerator
            self.__denumenator = denumerator 
            
    def __str__(self):
        return f"{self.__numenator}/{self.__denumenator}"

    def get_result(self):
        return self.__numenator / self.__denumenator

    def abbreviation(self):
        k = math.gcd(self.__numenator, self.__denumenator)
        self.__numenator = self.__numenator // k           
        self.__denumenator = self.__denumenator // k
        print(f'{self.__numenator}/{self.__denumenator}')

def main():
    try: 
        n = input('Enter numerator: ')
        d = input('Enter denumerator: ')
        my_rect = Rational(int(n), int(d))

        print(my_rect)
        my_rect.abbreviation()
        print("Result: ", my_rect.get_result())
        
        input('press enter to continue')
    except Exception:
        print("Exeption!")    
main()
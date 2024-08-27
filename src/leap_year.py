# Replace the "ANSWER HERE" for your answer
def is_leap_year() -> bool:
    año: int = int(input("ingrese un año: "))
    if (año % 4 == 0 and año % 100 != 0) or (año % 100 == 0 and año % 400 == 0):
        print(f"el año {año} es biciesto")
        return True
    else:
        print(f"el año {año} no es biciesto")
        return False

is_leap_year()
try:
    numerator=int(input("Enter a number:"))
    denominator=int(input("Enter a number:"))
    result=numerator/denominator
    print(result)
except ZeroDivisionError:
    print("Error : Denominator cannot be zero")
except IndexError:
    print("Error : Index out of box")
except SyntaxError:
    print("Error : Invalid Syntax")
except MemoryError:
    print("Error : Memory out of Box")
except KeyboardInterrupt:
    print("Error : Cltr keys cannot be used")


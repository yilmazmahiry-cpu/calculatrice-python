def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b

if __name__ == "__main__":
    print("Bienvenue dans la calculatrice !")
    print(f"2 + 3 = {addition(2, 3)}")
    print(f"10 - 4 = {soustraction(10, 4)}")
    print(f"3 x 5 = {multiplication(3, 5)}")
    print(f"8 / 2 = {division(8, 2)}")

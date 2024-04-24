a = input("a: ")
b = input("operand: ")
c = input("b: ")

addition = float(a) + float(c)
subtraction = float(a) + float(c)
multiplication = float(a) * float(c)
division = float(a) / float(c)
exponentiation = float(a) ** float(c)

if b == "+":
    print(str(addition))
elif b == "-":
    print(str(subtraction))
elif b == "*":
    print(str(multiplication))
elif b == "/":
    print(str(division))
elif b == "^":
    print(str(exponentiation))

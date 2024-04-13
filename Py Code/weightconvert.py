weight = input("what is your weight? ")
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    convert = float(weight) * 2.20462
    print("weight in lbs:" + str(convert))
elif unit.upper() == "L":
    convert = float(weight) * 0.453592
    print("weight in kg:" + str(convert))
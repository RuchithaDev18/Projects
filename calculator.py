def calculator(val1,val2,sign):
    if sign == "+":
        return val1 + val2
    elif sign == "-":
        return val1-val2
    else:
        return val1/val2

addition = calculator(2,7,"+")
multi = calculator(2,6,"*")

print(addition)
print(multi)

export calculator
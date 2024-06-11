def swap(var1,var2):
    """ swaps var1 and var2 using bitwise operation such that this swap occurs without taking extra space """
    var1 = var1 ^ var2
    var2 = var1 ^ var2
    var1 = var1 ^ var2
    return var1,var2

a,b = 10,20
print(f"Before swap- a,b:{a,b}")
a,b = swap(a,b)
print(f"After swap - a,b:{a,b}")
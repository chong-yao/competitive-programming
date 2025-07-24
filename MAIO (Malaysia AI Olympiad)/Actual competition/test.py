list = [-0.0293, -0.1092, -0.0290,  0.0885,  0.0623, -0.1106, -0.0229,  0.1987,
    -0.1062,  0.1949, -0.0279,  0.0705, -0.2228, -0.0478, -0.1745,  0.1071,
    -0.0549,  0.1062,  0.1074, -0.0229, -0.1208, -0.0866, -0.1071, -0.0919,
     0.1597,  0.1101,  0.0335,  0.0424, -0.1154,  0.0375,  0.0545, -0.2223,
    -0.0270, -0.0340,  0.0261,  0.1256,  0.0372, -0.0898, -0.1757,  0.1671,
    -0.1561,  0.0908,  0.0166, -0.0705, -0.0078, -0.0120, -0.0082, -0.0245,
    -0.1756, -0.0689]






# Python3 code to demonstrate working of
# Minimum element indices in list
# Using list comprehension + min() + enumerate()
 
# initializing list

 
# printing list
print("The original list : " + str(list))
 
# Minimum element indices in list
# Using list comprehension + min() + enumerate()
temp = max(list)
res = [i for i, j in enumerate(list) if j == temp]
 
# Printing result
print("The Positions of minimum element : " + str(res))
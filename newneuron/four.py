'''
Нейронка для вычисления приблизительного ответа на умножение числа на число
допустим:

4 * 5 = 20
но приблизительно это может быть, допустим, используя погрешность в 0.5, от 19.5 до 20.5
это тупо, но обучаемо
'''
import numpy as np
import random

input_numb = 2
output_numb = 3 
pogresh = 0.5


def xz(t):
    out = np.exp(t)
    return out / np.sum(out)

print(xz(3))
# def activ_fun(x):
#     if x >= 0.5:
#         return 1
#     else:
#         return 0
    
# def new_def(f, t):
#     if f > t:
#         n = 1
#     elif t >= f:
#         n = 0
#     return n

# def dsa():
#     f = float(input("1: "))
#     t = float(input("2: "))
#     if new_def(f, t) == True:
#         nums = round(f * t + random.uniform(0, pogresh), 5)
#     else:
#         nums = round(f * t - random.uniform(0, pogresh), 5)
#     return nums


    
# if __name__ == "__main__":
#     print(dsa())

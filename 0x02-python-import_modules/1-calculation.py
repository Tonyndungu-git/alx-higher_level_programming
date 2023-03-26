#!/usr/bin/python3

import calculator_1

a = 10
b = 5

sum_ab = calculator_1.add(a, b)
diff_ab = calculator_1.sub(a, b)
product_ab = calculator_1.mul(a, b)
quotient_ab = calculator_1.div(a, b)

print(f"{a} + {b} = {sum_ab}")
print(f"{a} - {b} = {diff_ab}")
print(f"{a} * {b} = {product_ab}")
print(f"{a} / {b} = {quotient_ab}")

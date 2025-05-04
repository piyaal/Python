def calculation(a, b, c):
    sum= a + b + c
    min= a - b + c
    div= (a + b) / c
    farewell = "hastala vista"

    return sum, min, div, farewell

# You can capture the returned values like this:
res1, res2, res3, msg = calculation(6, 4, 5)
print(res1)  # 6 + 4 + 5 = 15
print(res2)  # 6 - 4 + 5 = 7
print(res3)  # (6 + 4) / 5 = 2.0
print(msg)   # "hastala vista"
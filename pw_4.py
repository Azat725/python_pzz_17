two = lambda : 2
sqr = lambda x : x * x
pwr = lambda x, y : x ** y

for a in range(-2, 3):
    print(sqr(a), end="")
    print(pwr(a, two()))
    
    
divide_to_two = lambda x : x / 2


def pass_func():
    pass

def addOne(subroutine):
    return subroutine() + 1




@addOne
def add(x,y):
    return x + y

print(add(3,2))

for x in range(51):
    if(x%3==0 and x%5==0 ):
        print(x," is FIZZBUZZ")
    elif (x%5==0):
        print(x," is BUZZ")
    elif (x%3==0 ):
        print(x," is FIZZ")
    else:
        print(x)
def addthis(x, y):
    print(f"x: {x} dtype: {type(x)} \ny: {y} dtype: {type(y)}")
    
    try:
        result = x+y
    except TypeError:
        print(f"The wrong type pass in")

    return result

print(addthis(1, 2))
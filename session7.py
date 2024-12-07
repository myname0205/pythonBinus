#import logging
#
#logging.basicConfig
#def add(a, b):
#    logging.error(f"a:{a}, b: {b}")
#    return a + b
#
#print(add(5, 3))

list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = []

def CalculateMean(numbers):
    if len(numbers) == 0:
        return None
    else:
        mean = sum(numbers) / len(numbers)
        return(mean)

def TestMean():
    assert CalculateMean(list1) == 2
    assert CalculateMean(list2) == 3
    assert CalculateMean(list3) == None

TestMean()




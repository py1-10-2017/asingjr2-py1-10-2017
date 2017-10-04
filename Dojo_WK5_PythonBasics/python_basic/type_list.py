#Type List
a = ['hello', 6, ' world', 6]
b = [1,2]
c = ["moose", "dog", "cat"]

def mixer(lst):
    new_string = ''
    new_sum = 0

    for i in lst:
        if isinstance(i, int) or isinstance(i, float):
            new_sum += i
        elif isinstance(i, str):
            new_string += i

    if new_string and new_sum:
        print "The array you entered is of mixed type"
        print "String:", new_string
        print "Total:", new_sum

    elif new_string:
        print "The array you entered is of string type"
        print "String:",new_string

    else:
        print "The array you entered is of number(float or int) type"
        print "Total:", new_sum

print mixer(a)
print mixer(b)
print mixer(c)
#!/usr/bin/python3

def gen_reverse(astring):
    backwards = astring[::-1]
    normal = astring
    both = normal+backwards
    return both

txt = gen_reverse("Python")
print(txt)

def reverse(mystr):
    reversed = ""
    for char in mystr:
        reversed = char + reversed
    return reversed

def mirror(mystr):
    return mystr + reverse(mystr)

def assertEquals(a,b):
    mirror(a)
    if mirror(a) == b:
        return True
    elif mirror(a) != b:
        return False

test1 = assertEquals("good", "gooddoog")
test2 = assertEquals("Python", "PythonnohtyP")
test3 = assertEquals("", "")
test4 = assertEquals("a", "aa")
test5 = assertEquals("animal", "animal")
tests = [test1,test2,test3,test4,test5]

for test in tests:
    print(test)

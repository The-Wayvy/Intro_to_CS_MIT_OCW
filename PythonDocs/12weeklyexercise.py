def oyvey(checker, stringer):
    broken = stringer.split()
    passed = filter(checker, broken)
    return passed[0] 
    
print oyvey(lambda y: y if len(y) > 4 else None, "I am not going to tell you my secret")

print oyvey(lambda z: z if z[1] == 'r' else None, "Cats are pretty critters")

print oyvey(lambda q: q if q[len(q) - 1].upper() == q[len(q) - 1] else None, "Cats not batS")

print oyvey(lambda x: x if 'rs' in x else None, "toysrus toysrusrs")

"""
Lambda format:
lambda arg: arg boolean else None, list
This returns members of the list, called arg, which return true for the boolean.
"""

"""
in, can be used on both lists and strings
"""

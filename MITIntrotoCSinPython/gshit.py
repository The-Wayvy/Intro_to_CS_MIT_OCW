def what(fruit):
    for a in fruit:
        if a == 'z':
            return True
    else:
        return False

print what('yaz')
print what('apple')

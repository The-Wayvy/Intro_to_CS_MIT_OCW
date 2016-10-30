def four_nine(any_list):
    if len([x for x in any_list[0:4] if x == 9]) == 0:
        return False, 'the first four values do not contain 9'
    else: return True, 'at least one of the first four values is 9'

print four_nine([2, 3, 4, 5, 6])
print four_nine([9, 9, 7, 7, 6])
print four_nine([1, 1, 2, 3, 9])


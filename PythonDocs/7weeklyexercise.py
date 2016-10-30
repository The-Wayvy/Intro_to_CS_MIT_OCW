def comp_count(some_string):
    Total = 0
    already_counted = []
    for y in range(1, len(some_string) + 1):
        for x in [x for x in range(len(some_string)) if x < y]:
            if not some_string[x:y] in already_counted:
                       already_counted.append(some_string[x:y])
                       Total += 1
                       print some_string[x:y]
    else: print 'The total number of unique strings is', Total

comp_count('abbaz')
        

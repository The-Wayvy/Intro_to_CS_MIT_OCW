"""
def Pascal(n):

    triangle = []    

    for row_num in range(1, n + 1):
        new_row = row_builder(row_num)
        triangle.append(new_row)
    else: return triangle            

def row_builder(x):
    if x == 1:
        this_row = [1]
        return this_row
    else:
        refer = Pascal(x - 1)
        this_row = []
        for y in range(x):
            val = 0
            if y == 0 or y == x - 1:
                val = 1
                this_row.append(val)
            else:
                val = refer[x - 2][y] + refer[x - 2][y - 1]
                this_row.append(val)
        else:
            return this_row

def adder(n):
    summ = 0
    counter = 1
    while counter <= n:
        summ += counter
        counter += 1
    else: print summ
            

print Pascal(3)
print Pascal(6)
"""

def Pascal(n):
    whole = []
    counter = 1
    while counter <= n:
        this_row = []
        val = 0
        for num in range(0, counter):
            if num == 0 or num == (counter - 1):
                val = 1
                this_row.append(val)
            else:
                val = whole[counter - 2][num] + whole[counter - 2][num - 1]
                this_row.append(val)
        else:
            print counter, this_row
            whole.append(this_row)
            counter += 1
    else: return whole
          
Pascal(4)

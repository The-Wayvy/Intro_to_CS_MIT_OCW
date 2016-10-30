def calc_bill(bill, tip=0):
    if tip is None:
        print bill
    else:
        tip /= 100.0
        bill += bill * tip
        print bill

calc_bill(10, 20)

calc_bill(10)

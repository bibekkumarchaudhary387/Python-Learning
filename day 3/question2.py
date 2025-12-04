#price of a house is $1M
#if buyer has good credit,
    #they need to put down 10%
#otherwise
    #they need to put down 20%
#print the down payment
has_good_credit = True
if(has_good_credit==True):
    down_payment = (1000000*10)/100
else:
    down_payment = (1000000*20)/100
print(f"Down Payment: ${down_payment}")

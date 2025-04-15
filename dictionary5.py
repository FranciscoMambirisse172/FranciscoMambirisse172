def dict5():
    item_master = {'Matarchuque':400,'Bread':50 , 'Buttermilk':25}
    item_purchased = {'Matarchuque':2 , 'Bread':4}
    total_bill_amount = 0
    for item,qty in item_purchased.items():
        total_bill_amount += item_master[item]* qty
    print("total_bill_amount =", total_bill_amount)

dict5()    
   

import math

def optimal_change(item_cost, amount_paid):
    # input: cost in dollars, can have decimals
    # input: amount paid in dollars, amount to fill with change
    # output: string with variables comming from a list of optimal amount of change (using the least amount of bills-values)

    if amount_paid < item_cost:
        return False
    
    denomination_names = {
        "$100 bill":100,
        "$50 bill":50,
        "$20 bill":20,
        "$10 bill":10,
        "$5 bill":5,
        "$1 bill":1,
        "quarter":0.25,
        "dime":0.1,
        "nickel":0.05,
        "penny":0.01
    }

    denominations= list(denomination_names.keys())
    
    denom_values = list(denomination_names.values())

    # to avoid problems with floats for the minimization logic we multiply everything by 100

    values = list(map(lambda a : int(a*100),denom_values))
    
    amount = (amount_paid*100)-int(item_cost*100)
    
    change = calculator(values,amount)
    
    result_string = stringify(denominations,change,amount_paid,item_cost)
    return result_string


# to get the optimal amount we assume that the bigger the bills = the least amount of bills we need to use.
# for that divide the change amount by each bill number. we obtain the integer to know how many bills of each denomination, and the remainder to update the change to fill.

def calculator(list,num):
        res = []
        for i in list:
            d, m = divmod(num,i)
            res.append(d)
            num = m
        return res

# build a string with the variables we have in control to start the returning string and being able to concatenate the rest
# to build the rest all denominations need an "s" at the end for plural except penny, so we add acordingly to the return string.
# there is a couple edge cases that are unique enough that are solved in the logic but not in the string printing, so they print special ends to the string.

def stringify(keys, num_of_bills, amount_paid, item_cost):
    
    res = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is "

    for i,j in zip(keys,num_of_bills):

        if amount_paid == item_cost:
            res+= "0."
            break
        elif j == 0 and i == "penny":
            res = res[:-2] + "."
        elif j == 0:
            pass
        elif j == 1:
            res += f"{j} {i}, "
        elif j > 0 and i == "penny":
            res += f"and {j} pennies."
        elif j > 0:
            res += f"{j} {i}s, "
        else:
            break
    return res



'''
     Pseudocode:
     - create a key-value structure with every denomination of money.

     - since it's a minimization problem we need to divide the change left by every bill starting from the biggest, and add to a list the amount of bills of each denomination.

     - initialize a result string with all the data until the amount of bills.

     - loop through the amount of each bill and the name of each and add them to the starting string, being careful of edge cases, like exact change or underpayment.
'''    


def get_Amount_Money ():
    amount_Money_Func = int (input("How much money do you have?:"))
    return amount_Money_Func

def get_Apple_Price ():
    apple_Price_Func = int (input("How much is 1 apple?"))
    return apple_Price_Func

def get_Max_Apples (amount_Money, apple_Price):
    max_Apples_Func = amount_Money // apple_Price
    return max_Apples_Func 

def get_Change (amount_Money, apple_Price):
    get_Change_Func = amount_Money % apple_Price
    return get_Change_Func 

def displayOutput (max_Apples, change):
    print (f" You can buy {max_Apples} apples and your change is {change} pesos.")

#Steps:
#1.)Get amount of money. Store in variable.
amount_Money = get_Amount_Money()
#2.)Get price of apple. Store in variable.
apple_Price = get_Apple_Price()
#3.)Commpute maximum number of apples that can be bought. 
max_Apples = get_Max_Apples (amount_Money, apple_Price)
#4.)Compute remaining money. 
change = get_Change (amount_Money, apple_Price)
#5.)Display output. (You can buy _ apples and your change is _ pesos)
displayOutput (max_Apples, change)

def get_No_Apples():
    apples_Func = int (input("How many apples do you want to buy?:"))
    total_Apples = apples_Func*20
    return total_Apples

def get_No_Oranges():
    oranges_Func = int (input("How many oranges do you want to buy?:"))
    total_Oranges = oranges_Func*25 
    return total_Oranges

def get_Total_Fruits (apples, oranges):
    total_Fruits_Func = apples + oranges
    return total_Fruits_Func

def displayOutput (total):
    print (f"The total amount is {total}.")

#Steps;
# 1.) Ask how many apples you want to buy. Save to variable.
apples = get_No_Apples ()
# 2.) Ask how many oranges you want to buy. Save to variable.
oranges = get_No_Oranges ()
# 3.) Add total apples and oranges. Save total to variable.
total = get_Total_Fruits (apples, oranges)
# 4.) Display output (The total amount is:)
displayOutput (total)

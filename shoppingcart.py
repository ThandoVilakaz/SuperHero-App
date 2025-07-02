total = 0
prices=[]
items_list= []

def shop(items_list,prices,total):
    product = input("What product would you like to purchase? ") 
    items_list.append(product)
    price = int(input("At what price? "))
    prices.append(price)
    total +=price
    question = input("would you like to buy/add something?y/n ")
    return items_list,prices,total,question

while True:
    items_list,prices,total,question = shop(items_list,prices,total)
    if question.lower() != "y":
        break
    
print(items_list)
print(prices)
print(total)




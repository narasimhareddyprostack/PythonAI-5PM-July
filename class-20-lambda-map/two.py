prod_prices=[98,198,298,398]

def addplus(price):
    return price+1

map_obj=map(addplus,prod_prices)
new_prod_prices=list(map_obj)

print(prod_prices)
print(new_prod_prices)
import json 
fp1=open('product_data.json','r')
fp2=open('beauty.json','w')
fp3=open('groceries.json','w')
product_data=json.load(fp1)
products=product_data['products']

beauty_products=[]
groceries_products=[]

for product in products:
    if product['category'] =="beauty":
        beauty_products.append(product)
    elif product['category']=="groceries":
        groceries_products.append(product)

json.dump(beauty_products,fp2)
json.dump(groceries_products,fp3)
print("New JSON Created")

fp1.close()
fp2.close()
fp3.close()
'''
read product_data.json file and 
write all beauty products in beauty.json file
and 
write all groceries products in groceries.json file.
'''
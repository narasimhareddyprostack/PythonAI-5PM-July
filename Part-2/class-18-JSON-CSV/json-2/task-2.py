import json 
fp1=open('product_data.json','r')
fp2=open('beauty.json','w')
fp3=open('groceries.json','w')

product_data=json.load(fp1)
products=product_data['products']
print(type(products))
print(len(products))

'''
read product_data.json file and 
write all beauty products in beauty.json file
and 
write all groceries products in groceries.json file.
'''
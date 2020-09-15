# An ordered list of products and an ordered list of their prices. 
# The indexes corresponed, i.e. The price of product_list[0] = price_list[0].

product_list = ['sunglasses', 'socks', 'shoes', 'jewellery', 'bags']
price_list = [7.99, 2.99, 25.99, 15.95, 15.95]

# TASK 1: Write your code below this comment:
# Append
product_list.append('scarves')

# Insert (Any of the following are correct)
price_list.insert(5, 10.95) 
price_list.insert(-1, 10.95)
price_list.insert(len(price_list), 10.95)
print(len(price_list))
print(len(product_list))

# Remove
product_list.remove('socks')

# Del
del price_list[1]

# TASK 2: Write your code below this comment:
new_products = ['watches', 'gloves', 'hats']
new_prices = [75.99, 18.75, 20.99]
product_list += new_products
price_list.extend(new_prices)
print(len(product_list))
print(len(price_list))


#  TASK 3: Write your code below this comment:
print(product_list[2:6])


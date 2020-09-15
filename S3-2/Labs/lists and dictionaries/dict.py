# A dictionary of products and their prices as key value pairs. 

product_price = {
    'sunglasses': 7.99,
    'shoes': 25.99,
    'jewellery': 14.95,
    'bags': 15.95,
    'scarves': 10.95,
    'watches': 75.99,
    'gloves': 18.75,
    'hats': 20.99
}

# TASK 4: Write your code for below this comment: 

product_price['scarves'] = 8.99
product_price['umbrellas'] = 12.99
print(product_price)
# A dictionary of products with each product also having a dictionary as it's value.
products = {
    'sunglasses': {
        'price': 7.99,
        'colors': ['black', 'clear', 'brown', 'pink'],
        'in_stock': True
    },
    'shoes': {
        'price': 25.99,
        'colors': ['black', 'brown', 'white'],
        'in_stock': False
    },
    'jewellery': {
        'price': 14.95,
        'colors': ['gold', 'silver'],
        'in_stock': True
    },
}

# TASK 5: Write your code below this comment and below the new product dictionary: 
print(products['sunglasses']['price'])
products['shoes']['in_stock'] = True
print(products)


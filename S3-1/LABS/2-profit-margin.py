# TASK 1: Write your code below this comment:
cost = 25
profit_margin = .2
# works for .2 and .20

# TASK 2: Write your code below this comment:
# passed with or without spaces
sale_price = cost / (1 - profit_margin)
# only works if the below f-string is printed
print(f"Sale price: {sale_price}")

# TASK 3: Write your code below this comment:
# profit = 1300 * ( sale_price - cost ) did not work
profit = 1300 * (sale_price - cost)
operating_costs = 10000
profitable = profit > operating_costs
print(f"Is the company profitable? {profitable}")

# TASK 4: Write your code below this comment:
# ( sale_price - cost ) will not work
products_sold = operating_costs / (sale_price - cost)
print(f"We must sell {products_sold} units to be profitable.")

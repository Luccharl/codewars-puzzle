import re

order = 'milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza'
organized_orders = []

menu_pattern =re.compile(r'burger|fries|chicken|pizza|sandwich|onionrings|milkshake|coke')
match = menu_pattern.findall(order)

menu = ['Burger', 'Fries', 'Chicken', 'Pizza', 'Sandwich', 'Onionrings', 'Milkshake', 'Coke']

for item in match:
    item = item.capitalize()
    if item in menu:
        organized_orders.append(item)

organized_orders = sorted(organized_orders, key=menu.index)
print(organized_orders)




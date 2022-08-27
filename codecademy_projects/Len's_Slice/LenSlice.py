
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)

print("We sell", num_pizzas, "different kinds of pizza!")

pizza_and_prices = []
for x in range(num_pizzas):
    temp = [prices[x], toppings[x]]
    pizza_and_prices.append(temp)
print(pizza_and_prices)
# [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]

pizza_and_prices.sort()
# print(pizza_and_prices)
# [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [3, 'sausage'], [6, 'pineapple'], [7, 'anchovies']]
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop()

pizza_and_prices.insert(4, [2.5, "peppers"])
# print(pizza_and_prices)
# [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [2.5, 'peppers'], [3, 'sausage'], [6, 'pineapple']]

three_cheapest = pizza_and_prices[:3]
# print(three_cheapest)

print("The mice are very please and will be leaving you a 5-star review.")

# empty line
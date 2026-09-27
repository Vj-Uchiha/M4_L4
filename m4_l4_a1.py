basket1={"Mango", "Apple", "Orange", "Watermelon" }
basket2={"Mango", "Banana", "Grapes", "Apple" }
print("Basket 1:", basket1)
print("Basket 2:", basket2)

basket1.add("Grapes")
print("Basket 1 after adding Grapes:", basket1)

common_fruits = basket1.intersection(basket2)
print("Common fruits in both baskets:", common_fruits)

#Arrays
import array as arr
numbers = arr.array('i', [1, 2, 3, 4, 5])
print("Array of numbers:", numbers)

numbers.append(6)
print("Array after appending 6:", numbers)
numbers.insert(2, 10)
print("Array after inserting 10 at index 2:", numbers)

count=numbers.count(2)
print("Count of 2 in the array:", count)

numbers.reverse()
print("Array after reversing:", numbers)

print("====Fruit Basket Summary====")
print("Basket 1:", basket1)
print("Basket 2:", basket2)
print("Common fruits:", common_fruits)
print("Array of numbers:", numbers)
print("Count of 2 in the array:", count)
print("Array after reversing:", numbers)
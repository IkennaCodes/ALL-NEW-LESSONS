# Start with an empty list
x = []

#  Now create a list with different types of stuff
x = ["Adanna", 12345, "Ikenna", 78.12309, True]

#  Access items
print(x[0])   # First item: 'Adanna'
print(x[-1])  # Last item: True

#  Count how many items in the list
print(len(x))  # Output: 5

#  C - Create: Add new stuff using append()
x.append("Water Melon")
print(x)

x.append(100)
print(x)

#  R - Retrieve: Loop through each item
for i in x:
    print(i)

#  U - Update: Change item at index 5
x[5] = "Mango"  # Replaces "Water Melon" with "Mango"
print(x)

# D - Delete: Remove items in two ways

x.pop(1)        # Removes item at index 1 (12345)
print(x)

x.remove("Mango")  # Removes the item named "Mango"
print(x)

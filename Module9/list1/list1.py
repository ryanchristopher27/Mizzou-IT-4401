# Name: Ryan Christopher
# Pawprint: rdcb2f
# Challenge: List 1
# Module 9

# Functions
def display_list(label, items): # Prints the passed string and displays the items in the passed list
    print(label)
    for x in items:
        print(x)

# Main Function
foods = ["pizza", "salad", "hamburger", "steak", "apple", "orange"] # Declare foods list

display_list("foods in original order:", foods) # Display foods list

foods.sort() # Sort foods list in ascending order

display_list("foods in ascending alphabetical order:", foods) # Display foods list in ascending order

foods.sort(reverse=True) # Sort foods list in descending order

display_list("foods in descending alphabetical order:", foods) # Display foods list in descending order

foods2 = foods.copy() # Copy foods list to foods2 list
foods2.sort() # Sort foods2 list in ascending order

display_list("foods2 in ascending alphabetical order:", foods2) # Display foods2 list in ascending order

display_list("foods still in descending alphabetical order:", foods) # Display foods in descending order

foods.reverse() # Reverse foods list

display_list("foods in ascending alphabetical order:", foods) # Display foods list in ascending order

foods.append("carrots") # Append carrots to foods list
foods.append("milk") # Append milk to foods list

display_list("sorted foods with carrots and milk appended to end:", foods) # Display foods list in ascending order with appended items

foods.sort() # Sort foods list in ascending order

display_list("foods in ascending alphabetical order:", foods) # Display foods list in ascending order

pizza_index = foods.index("pizza") # Find foods list index of pizza

print("Pizza is at " + str(pizza_index)) # Print foods list index of pizza

foods.insert(pizza_index, "fries") # Insert fries into foods list at pizza index

pizza_index = foods.index("pizza") # Find foods list index of pizza

print("Pizza is now at " + str(pizza_index)) # Print foods list index of pizza
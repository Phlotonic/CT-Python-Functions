# Task 1: Write a function that lets the user add items to a list.
def add_item(shopping_list):
    """
    Function to add an item to the shopping list.
    Args:
    shopping_list (list): The current shopping list.
    """
    item = input("Enter the item to add: ")  # Prompt the user to enter an item
    shopping_list.append(item)  # Add the item to the shopping list
    print(f"{item} has been added to the list.")  # Confirm the item has been added


# Task 2: Include a function to remove items from the list.
def remove_item(shopping_list):
    """
    Function to remove an item from the shopping list.
    Args:
    shopping_list (list): The current shopping list.
    """
    item = input("Enter the item to remove: ")  # Prompt the user to enter an item to remove
    if item in shopping_list:
        shopping_list.remove(item)  # Remove the item if it exists in the list
        print(f"{item} has been removed from the list.")  # Confirm the item has been removed
    else:
        print(f"{item} is not in the list.")  # Inform the user if the item is not found


# Task 3: Add a function that prints out the entire list in a formatted way.
def print_list(shopping_list):
    """
    Function to print the entire shopping list in a formatted way.
    Args:
    shopping_list (list): The current shopping list.
    """
    print("\nShopping List:")  # Print a header for the shopping list
    for item in shopping_list:
        print(f"- {item}")  # Print each item in the list
    print()  # Add a blank line for better readability


# UPDATE: Created a main function to handle user interaction in a while loop.
def main():
    shopping_list = []  # Initialize an empty shopping list

    while True:
        # Display options to the user
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Print list")
        print("4. Exit")
        choice = input("Enter your choice: ")

        # Call the appropriate function based on user choice
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            print_list(shopping_list)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


# Entry point of the program
if __name__ == "__main__":
    main()

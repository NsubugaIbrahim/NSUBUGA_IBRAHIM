def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Inventory Management System ---")
    print("1. Add Item")
    print("2. Update Item Quantity")
    print("3. Display Inventory")
    print("4. Remove Item")
    print("5. Exit")
    print("---------------------------------")

def add_item(inventory):

    #Adds a new item to the inventory.
    
    item_name = input("Enter item name: ").strip().capitalize()
    if not item_name:
        print("Error: Item name cannot be empty.")
        return

    try:
        quantity = int(input(f"Enter quantity for {item_name}: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            return
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return

    if item_name in inventory:
        print(f"'{item_name}' already exists. Updating the old quantity '{inventory[item_name]}'.")
        inventory[item_name] += quantity
        print(f"Updated '{item_name}' quantity to {inventory[item_name]}.")
    else:
        inventory[item_name] = quantity
        print(f"Added new item '{item_name}' with quantity {quantity}.")
        

def update_item_quantity(inventory):

    # Updates the quantity of an existing item in the inventory.
    
    item_name = input("Enter the name of the item to update: ").strip().capitalize()
    if not item_name:
        print("Item name cannot be empty.")
        return

    if item_name not in inventory:
        print(f"'{item_name}' not found in inventory.")
        return

    try:
        new_quantity = int(input(f"Enter the new quantity for {item_name} (current: {inventory[item_name]}): "))
        if new_quantity < 0:
            print("Quantity cannot be negative.")
            return
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return

    inventory[item_name] = new_quantity
    print(f"Quantity of '{item_name}' updated to {new_quantity}.")

def display_inventory(inventory):

    # Displays all items and their quantities in the inventory.
    
    if not inventory:
        print("\nInventory is empty.")
        return

    print("\n--- Current Inventory ---")
    for item, quantity in inventory.items():
        print(f"- {item}: {quantity}")
    print("-------------------------")

def remove_item(inventory):
   
    # Removes an item from the inventory.
    
    item_name = input("Enter the name of the item to remove: ").strip().capitalize()
    if not item_name:
        print("Item name cannot be empty.")
        return

    if item_name in inventory:
        del inventory[item_name]
        print(f"'{item_name}' removed from inventory.")
    else:
        print(f"'{item_name}' not found in inventory.")

def main():
  
    # Main function to run the inventory management system.
 
    inventory = {} # Initialize an empty dictionary to store inventory items

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            update_item_quantity(inventory)
        elif choice == '3':
            display_inventory(inventory)
        elif choice == '4':
            remove_item(inventory)
        elif choice == '5':
            print("Exiting Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

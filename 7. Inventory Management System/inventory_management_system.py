import csv
import os

# CSV file used to store inventory data
INVENTORY_CSV = 'inventory.csv'

# Dictionary to store inventory items and quantities
inventory = {}


def load_inventory():
    """
    Load inventory data from inventory.csv.

    Reads each row from the CSV file and stores it
    in the inventory dictionary.

    Example CSV:
        apple,10
        banana,5

    Result:
        inventory = {
            "apple": 10,
            "banana": 5
        }
    """
    if os.path.exists(INVENTORY_CSV):
        with open(INVENTORY_CSV, mode='r', newline='') as file:
            reader = csv.reader(file)

            for row in reader:
                item, quantity = row
                inventory[item] = int(quantity)


def save_inventory():
    """
    Save the current inventory to inventory.csv.

    Each inventory item is written as:
        item_name,quantity

    Example:
        apple,10
        banana,5
    """
    with open(INVENTORY_CSV, mode='w', newline='') as file:
        writer = csv.writer(file)

        for item, quantity in inventory.items():
            writer.writerow([item, quantity])


def add_item(item, quantity):
    """
    Add an item to inventory.

    Args:
        item (str): Name of the item.
        quantity (int): Quantity to add.

    Example:
        add_item("apple", 5)
    """
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

    print(f"Added {quantity} {item}(s)")


def remove_item(item, quantity):
    """
    Remove quantity from an item.

    If quantity becomes zero or less,
    the item is removed completely.

    Args:
        item (str): Name of the item.
        quantity (int): Quantity to remove.
    """
    if item in inventory:
        if inventory[item] <= quantity:
            del inventory[item]
            print(f"{item} removed completely from inventory")
        else:
            inventory[item] -= quantity
            print(f"Removed {quantity} {item}(s)")
    else:
        print(f"{item} not found in inventory")


def check_item(item):
    """
    Check whether an item exists in inventory.

    Args:
        item (str): Name of the item to search.
    """
    if item in inventory:
        print(f"{item}: {inventory[item]}")
    else:
        print(f"{item} is not in inventory")


def show_inventory():
    """
    Display all inventory items and quantities.

    Example Output:
        Current Inventory
        apple: 10
        banana: 5
    """
    if not inventory:
        print("Inventory is Empty")
    else:
        print("Current Inventory")

        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")


def main():
    """
    Main program loop.

    Available Commands:
        add <qty> <item>
        remove <qty> <item>
        check <item>
        show
        quit

    Examples:
        add 10 apple
        remove 5 apple
        check apple
        show
        quit
    """
    load_inventory()

    print("Welcome to Inventory Tracker")
    print("Commands:")
    print("  add <qty> <item>")
    print("  remove <qty> <item>")
    print("  check <item>")
    print("  show")
    print("  quit")

    while True:
        command = input("> ").strip().lower()

        if command == "quit":
            save_inventory()
            print("Inventory saved. Goodbye.")
            break

        elif command == "show":
            show_inventory()

        elif command.startswith("add"):
            try:
                parts = command.split()
                qty = int(parts[1])
                item = " ".join(parts[2:])
                add_item(item, qty)

            except (ValueError, IndexError):
                print("Invalid add command. Use add <qty> <item>")

        elif command.startswith("remove"):
            try:
                parts = command.split()
                qty = int(parts[1])
                item = " ".join(parts[2:])
                remove_item(item, qty)

            except (ValueError, IndexError):
                print("Invalid remove command. Use remove <qty> <item>")

        elif command.startswith("check"):
            item = command[6:].strip()
            check_item(item)

        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
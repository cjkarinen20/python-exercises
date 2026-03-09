def display_inventory(inventory):
    
    print("Inventory:")
    sum = 0
    for item, count in inventory.items():
        print(f"{count} {item}") # Print number of each item
        sum += int(count)
    print(f"Total number of items: {sum}") # Print total number of items in inventory
    
    
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

display_inventory(inventory)
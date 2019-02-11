def display_inventory(inventory):

    print("Inventory:")
    for keys, values in inventory.items():
        print(str(keys) + ' ' + str(values))
    print("Total numbers of items: ", sum(inventory.values()))


def add_to_inventory(inventory, added_items):

    for element in added_items:
        if element in inventory:
            inventory[element] += 1
        else:
            inventory.update({element: 1})

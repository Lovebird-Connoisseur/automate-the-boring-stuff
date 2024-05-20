inventory = {'gold coin': 42, 'rope': 1}
dragonloot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayinventory(inv):
    print("Inventory:")
    total_items = 0
    for k, v in inv.items():
        print(v, k)
        total_items += v
    print(f'Total number of items: {total_items}')


def addtoinventory(inventory, addeditems):
    global inv
    for i in addeditems:
        if i not in inventory:
            inventory[i] = 1
            print(inventory)  # debug
        else:
            inventory[i] += 1
            print(inventory)  # debug
    print(inventory)  # debug


inv = addtoinventory(inventory, dragonloot)
displayinventory(inventory)

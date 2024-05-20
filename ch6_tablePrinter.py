tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(data):
    colWidths = [0] * len(data)
    number_of_lists = len(data)
    list_number = 0
    items = []
    number_of_items = len(data[0])
    while list_number != number_of_lists:
        for i in data[list_number]:
            if colWidths[list_number] < len(i):
                colWidths[list_number] = len(i)
                print(colWidths)
        list_number += 1
    for i in range(number_of_items):
        for l in range(number_of_lists):
            print(data[l][i].rjust(colWidths[l]), end=" ")
        print()


printTable(tableData)

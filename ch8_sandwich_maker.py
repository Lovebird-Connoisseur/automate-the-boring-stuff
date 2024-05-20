import pyinputplus

sandwich = {'bread': '', 'protein': '', 'cheese': '', 'other': '', 'number': ''}

sandwich['bread'] = pyinputplus.inputChoice(['wheat', 'white', 'sourdough'])
sandwich['protein'] = pyinputplus.inputChoice(['chicken', 'turkey', 'ham', 'tofu'])

want_cheese = pyinputplus.inputYesNo('Do you want cheese? ')
if want_cheese == 'yes':
    sandwich['cheese'] = pyinputplus.inputChoice(['cheddar', 'Swiss', 'mozzarella'])
else:
    pass

sandwich['other'] = pyinputplus.inputChoice(['mayo', 'mustard', 'lettuce', 'tomato'])
sandwich['number'] = pyinputplus.inputInt('Number of sandwiches? ')

print(sandwich)

if sandwich['bread'] == 'wheat':
    bread_price = 1
elif sandwich['bread'] == 'white':
    bread_price = 2
elif sandwich['bread'] == 'sourdough':
    bread_price = 5
else:
    bread_price = 0

if sandwich['protein'] == 'chicken':
    protein_price = 1
elif sandwich['protein'] == 'turkey':
    protein_price = 3
elif sandwich['protein'] == 'ham':
    protein_price = 2
elif sandwich['protein'] == 'tofu':
    protein_price = 4
else:
    protein_price = 0

if sandwich['cheese'] == 'cheddar':
    cheese_price = 1
elif sandwich['cheese'] == 'Swiss':
    cheese_price = 2
elif sandwich['cheese'] == 'mozzarella':
    cheese_price = 2
else:
    cheese_price = 0

if sandwich['other'] == 'mayo':
    other_price = 1
elif sandwich['other'] == 'mustard':
    other_price = 2
elif sandwich['other'] == 'lettuce':
    other_price = 1
elif sandwich['other'] == 'tomato':
    other_price = 1
else:
    other_price = 0

total_price = (bread_price + protein_price + cheese_price + other_price) * sandwich['number']
print(total_price)

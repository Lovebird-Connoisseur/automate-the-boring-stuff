import random, pyinputplus, time

correct_guesses = 0

for i in range(10):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    print(f'{num1} x {num2}?')
    response = num1 * num2
    try:
        pyinputplus.inputStr(allowRegexes=[f'^{response}$'],
                                            blockRegexes=[('.*'), 'Incorrect!'],
                                            limit=3, timeout=10)
    except pyinputplus.TimeoutException:
        print('Ran outta time!')
    except pyinputplus.RetryLimitException:
        print('Ran outta tries!')
    else:
        correct_guesses += 1
        print('Correct')
        time.sleep(1)

print(correct_guesses, '/ 10')

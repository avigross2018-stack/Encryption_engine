order_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
order_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9' '0']



def cesar_cipher(user_input):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9' '0']
    final_output = []
    while True: 
        user_num = input('Enter a round number: ')
        try:
            int_num = int(user_num)
            break
        except (TypeError, ValueError):
            print('You can enter only round number')
            continue

    index = 0
    while int_num > index:
        letters.append(letters[0])
        out = letters.pop(0)
        numbers.append(numbers[0])
        out = numbers.pop(0)
        index += 1
    print(letters)
    print(numbers)
    for letter in user_input:
        if letter in numbers:
            x = order_numbers.index(letter)
            final_output.append(numbers[x])
        if letter in letters:
            y = order_letters.index(letter)
            final_output.append(letters[y])
    result = "".join(final_output)
    return result

print(cesar_cipher('5b14a'))       
    
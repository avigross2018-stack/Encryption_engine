order_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
order_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9' '0']

def fence_cipher(user_input):
    
    user_list = []
    odd = []
    even = []
    for letter in user_input:
        user_list.append(letter)
    for letter in range(len(user_list)):
        if letter % 2 == 0:
            even.append(user_list[letter])
        elif letter % 2 != 0:
            odd.append(user_list[letter])
    final_output = even + odd
    return ''.join(final_output)
    
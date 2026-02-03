order_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
order_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']

def user_input_pas():
    while True:
        user_input = input().lower()
        user_list = list(user_input)
        flag = True
        for letter in user_list:
            if letter not in order_letters and letter not in order_numbers:
                flag = False
            else:
               continue
        if flag == True:
            return user_input
        else:
            print('You can enter only numbers or letters!')
               

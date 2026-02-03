import random

def random_cipher(user_input):
    list_random = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','?','@','#','$','&','%','+','-','*']
    random_pass = []
    for i in user_input:
        new = random.choice(list_random)
        random_pass.append(new)
    return ''.join(random_pass)
print(random_cipher('dnrj48dn48njf'))
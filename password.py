import re
def passcheck(s):
    if len(s) >= 6:
        if bool(re.findall('(\d+)', s)) == True:
            if s.isdigit() == False:
                if s.casefold().find("password") == -1:
                    print("хороший пароль")
                else:
                    print("пароль не должен содержать 'password'")  
            else:
                print("пароль не должен состоять только из цифр")
        else:
            print("в пароле должна быть хотя бы одна цифра")    
    else:
        print("пароль длжен состоять не менее чем из 6 символов") 

print("введите свой пароль: ")
s = input()
passwd = passcheck(s)



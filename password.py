name = input('Can I know your name, please ? ')
if len(name) < 2 :
    name = input('Please enter your real name ? ')

password = input('And your new password ?')
    
if len(password) <6 :
    password = input('Your password need at least 6 character, please inter again: ')

encode = (len(password)-3) * '*'
length = len(password)
print(f'Hey {name}, your password is {password[:3]}{encode}, has {length} characters')        

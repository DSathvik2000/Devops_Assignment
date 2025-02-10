import re

def check_password_strength(str1):
    length = len(str1)
    if(length >= 8):
        # if re.search(r'[A-Z]',str1) and re.search(r'[a-z]',str1) and re.search(r'\d',str1) and re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?/~`|-]', s):
        #     return 1
        uppercase = any(c.isupper() for c in str1)
        lowercase = any(c.islower() for c in str1)
        digit = any(c.isdigit() for c in str1)
        specialchar = any(c in "!@#$%^&*()_+{}[]:;<>,.?/~`|-" for c in str1)

        if uppercase and lowercase and digit and specialchar:
            return 1
        else:
            return 0
    else:
        str1 = "Length should be more than 8 characters"
    return str1




str1 = input()
result = check_password_strength(str1)
if result == 1 :
    print("Strong Password")
elif result == 0:
    print("The password should contain uppercase, lowercase, digit and a special character")
else:
    print(result)
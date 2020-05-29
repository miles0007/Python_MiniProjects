import re

# Complete set of reg Expressions to Check
re_num = re.compile(r'.{8,}')
re_cap = re.compile(r'[A-Z]+')
re_sm = re.compile(r'[a-z]+')
re_dig =re.compile(r'[\d]+')
re_spc = re.compile(r'[\W]+')

# combining all reg expressions
re_list = [re_num,re_cap,re_sm,re_dig,re_spc]

def strong(password):
    re_count = 0
    for pwd in re_list:
    	# check the password for a match in re_list
        if pwd.search(password) is None:
        	# if match not found
            print('Your Password is Weak. Try another One.')
            break
        else:
            re_count += 1
    # the value is 5 because we uses 5 set of reg expressions
    if re_count is 5:
        print('Your Password is Strong.')
user = input()
strong(user)
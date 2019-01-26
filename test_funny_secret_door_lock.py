"""
Coding Challenge Question 42 : Funny Secret Door Lock Test program
The Test Program will call Funny Secret Door Lock Test program and it's component to verify whether they works as intended.
NOTE: some of the funny_secret_door_lock.py functions are modified automate tests
"""


# To generate random pass-code
from random import randint

	
# Retive Pass-code from user
def get_the_user_input():
	user_passcode = user_input
	return user_passcode


# Validte user pass-code
def validate_passcode(user_passcode):
	error = False
	validated_passcode = 0
	try:
		validated_passcode = int(user_passcode)
		if validated_passcode < 0:
			my_print("Invalid passcode!! No negative numbers")
			error = True
			return validated_passcode, error
		else:
			return validated_passcode, error
	
	except ValueError:
		error = True
		my_print("Invalid passcode!! passcode should be numeric")
		return validated_passcode, error

		
# Verify the user pass-code against auto-passcode		
def check_the_passcode(user_passcode, auto_passcode):
	success = False
	if user_passcode == auto_passcode:
		my_print("WELCOME !!!\n")
		success = True
		return success, 0
	elif user_passcode > (auto_passcode + 3):
		my_print("Walk down some steps\n")
		success = False
		return success, abs(auto_passcode - user_passcode)
	elif user_passcode < (auto_passcode - 3):
		my_print("Walk up some steps\n")
		success = False
		return success, abs(auto_passcode - user_passcode)
	else:
		my_print("Hop around\n")
		success = False
		return success, abs(auto_passcode - user_passcode)

		
# Funny Secret Door Lock program starts here.
# =============================================
def funny_secret_door_lock(choice):

	count = 0
	steps_away = 0
	nearest = 0
	success = False
	
	while count < choice:
		error = True
		validated_passcode = 0
		
		while error == True:
			user_passcode = get_the_user_input()
			validated_passcode, error = validate_passcode(user_passcode)
			
		success, steps_away = check_the_passcode(validated_passcode, auto_passcode)
		
		if success == True:
			break;
			
		if count == 0:
			nearest = steps_away
		else:
			if steps_away < nearest:
				nearest = steps_away
				
		count += 1
	else:
		my_print("Sorry : You were {n} steps away".format(n=nearest))
		

		
# Tests Starts here
# =========================================
# Test variable to verify print strin
print_string = []

def my_print(string):
	global print_string
	print_string.append(string)


# Test Case 1
auto_passcode = randint(10, 40)
user_input = str(auto_passcode)
funny_secret_door_lock(1)
if print_string[0] == "WELCOME !!!\n":
	print(" Test case 1: OK")
else:
	print(" Test case 1: NOK")

	
# Test Case 2
del print_string[:]
auto_passcode = randint(10, 40)
user_input = str(auto_passcode - 1)
funny_secret_door_lock(1)
if print_string[0] == "Hop around\n":
	print(" Test case 2: OK")
else:
	print(" Test case 2: NOK")

# Test Case 3
del print_string[:]
auto_passcode = randint(10, 40)
user_input = str(auto_passcode - 3)
funny_secret_door_lock(1)
if print_string[0] == "Hop around\n":
	print(" Test case 3: OK")
else:
	print(" Test case 3: NOK")

# Test Case 4
del print_string[:]
auto_passcode = randint(10, 40)
user_input = str(auto_passcode + 1)
funny_secret_door_lock(1)
if print_string[0] == "Hop around\n":
	print(" Test case 4: OK")
else:
	print(" Test case 4: NOK")

# Test Case 5
del print_string[:]
auto_passcode = randint(10, 40)
user_input = str(auto_passcode + 3)
funny_secret_door_lock(1)
if print_string[0] == "Hop around\n":
	print(" Test case 5: OK")
else:
	print(" Test case 5: NOK")

# Test Case 6
del print_string[:]
auto_passcode = randint(10, 40)
user_input = str(auto_passcode + 4)
funny_secret_door_lock(1)
if print_string[0] == "Walk down some steps\n":
	print(" Test case 6: OK")
else:
	print(" Test case 6: NOK")

# Test Case 7
del print_string[:]
auto_passcode = randint(10, 40)
user_input = str(auto_passcode + 10)
funny_secret_door_lock(1)
if print_string[0] == "Walk down some steps\n":
	print(" Test case 7: OK")
else:
	print(" Test case 7: NOK")

# Test Case 8
del print_string[:]
auto_passcode = randint(10, 40)
user_input = str(auto_passcode - 4)
funny_secret_door_lock(1)
if print_string[0] == "Walk up some steps\n":
	print(" Test case 8: OK")
else:
	print(" Test case 8: NOK")

# Test Case 9
del print_string[:]
auto_passcode = randint(10, 40)
user_input = str(auto_passcode - 10)
funny_secret_door_lock(1)
if print_string[0] == "Walk up some steps\n":
	print(" Test case 9: OK")
else:
	print(" Test case 9: NOK")

# Test Case 10
del print_string[:]
auto_passcode = randint(10, 40)
user_input = str(auto_passcode - 10)
funny_secret_door_lock(1)
if print_string[-1] == "Sorry : You were 10 steps away":
	print(" Test case 10: OK")
else:
	print(" Test case 10: NOK")

# Test Case 11
del print_string[:]
auto_passcode = randint(10, 40)
user_input = str(auto_passcode + 10)
funny_secret_door_lock(1)
if print_string[-1] == "Sorry : You were 10 steps away":
	print(" Test case 11: OK")
else:
	print(" Test case 11: NOK")

# Test Case 12
del print_string[:]
pas_code, err = validate_passcode("sdfkj;lkdfj") # call validate_passcode() with invalid inputs
if err == True and print_string[0] == "Invalid passcode!! passcode should be numeric":
	print(" Test case 12: OK")
else:
	print(" Test case 12: NOK")


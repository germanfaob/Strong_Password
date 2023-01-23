import re

check_pass = re.compile(r'''(
^.*(?=.{10,})           # Checking the length, minimum 10
(?=.*\d)                # Numeric Digits
(?=.*[a-z])             # Lowercase, a to z.
(?=.*[A-Z])             # Uppercase, A to Z
(?=.*[@#$%^&+=!]).*$    # Special Characters
)''',re.VERBOSE)

# Strong password instruction:
# Min length: 10
# Must contain: [A-Z], [a-z], [0-9] and [Special character]

passCode = input('Enter the Password: ')
checking = check_pass.search(passCode)

# Check the password is validate or not
if checking:
    print("Strong Password.")
else:
    print("Not Valid!. Weak Password.")
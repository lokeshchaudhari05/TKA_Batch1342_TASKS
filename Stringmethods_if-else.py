# Check whether "Python" contains only alphabetic characters using isalpha().
# s = "Python"
# if s.isalpha():
#     print("Only alphabets")
# else:
#     print("Not only alphabets")



# Check whether "12345" contains only digits using isdigit().
# s = "12345"
# if s.isdigit():
#     print("Only digits")
# else:
#     print("Not only digits")



# Check whether "Python123" contains only letters and digits using isalnum().
# s = "Python123"
# if s.isalnum():
#     print("Alphanumeric")
# else:
#     print("Not alphanumeric")



# Check whether "hello" is lowercase using islower().
# s = "hello"
# if s.islower():
#     print("Lowercase")
# else:
#     print("Not lowercase")



# Check whether "HELLO" is uppercase using isupper().
# s = "HELLO"
# if s.isupper():
#     print("Uppercase")
# else:
#     print("Not uppercase")



# Check whether " " contains only whitespace using isspace().
# s = "   "
# if s.isspace():
#     print("Only whitespace")
# else:
#     print("Not only whitespace")



# Check whether "Python Programming" starts with "Python".
# s = "Python Programming"
# if s.startswith("Python"):
#     print("Starts with Python")
# else:
#     print("Does not start with Python")



# Check whether "Hello World" ends with "World".
# s = "Hello World"
# if s.endswith("World"):
#     print("Ends with World")
# else:
#     print("Does not end with World")



# Check whether "123abc" contains only digits.
# s = "123abc"
# if s.isdigit():
#     print("Only digits")
# else:
#     print("Not only digits")



# Check whether "Hello123" is alphanumeric.
# s = "Hello123"
# if s.isalnum():
#     print("Alphanumeric")
# else:
#     print("Not alphanumeric")



# If "python" is lowercase, print Valid; otherwise, print Invalid.
# s = "python"
# if s.islower():
#     print("Valid")
# else:
#     print("Invalid")



# If "WELCOME" is uppercase, print Welcome Message; otherwise, print Invalid Message.
# s = "WELCOME"
# if s.isupper():
#     print("Welcome Message")
# else:
#     print("Invalid Message")



# Check whether "Java123" is alphanumeric. Print Accepted or Rejected.
# s = "Java123"
# if s.isalnum():
#     print("Accepted")
# else:
#     print("Rejected")



# Check whether "student@gmail.com" ends with ".com".
# s = "student@gmail.com"
# if s.endswith(".com"):
#     print("Valid Domain")
# else:
#     print("Invalid Domain")



# Check whether "Python" starts with "Py" and ends with "on".
# s = "Python"
# if s.startswith("Py") and s.endswith("on"):
#     print("Both conditions satisfied")
# else:
#     print("Condition not satisfied")



# Check whether "12345" contains only digits and has exactly five characters.
# s = "12345"
# if s.isdigit() and len(s) == 5:
#     print("Valid")
# else:
#     print("Invalid")



# Check whether "Hello" contains only letters and has a length greater than three.
# s = "Hello"
# if s.isalpha() and len(s) > 3:
#     print("Accepted")
# else:
#     print("Rejected")



# Check whether "HELLO123" is uppercase using isupper().
# s = "HELLO123"
# if s.isupper():
#     print("Uppercase")
# else:
#     print("Not uppercase")



# Check whether "Python@123" is alphanumeric.
# s = "Python@123"
# if s.isalnum():
#     print("Alphanumeric")
# else:
#     print("Not alphanumeric")



# Check whether " " contains whitespace and has length greater than zero.
# s = "   "
# if s.isspace() and len(s) > 0:
#     print("Valid whitespace")
# else:
#     print("Invalid")
# Expected output: Valid whitespace



# Check whether "Python123" is alphanumeric and has length greater than five.
# s = "Python123"
# if s.isalnum() and len(s) > 5:
#     print("Valid")
# else:
#     print("Invalid")



# Check whether "HELLO" is uppercase and alphabetic.
# s = "HELLO"
# if s.isupper() and s.isalpha():
#     print("Accepted")
# else:
#     print("Rejected")



# Check whether "hello123" is lowercase and alphanumeric.
# s = "hello123"
# if s.islower() and s.isalnum():
#     print("Accepted")
# else:
#     print("Rejected")



# Check whether "12345" contains only digits OR only alphabetic characters.
# s = "12345"
# if s.isdigit() or s.isalpha():
#     print("Accepted")
# else:
#     print("Rejected")



# Check whether "Python.org" starts with "Python" and ends with ".org".
# s = "Python.org"
# if s.startswith("Python") and s.endswith(".org"):
#     print("Valid")
# else:
#     print("Invalid")



# Check whether "Hello World" starts with "Hello" OR ends with "Python".
# s = "Hello World"
# if s.startswith("Hello") or s.endswith("Python"):
#     print("Accepted")
# else:
#     print("Rejected")



# Check whether "123abc" is alphanumeric but not purely numeric.
# s = "123abc"
# if s.isalnum() and not s.isdigit():
#     print("Alphanumeric, not purely numeric")
# else:
#     print("Invalid")



# Check whether "WELCOME" is uppercase and exactly seven characters long.
# s = "WELCOME"
# if s.isupper() and len(s) == 7:
#     print("Valid")
# else:
#     print("Invalid")



# Check whether "python" is lowercase but does not start with "j".
# s = "python"
# if s.islower() and not s.startswith("j"):
#     print("Accepted")
# else:
#     print("Rejected")



# Check whether "12345" contains only digits and is not alphabetic.
# s = "12345"
# if s.isdigit() and not s.isalpha():
#     print("Numeric string")
# else:
#     print("Not a numeric string")



# A username is valid if it is alphanumeric and has between 5 and 10 characters. Validate "student123".
# s = "student123"
# if s.isalnum() and 5 <= len(s) <= 10:
#     print("Valid Username")
# else:
#     print("Invalid Username")



# A filename must start with "report" and end with ".pdf". Validate "report2026.pdf".
# s = "report2026.pdf"
# if s.startswith("report") and s.endswith(".pdf"):
#     print("Valid Filename")
# else:
#     print("Invalid Filename")



# A product code must be alphanumeric, start with "PR", and have exactly eight characters. Validate "PR12AB34".
# s = "PR12AB34"
# if s.isalnum() and s.startswith("PR") and len(s) == 8:
#     print("Valid Product Code")
# else:
#     print("Invalid Product Code")



# A password for this exercise must be at least eight characters long and alphanumeric. Validate "Python123".
# s = "Python123"
# if len(s) >= 8 and s.isalnum():
#     print("Password Accepted")
# else:
#     print("Password Rejected")



# Accept a string if it contains only alphabetic characters OR only digits. Test "Python", "12345", and "Python123".
# s = "Python"
# if s.isalpha() or s.isdigit():
#     print("Accepted")
# else:
#     print("Rejected")
# s = "12345"
# if s.isalpha() or s.isdigit():
#     print("Accepted")
# else:
#     print("Rejected")
# s = "Python123"
# if s.isalpha() or s.isdigit():
#     print("Accepted")
# else:
#     print("Rejected")
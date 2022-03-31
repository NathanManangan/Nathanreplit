import re

class Palindrome:
  def __call__(self, n):
    str(n)
    reverse_n = n[::-1]
      
    new_n = (re.sub('[^a-zA-Z0-9]', '', n)).lower()
    return new_n == new_n[::-1]

def tester():
  pal_of = Palindrome()
  str_input = str(input("Enter a string or number (only accepts alphanumeric characters): "))
  if pal_of(str_input):
    print(str_input + " is a palindrome.")
  elif pal_of(str_input) == False:
    print(str_input + " is not a palindrome.")
  else:
    print("Oh no! Something went wrong!")
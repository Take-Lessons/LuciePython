import random
import string
# Import = bring something pre built into this file
# Random & string = a built in python function

N = 8
res = ''.join(random.choices(string.ascii_letters, k=N))
print("The generated random string : " + str(res))
code = str(res)
print(code)

result01 = string.ascii_letters
result02 = string.ascii_lowercase
result03 = string.ascii_uppercase
result04 = string.digits
result05 = string.punctuation
result06 = result01 + result04 + result05

pw = 16 # How long we want our answer to be (password)
# k is please repeat and join this how ever many times k is equal too
word = ''.join(random.choices(result06, k=pw)) # randomly choosing and joining the characters
print(word)

# function
def generatePassword(passwordLength,characterChoices):
    word = ''.join(random.choices(characterChoices, k=passwordLength))
    print('the password', word)
    return word

generatePassword(16, result06)
# 16 is what we are telling passwordLength to equal and result06 is what we are telling characterChoices to be equal too
generatePassword(4, result05)
# pw is now equal to 4 and chars = result05
generatePassword(25, result04)
# library
import getpass
import string

# inputs
user_name = input('♖ Please enter your username: ') 
pass_word = getpass.getpass('♕ Please enter your password: ')
user_birth_year = input('♔ Please enter your birth year: ')

# infinity loop and condition for empty username password and birth year
while 1:
       # username
       if user_name == '':
              print('☢ Username cannot be empty. Please try again.')
              user_name = input('♖ Please enter your username: ') 
   
       # password
       if pass_word == '':
              print('☢ Password cannot be empty. Please try again.')
              pass_word = getpass.getpass('♕ Please enter your password: ')
       
       # birth year
       if not user_birth_year.isdigit():
              print('☢ Birth year cannot be empty and must be a number. Please try again.')
              user_birth_year = input('♔ Please enter your birth year: ')
       

       # finally
       if user_birth_year.isdigit() and pass_word != '' and user_name != '':
              break

# filter
score = 8
print("-"*15 + ' ☕ Filter checks ' + "-"*15)
detail_check = []
tips = []
# length more than 8 char
if len(pass_word) < 8:
       tips.append('📌 FYI just use more than 8 charachters.')
       score -= 1
       detail_check.append('☒ Password is shorter than 8 characters.')
else:
       detail_check.append('☑ Password length is sufficient.')
# including at least one English word
if any(i in string.ascii_letters for i in pass_word):
       detail_check.append('☑ Contains at least one English letter.')
else:
       tips.append('📌 Please include at least one English word.')
       score -= 1
       detail_check.append('☒ Password does not contain any English letters.')
# character at least has a one special character
if any(i in string.punctuation for i in pass_word):
       detail_check.append('☑ Contains at least one special character.')
else:
       tips.append('📌 My friend please include at least one special character.')
       score -= 1
       detail_check.append('☒ Password does not contain any special characters.')
# includes at least one Capital English letter
if any(i in string.ascii_uppercase for i in pass_word):
       detail_check.append('☑ Contains at least one uppercase letter.')
else:
       tips.append('📌 Where is at least one Capital English letter? I cannot find it, just add it into your password.')
       score -= 1
       detail_check.append('☒ Password does not contain any uppercase letters.')

# password doesnt be a same as username
if pass_word.lower() != user_name.lower():
       detail_check.append('☑ Password is not identical to the username.')
else:
       tips.append('📌 Why the password and Username are the same? Fix it.')
       score -= 1
       detail_check.append('☒ Password and username are the same.')
# password must not be the swapcase of the username
if pass_word != user_name.swapcase():
       detail_check.append('☑ Password is not the swapcase version of the username.')
else:
       tips.append('📌 It is better the password not be a swapcase of the username.')
       score -= 1
       detail_check.append('☒ Password is the swapcase version of the username.')
# password must not be a leet-speak
leet_map = {
    "a": ["@", "4"],
    "i": ["!", "1", "|"],
    "s": ["$", "5"],
    "o": ["0"],
    "e": ["3"],
    "l": ["1", "|"],
    "t": ["7"],
    "A": ["@", "4"],
    "I": ["!", "1", "|"],
    "S": ["$", "5"],
    "O": ["0"],
    "E": ["3"],
    "L": ["1", "|"],
    "T": ["7"]
}
passwd = pass_word
for i in passwd:
       for j in leet_map:
              if i in leet_map[j]:
                     passwd = passwd.replace(i,j)
if passwd.lower() != user_name.lower():
       detail_check.append('☑ Password is not a special-character version of the username.')
else:
       tips.append('📌 Just be assure about the password not be a leet-speak.It is a password not a friendly conversation with a friend.')
       score -= 1
       detail_check.append('☒ Password is a special-character version of the username.')
# password should not be a common password
with open("weakpass.txt") as f:
       weak_pass = f.read()
if pass_word not in weak_pass:
              detail_check.append('☑ Password is not one of the most common passwords.')
else:
       tips.append('📌 It is a common password mate, even my grandma can guess it, so fix it.')
       score -= 1
       detail_check.append('☒ Password is one of the most common passwords.')
# password should not be a birth year

if user_birth_year in pass_word:
       tips.append('📌 The user used the birth year in the password. Normally it is better that password to not be birth year or included with it.')
else:
       detail_check.append('☑ Password is not includes with a birth year.')

# security lever
security_level = {
    1: "Very Weak",
    2: "Weak",
    3: "Poor",
    4: "Fair",
    5: "Moderate",
    6: "Strong",
    7: "Very Strong",
    8: "Perfect",
}
for i in detail_check:
       print(i)
# result
print("-"*15 + ' ⛵ results ' + "-"*15)
print(f'🔐 Final Score: {score} out of 8')
print(f'🔒 Security Level: {security_level[int(score)]}')

match int(score):
       case 1:
              print('🎱 This password is not even a password.')
       case 2:
              print('🎱 The password is a worse password i ever seen in my whole life.')
       case 3:
              print('🎱 The password is awful.')
       case 4:
              print('🎱 could be better.')
       case 5:
              print('🎱 Hmmmm, fair.')
       case 6:
              print('🎱 Good password.')
       case 7:
              print('🎱 The password is a real deal.')
       case 8:
              print('🎉 Congratulations! Your password is highly secure and passed eight of security checks.')

print('🔑 Tips:\n'+'\n'.join(tips))
input("Press Enter to exit...")
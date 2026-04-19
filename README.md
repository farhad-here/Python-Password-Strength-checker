# 🐍 Password strength checker with python for Django
### 🖼️ Image of programe terminal
```
♖ Please enter your username:  
♕ Please enter your password: 
♔ Please enter your birth year: 
☢ Username cannot be empty. Please try again.
♖ Please enter your username: Fred
☢ Password cannot be empty. Please try again.
♕ Please enter your password: 
☢ Birth year cannot be empty and must be a number. Please try again.
♔ Please enter your birth year: 2000
--------------- ☕ Filter checks ---------------    
☒ Password is shorter than 8 characters.
☒ Password does not contain any English letters.   
☒ Password does not contain any special characters.
☒ Password does not contain any uppercase letters.
☑ Password is not identical to the username.
☑ Password is not the swapcase version of the username.
☑ Password is not a special-character version of the username.
☒ Password is one of the most common passwords.
☑ Password is not includes with a birth year.
--------------- ⛵ results ---------------
🔐 Final Score: 3 out of 8
🔒 Security Level: Poor
🎱 The password is awful.
🔑 Tips:
📌 FYI just use more than 8 charachters.
📌 Please include at least one English word.
📌 My friend please include at least one special character.
📌 Where is at least one Capital English letter? I cannot find it, just add it into your password.
📌 It is a common password mate, even my grandma can guess it, so fix it.
Press Enter to exit...
```
### 👨‍💻Libraries and language:
- python
- getpass
- string

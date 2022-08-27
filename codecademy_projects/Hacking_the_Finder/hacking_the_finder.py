#Steps 1 and 12
import csv #Step 1
import json #Step 12, always good practice to import modules at the beginning of the file

#Step 2
compromised_users=[]

#Steps 3, 4, 5, 6 and 7
with open("passwords.csv") as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    compromised_users.append(password_row["Username"])

# print(compromised_users) - This should display a list of all users

#Steps 8, 9, 10, 11
with open("compromised_users.txt", "w") as compromised_user_file:
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user)

#Steps 13, 14, 15
with open("boss_message.json", "w") as boss_message:
  boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
  json.dump(boss_message_dict, boss_message)

#Steps 16, 17, 18, 19
with open("new_passwords.csv", "w") as new_passwords_obj:
  slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  new_passwords_obj.write(slash_null_sig)
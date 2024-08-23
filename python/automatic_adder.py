#!/usr/bin/python3

import os
import hashlib

userlist = ["nibb0s"]  #select multiple
group = ["xxxx"] #only select one group
tmp = "tmp_group"

# Add users to the system and set their passwords

print("Adding users to the system")
print("###########################")
for user in userlist:
    result = hashlib.md5(user.encode()).hexdigest()
    exitcode = os.system("id {}".format(user))
    if exitcode != 0:
        print("User {} doesn't exist, adding...".format(user))
        os.system("useradd {}".format(user))
        os.system("sudo usermod -g tmp_group {}".format(user))
        # After successfully adding the user, set the password
        if os.system("id {}".format(user)) == 0:
            os.system("echo '{}:{}' | sudo chpasswd".format(user, result))
            print("Password set for user {} to the MD5 hash.:{}".format(user, result))
        else:
            print("Failed to add user {}.".format(user))
    else:
        print("User {} already exists, skipping it.".format(user))
    print("############################")
    print()

# Add users to the group
 # Correctly capture the output of the id command
    user_group = os.popen("id {} | awk -F'[=()]' '{{print $8}}'".format(user)).read().strip()

    # Check if the user is already in the group
    if user_group == tmp:
        # Use a loop to ensure correct input from the user
        while True:
            
            response = input("User wasn't added to the group. Want to add? y/n: ").lower()
            
            if response == 'y':
                os.system("usermod -aG {} {}".format(group, user))
                print("User {} added to group {}.".format(user, group))
                break
            elif response == 'n':
                print("Skipping process... adding user to non-organization group")
                os.system("usermod -aG default {}".format(user))
                break
            else:
                print("Please select 'y' or 'n'.")
        
        print("############################")
        print()
    else:
        
      
       os.system("sudo groupdel tmp")

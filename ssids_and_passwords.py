#! py
######################################
#             bhasu magic            #
######################################

import subprocess

ssids = subprocess.getoutput('netsh wlan show profiles')
ssids = ssids.split('\n')
ssids = [ a for a in ssids if "All User Profile     :" in a ]
ssids = [ b.replace('    All User Profile     : ', '') for b in ssids ]

password_list = []
file = open("passwords.txt" , "w" )

for i in range(len(ssids)):
    command = 'netsh wlan show profiles name="'+ssids[i]+'" key=clear'
    passwrd = subprocess.getoutput(command)
    passwrd = passwrd.split("\n")
    pin = [ s for s in passwrd if "Key Content            :" in s ]
    if pin:
        pin = pin[0].replace("    Key Content            : " , "")
        password_list.insert(i, pin)
    else:
        password_list.insert(i, "!! Password doesn't exist !!")
    file.write( ssids[i] + " : " + password_list[i] + "\n" )
file.close()

import subprocess
ssids = [ r.replace('All User Profile     :', '').strip() for r in list(subprocess.getoutput('netsh wlan show profiles').split('\n')) if "All User Profile" in r ]
with open("ssids_and_passwords.txt" , "w", encoding='utf-8' ) as file:
    for i in range(len(ssids)):
        pin = [ s.replace("Key Content            :" , "").strip() for s in list(subprocess.getoutput('netsh wlan show profiles name="'+ssids[i]+'" key=clear').split('\n')) if "Key Content" in s]
        if len(pin)>0:
            file.write( ssids[i] + " : " + pin[0] + "\n")
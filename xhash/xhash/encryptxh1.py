import os
import time
import json
import random
import urllib.request
from colored import fg

#Files needed to run the program.
version = json.loads(open('../src/xh1/version.json', "r").read())
xh1 = json.loads(open('../src/xh1/xh1.json', "r").read())

#Version verification and other files needed.
def ifversionok():
    os.system('clear')
    print("Verifying Software Version...")
    time.sleep(1)

    getversion = False
    while not getversion:
        try:
            global gitrawversion, gitrawxh1
            gitrawversion = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/lolenseu/xhash/main/src/xh1/version.json').read())
            gitrawxh1 = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/lolenseu/xhash/main/src/xh1/xh1.json').read())
            getversion = True
        except:
            print("Please Connect to Internet!")
            exit()

    #Checking the Software files.
    os.system('clear')
    print("Checking your Software...")
    time.sleep(2)

    if version == gitrawversion and xh1 == gitrawxh1:
        os.system('clear')
        pass
    else:
        os.system('clear')
        print("Please Update your Software!")
        exit()

#Encrypting cli animation.
def animation(spiner_counter, starttime, strap, result):
    spiner = "\\|/-"
    loadinganimation = spiner[spiner_counter]
    timeanimation = "%s sec" % (int(time.time()) - int(starttime))
    print(f"[{timeanimation}] Encrypting {loadinganimation} --> Writing [{strap}] {result}", end="\r")

#Encrypting procces.
def mainprocces():
    os.system('clear')
    global inputdata, workdata, data

    #Input file or text from the user.
    print("Type z to encrypt with file and x to encrypt with text")
    qchoice = input("Enter your choice: ").lower()

    if qchoice == 'z':
        os.system('clear')
        filedata = input("Enter your File or Directory: ").rstrip(' ')
        workdata = 'File'
        try:
            data = open(filedata, 'r').read()
        except:
            print(f"No such File or Directory: {filedata},\nMaybe {workdata} not utf-8 format.")
            time.sleep(5)
            mainprocces()

    elif qchoice == 'x':
        os.system('clear')
        textdata = input("Enter a Text: ")
        workdata = 'Text'
        data = textdata
    else:
        os.system('clear')
        print("Enter a valid choice!")
        time.sleep(2)
        mainprocces()

    #Generating new file to save the hash.
    genfilename = ''.join((random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890') for i in range(8)))
    filename = genfilename + '.xh1'
    a = open(f'encrypted-files/{filename}', 'w')
    a.write('0x')

    #Clearing the cli for encrypting procces.
    os.system('clear')
    print("Start Encrypting...")
    time.sleep(2)
    starttime = time.time()

    #Starting the encrypting procces.
    countdata = len(data)
    spiner_counter = 0
    counter = 0
    while counter < countdata:
        procces = data[counter]
        try:
            strap = xh1[procces]
            a.write(strap[2:])
            counter += 1
            result = 'ok!'
            if spiner_counter == 4:
                spiner_counter = 0
            animation(spiner_counter, starttime, strap, result)
            spiner_counter += 1
        except:
            result = 'error!'
            os.system(f'rm -rf encrypted-files/{filename}')
            animation(spiner_counter, starttime, result, result,)
            print(f"\n[{result}] Can't Write \'{procces}\'!")
            print(f"Your {workdata} not utf-8 format or \'{procces}\' are not in Dictionary.")
            print(f"Solution: Check if your {workdata} contain a non-readable characters.")
            exit()

    #Encrypting Done!
    os.system('clear')
    endtime = "[%s sec] " % (int(time.time()) - int(starttime))
    print(endtime + "Encrypting Done!")
    print("Your Encrypted file saved to: " + "encrypted-files/" + str(filename))
    exit()


#ifversionok() #Put hashtag here to cancel or bypass the version verification!, example: "#ifversionok()".
mainprocces()

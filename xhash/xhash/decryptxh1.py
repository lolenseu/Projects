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

#Decrypting cli animation.
def animation(spiner_counter, starttime, procces, result):
    spiner = "\\|/-"
    loadinganimation = spiner[spiner_counter]
    timeanimation = "%s sec" % (int(time.time()) - int(starttime))
    print(f"[{timeanimation}] Decrypting {loadinganimation} --> Reading [{procces}] {result}", end="\r")

#Decrypting procces.
def mainprocces():
    os.system('clear')
    global inputdata, workdata, data

    #Input file from the user.
    os.system('clear')
    filedata = input("Enter your File or Directory: ").rstrip(' ')

    if filedata[-4:] == '.xh1':
        workdata = 'File'
        try:
            data = open(filedata, 'r').read()
        except:
            print(f"No such File or Directory: {filedata},\nMaybe {workdata} not xh1 format.")
            time.sleep(5)
            mainprocces()

    else:
        os.system('clear')
        print("Enter a valid file!")
        time.sleep(2)
        mainprocces()

    #Checking the file.
    if data[:2] != '0x':
        os.system('clear')
        print(f"Ops! Your {workdata} are invalid or corrupted,\nMake sure it start wtih \"0x\", Example: \"0x000000000\".\nMaybe {workdata} not xh1 format.")
        exit()
    else:
        pass

    #Generating new file to save the decrypted hash.
    genfilename = ''.join((random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890') for i in range(8)))
    filename = genfilename
    a = open(f'decrypted-files/{filename}', 'w')

    #Clearing the cli for decrypting procces.
    os.system('clear')
    print("Start Decrypting...")
    time.sleep(2)
    starttime = time.time()

    #Starting the decrypting procces.
    numsdata = data[2:]
    countdata = data[2:]
    countdata = len(countdata) / 3
    spiner_counter = 0
    counter1 = 0
    counter2 = 0
    counter3 = 3
    while counter1 < countdata:
        procces = '0x' + numsdata[counter2:counter3]
        try:
            strap = xh1[procces]
            a.write(strap)
            counter1 += 1
            counter2 += 3
            counter3 += 3
            result = 'ok!'
            if spiner_counter == 4:
                spiner_counter = 0
            animation(spiner_counter, starttime, procces, result)
            spiner_counter += 1
        except:
            result = 'error!'
            os.system(f'rm -rf decrypted-files/{filename}')
            animation(spiner_counter, starttime, result, result)
            print(f"\n[{result}] Can't Read \'{procces}\'!")
            print(f"Your {workdata} are corrupted or \'{procces}\' are not in Dictionary.")
            print(f"Solution: Try to Decrypt your {workdata} to the version you encrypted.")
            exit()

    #Decrypting Done!
    os.system('clear')
    endtime = "[%s sec] " % (int(time.time()) - int(starttime))
    print(endtime + "Decrypting Done!")
    print("Your Decrypted file saved to: " + "decrypted-files/" + str(filename))
    exit()


#ifversionok() #Put hashtag here to cancel or bypass the version verification!, example: "#ifversionok()".
mainprocces()

import requests, sys, json, os, time, pyperclip

webhook = "https://discordapp.com/api/webhooks/1038464988626550896/aHmYQHLOMzofbVaHLA30iBVqsILCNMyDId-E5SFJQmMEEQwCrdoHOJiaNGRIDfSsqwf9" #WebHook URL

if(len(webhook)<5): #if webhook url exists
    print("[Line: 3] WebHook URL missing!")
    input()
    exit()

def c(text, s):         #slow print
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(s)

def cls():              #clear cross os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#cls()
if(len(sys.argv) > 1):
    path_img=sys.argv[1]
else:
    print("________________________________________________________________\n")
    print("Files are uploaded through discord [https://discord.com/tos]")
    print("DISCORD DOES NOT ENCRYPT MESSAGES ALL UPLOADED FILES ARE PUBLIC")
    print("________________________________________________________________\n")
    path_img = input("[D&D] File path: ")

if(os.path.exists(path_img) and round(os.path.getsize(path_img) / (1024 * 1024), 3) < 100): #if file exists and if file is under 100MB (discord file size upload limit)
    url = webhook+'?wait=true'  #add ?wait=true at the end of webhook url to get res form request
    with open(path_img, 'rb') as img:
        name_img=os.path.basename(path_img)
        files= {'image': (name_img,img,'multipart/form-data',{'Expires': '0'}) }
        with requests.Session() as s:
            r = s.post(url,files=files, headers={"authorization": ""})      #Upload file to discord
            #cls()
            if("200" in str(r)):                                            #If file was uploaded successfully
                url_of_file = json.loads(r.text)['attachments'][0]['url']   #Get Url from request res
                c("Successfully uploaded!\n", .05)
                print(url_of_file)
                #pyperclip.copy(url_of_file) win olny                                 #Copy URL to clipboard
            else:
                print("Error")
                print("Request res: ")
                print(r.text)
                input()
                exit()
else:
    print("Error")
    print("File Is Too Large OR doesn't exist")
    input()
    exit()

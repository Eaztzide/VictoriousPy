import pyperclip, re, os

#The aim of this code is to extract email addresses and Nigerian MOBILE phone numbers
#The extractor validates if it has come across a Nigerian number by checking the network prefix
#If it matches the ones stored in a plaintext file, it's a go-ahead.

phone9jaRegex = re.compile(r'''(
    (\+)?                           # the plus sign which is only present if there's a 234 
    (234|0)                         # the country code which can be optional if thers's a staring '0'
    (\d\d\d)                        # the network prefix         
    (\d\d\d\d\d\d\d)                # the last 6 digits
    )''', re.VERBOSE)                   

#This regex checks for any potential email address by looking for parameters like
#username, @ symbol, domain name, and domain (examples cited at line 20 (groups[4] comment))
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain-name
    (\.[a-zA-Z]{2,4})       # domain (e.g. .com, .org, .mail, .etc)
    )''', re.VERBOSE)       

text = str(pyperclip.paste())
matches = []
for groups in phone9jaRegex.findall(text):
    #What this does is to open and read the plaintext files that contains prefixes 
    #unique to specific Nigerian MOBILE Networks.
    #It then joins all the prefixes together into one list (AllPrefix).
    NetWorkPreFix1 = open('9MobilePrefix.txt')
    NetWorkPreFix2 = open('AirtelPrefix.txt')
    NetWorkPreFix3 = open('GloPrefix.txt')
    NetWorkPreFix4 = open('MTNPrefix.txt')
    AllPrefix = NetWorkPreFix1.read() + '\n' + NetWorkPreFix2.read() + '\n' + NetWorkPreFix3.read() + '\n' + NetWorkPreFix4.read()

    #If it comes across a number that starts with + (groups[1]) and 234 (groups[2]),
    #followed by a Network prefix (groups[3]) that is present in the AllPrefix list,
    #then it validates that it is a Nigerian mobile number.
    if '+' == groups[1] and '234' == groups[2] and groups[3] in AllPrefix:
        phoneNum = groups[1] + groups[2] + groups[3] + groups[4]
    #Unless if it comes across a number that starts with 0 (groups[2]) and followed by
    #a Network prefix (groups[3]) that is present in the AllPrefix list, it validates it
    #as a Nigerian number and concatenate 0 (groups[2]), the prefix (groups[3]),
    #and the rest of the number (groups[4]).
    elif '0' == groups[2] and groups[3] in AllPrefix:
        phoneNum = groups[2] + groups[3] + groups[4]
    #If a number doesn't follow any of the parameters given above,
    #it's most likely not a Nigerian mobile number.
    else:
        print('No Nigerian number found!')
        #Adds a found number to the 'matches' list
        matches.append(phoneNum)
for groups in emailRegex.findall(text):
    #Adds a found email address to the 'matches' list
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
#If no number or email address is found, notify.
else:
    print('No mobile phone numbers or email addresses found!')





import random

#Country Code
NGA = ('+234')

#A list of Nigerian network providers and their prefixes
N9Mobile = ('809', '817', '818', '908', '909')
Airtel = ('701', '704', '708', '802', '808', '812',
          '901', '902', '904', '907', '912')
Glo = ('705', '805', '807', '811', '815', '905', '915')
MTN = ('7025', '7026', '703', '704', '706', '803',
       '806', '810', '813', '814', '816', '903',
       '906', '913', '916')

#Randomly choose prefixes from providers
N9Rand = random.choice(N9Mobile)
AirRand = random.choice(Airtel)
GloRand = random.choice(Glo)
MTNRand = random.choice(MTN)

def GenReq():
    while True:
            print('Welcome to Number Generator!\n')
            print('Do you want me to generate a phone number for you?') #Asks if the user wants to generate a number.
            Ans = input('') #Collects response
            
            if Ans.startswith('Yes') or Ans.startswith('yes') or Ans.startswith('YES'): 
                print('Ok!\n')
            elif Ans.startswith('No'):
                break #Breaks if answer is no
            else:
                break
                continue
                
            print('Which Nigerian network do you want?') #Request which Nigerian network to generate
            NetReq = input('')
            
            #Randomly generate numbers strings to concatenate with
            #They are intentional divided into 7 individual numbers
            #because of zero in Python and the fact that numbers
            #from 0000000 to 0999999 wouldn't have the zeroes in 
            #front of them counted as a standalone string in Python
            #i.e 0000000 will be interpreted as 0, not as a 7 digit
            #string when generated.
            
            R1 = str(random.randint(0,9))
            R2 = str(random.randint(0,9))
            R3 = str(random.randint(0,9))
            R4 = str(random.randint(0,9))
            R5 = str(random.randint(0,9))
            R6 = str(random.randint(0,9))
            R7 = str(random.randint(0,9))
            #If the network requested matches the keywords for the variables,
            #the module concatenates the country code first with a randomly selected
            #prefix of the requested network provider, followed by 6 or 7 strings
            #that are also randomly generated.
            #It is between 6 or 7 digits because of the MTN network that has prefixes
            #with 4 digits without the starting zero. In order to generate a valid
            #Nigerian number that isn't more than 10 digits, if the randomly chosen
            #prefix is upto 4, it will be concatenated with 6 random strings. If it's
            #a 3 digit prefix, it will be concatenated with all the 7 random strings.
            if NetReq == '9mobile' or NetReq == '9Mobile' or NetReq == 'Etisalat' or NetReq == 'etisalat':
                return 'Here you go:\n' + NGA + N9Rand + R1 + R2 + R3 + R4 + R5 + R6 + R7 + '\n'
            elif NetReq == 'Airtel' or NetReq == 'airtel' or NetReq == 'zain' or NetReq == 'Zain':
                return 'Here you go:\n' + NGA + AirRand + R1 + R2 + R3 + R4 + R5 + R6 + R7 + '\n'
            elif NetReq == 'Glo' or NetReq == 'glo' or NetReq == 'GLO':
                return 'Here you go:\n' + NGA + GloRand + R1 + R2 + R3 + R4 + R5 + R6 + R7 + '\n'
            elif len(MTNRand) == 4 and NetReq == 'MTN' or len(MTNRand) == 4 and NetReq == 'mtn' or len(MTNRand) == 4 and NetReq == 'Mtn':
                return 'Here you go:\n' + NGA + MTNRand + R1 + R2 + R3 + R4 + R5 + R6 + '\n'
            elif len(MTNRand) == 3 and NetReq == 'MTN' or len(MTNRand) == 3 and NetReq == 'mtn' or len(MTNRand) == 3 and NetReq == 'Mtn':
                return 'Here you go:\n' + NGA + MTNRand + R1 + R2 + R3 + R4 + R5 + R6 + R7 + '\n'
            else:
                return 'Request a valid Nigerian provider!'
                continue
            
print(GenReq())

#Nigerian numbers prefixes

#A list of network providers and their prefixes
N9Mobile = ('809', '817', '818', '908', '909')
Airtel = ('701', '704', '708', '802', '808', '812',
          '901', '902', '904', '907', '912')
Glo = ('705', '805', '807', '811', '815', '905', '915')
MTN = ('7025', '7026', '703', '704', '706', '803',
       '806', '810', '813', '814', '816', '903',
       '906', '913', '916')
Multilinks = ('7027', '709')
Ntel = ('804')
Smile = ('7020')
Starcomms = ('7028', '7029', '819')
Zoom = ('707')
AllNigNet = (N9Mobile, Airtel, Glo, MTN, Multilinks, Ntel, Smile, Starcomms, Zoom)
try:
    while True:
            print('\nEnter your Nigerian number without the country code:')
            Number = str(int(input()))

    #A module to  make sure the number typed is = 10
            if len(Number) <= 9 or len(Number) > 10:
                print('Number must be 11 digits or 10 if without the first zero(0)!')
                continue
                
    #Checking the number network provider
            if Number.startswith(N9Mobile):
                print('\nThis is most likely a 9Mobile no.')
            elif Number.startswith(Airtel):
                print('\nThis is most likely an Airtel no.')
            elif Number.startswith(Glo):
                print('\nThis is most likely a Glo no.')
            elif Number.startswith(MTN):
                print('\nThis is most likely a MTN no.')
            elif Number.startswith(Multilinks):
                print('\nUmm... Who stil uses Multilinks?')
            elif Number.startswith(Ntel):
                print('\nThis is most likely an Ntel no.')
            elif Number.startswith(Smile):
                print('\nThis is most likely a Smile no.')
            elif Number.startswith(Starcomms):
                print('\nStarcomms? In this era?')
            elif Number.startswith(Zoom):
                print('\nZoom Mobile? Thought they\'ve left the country?')
            else:
                print('\nEnter a valid Nigerian number')
            
except ValueError:
    print('Enter numbers !') #If the character entered is not a number.
    
    


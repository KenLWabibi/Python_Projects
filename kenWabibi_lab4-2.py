# Ken Wabibi 04SEP24 Ch04_lab4-2

'''
                    Temperature Conversion
            
The purpose of this program is to ask the user to input a temperature range 
(beginning and ending temperature) and from the input temperature range the 
program will perform the following tasks:
1. First displays a table of Fahrenheit/Celsius temperatures with the 
   Fahrenheit/Celsius equivalent.
2. Second ask user if they want to calculate another temperture conversion.

'''

calc_another = 1             # variables to control the loop    

while calc_another == 1:     # validation for another temperture conversion 
    # input temperature type data
    temp=input('Input temperature type (c = celsius  f = fahrenheit): ')
    
    if temp == 'c':   # validate temp selection
        # input celsius range data
        lowRange=int(input('Enter the low range of celsius temp: '))
        highRange=int(input('Enter the high range of celsius temp: '))
        
        # data output / display table 
        print('Celsius\tFahrenheit')  
        print('___________________') 
        
        for C in range(lowRange, highRange + 1):
            F = (9 / 5) * C + 32   # fahrenheit conversion formula
            print(f'{C:.1f}\t{F:.1f}') # print results
    
    elif temp == 'f':
        # input fahrenheit range data
        lowRange=int(input('Enter the low range of Fahrenheit temp: '))
        highRange=int(input('Enter the high range of Fahrenheit temp: '))
        
        # data output / display table
        print('Celsius\tFahrenheit')   
        print('___________________') 
        
        for F in range(lowRange, highRange + 1):
            C = (F - 32) * 5/9     # celsius conversion formula
            print(f'{C:.1f}\t{F:.1f}') # print results
            
    else:
        print()
        print('INVALID ENTRY - TRY AGAIN')
        
    print()
    # input for another temperture conversion
    calc_another=int(input('Calculate another temp conversion? 1=yes 2=no: '))
    if calc_another == 2:
        print()
        print('This program has ended. I hope you found it useful.')
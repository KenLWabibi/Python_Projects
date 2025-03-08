# Ken Wabibi 27AUG24 

'''
                    Money Counting Game
            
The purpose of this program is to ask for input of the number of pennies, 
nickels, dimes, and quarters, and the objective is for the number of coins 
entered to exactly one dollar ($1.00).
The program will perform the following tasks:
1. Inform the user the value of the coins entered.
2. Offer congratulations if the value is $1.00.
3. If the coins input do not total $1.00, inform the user of the difference.
4. Program input is the number of pennies, nickles, dimes and quarters to be 
   counted (at least 1 of each coin must be input) if any coin input is 
   zero (0) stop the program.

'''

# ================ program CONSTANTS
PENNIES = .01              # constant to hold for pennie value 
NICKELS = .05              # constant to hold for nickle value 
DIMES = .10                # constant to hold for dime value 
QUARTERS = .25             # constant to hold for quarter value 
DOLLAR = 1.00              # constant to hold for dollar value 

# ================ program variables
pennies = 0                # variable to hold the input data for pennies
nickels = 0                # variable to hold the input data for nickels
dimes = 0                  # variable to hold the input data for dimes 
quarters = 0               # variable to hold the input data for quarters
ttl_Pennies = 0            # variable to hold the total value for pennies
ttl_Nickels = 0            # variable to hold the total value for nickels
ttl_Dimes = 0              # variable to hold the total value for dimes
ttl_Quarters = 0           # variable to hold the total value for quarters
ttl_Coins = 0.0            # variable to hold the total value for all coins
difference = 0.0           # variable that informs the user of the difference 

# ================ input data
pennies=int(input('Enter the number of pennies or enter 0 to exit: '))
nickels=int(input('Enter the number of nickel or enter 0 to exit: '))
dimes=int(input('Enter the number of dimes or enter 0 to exit: '))
quarters=int(input('Enter the number of quarters or enter 0 to exit: '))

# ================ determine if coins entered a zero to exit program
if pennies == 0 or nickels == 0 or dimes == 0 or quarters == 0:
   print('A 0 was entered for one or more coin values, program has ended.')
else:   
# ================ processing / caculations
   ttl_Pennies = pennies * PENNIES
   ttl_Nickels = nickels * NICKELS
   ttl_Dimes = dimes * DIMES
   ttl_Quarters = quarters * QUARTERS
   ttl_Coins = ttl_Pennies + ttl_Nickels + ttl_Dimes + ttl_Quarters
   difference = DOLLAR - ttl_Coins

# ================ determine if coins equal $1.00 / data output / print results
   if ttl_Coins == DOLLAR:
      print(f'Total value of pennies {ttl_Pennies:.2f}.')
      print(f'Total value of nickels {ttl_Nickels:.2f}.')
      print(f'Total value of dimes {ttl_Dimes:.2f}.')
      print(f'Total value of quarters {ttl_Quarters:.2f}.')
      print('Congratulations, the total coins entered equal $1.00.')
   else:
      print(f'Total value of pennies {ttl_Pennies:.2f}.')
      print(f'Total value of nickels {ttl_Nickels:.2f}.')
      print(f'Total value of dimes {ttl_Dimes:.2f}.')
      print(f'Total value of quarters {ttl_Quarters:.2f}.')      
      print('Sorry, the total coins enterd do not equal $1.00.') 
      print(f'You were off by {difference:.2f}.')

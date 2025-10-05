# Write a program that simulates a simple ATM machine.
#The program should:
#Start with a fixed account balance (e.g. 1000).
#Show a of options:
#Check Balance
#Deposit Money
#Withdraw Money
#Exit
#Ask the user to choose an option (with input).
#Perform the action:
#If balance check → print the balance.
#If deposit → ask how much, add to balance, and show new balance.
#If withdraw → ask how much, subtract if enough money, otherwise show error.
#If exit → stop the program.
#Keep showing the menu until the user chooses Exit.
balance = 1000
counter =0
while True:
 print('your balance is 1000')
 print('1- check balance')
 print('2- deposite money')
 print('3- withdraw money')
 print('4- exit')
 option = int(input('choose a nb (1,2,3,4):'))
 counter = counter + 1

 if option ==2 :
   deposite = int(input('enter the amount you want to depsoite is:'))
   new_balance = balance + deposite
   print ('deposite is successful the new balance for you is:',new_balance)

 elif option == 3:
   withdraw = int(input('enter the amount you want to withdraw is:'))
   if withdraw < balance :
     new_balance = balance - withdraw
     print ('withdraw is successful the new balance for you is:',new_balance)
   else:
    print('insufficient funds')

 elif option == 4:
   print('goodbye')
   break

 else:
   print('you have checked your balance')

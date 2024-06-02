#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Developing a banking program
# Functin to deposit an amount
def deposit(balance):
    amount = float(input('Enter amount to deposit:  '))
    
    if amount < 0:
        print('**********************************')
        print('That is not a valid amount')
        print('**********************************')
        return 0
    else:
        return amount
    
    # Function to show your account balance
def show_balance(balance):
    
    print(f'Your Account balance is $ {balance:.2f}')
    print('**********************************')
    
    #Function to withdraw an amount
def withdraw(balance):
    amount = float(input('Enter amount to be withdraw" '))
    if amount > balance:
        print('**********************************')
        print('Insuficient Funds')
        print('**********************************')
        return 
    elif amount < 0:
        print('**********************************')
        print('Amount must be greater than 0')
        print('**********************************')
    else:
        return amount
    
# Defining the main function for the program    
def main():
    
    is_running = True
    balance = 0

    while is_running:
        print('**********************************')
        print('Banking program')
        print('**********************************')
        print('1.Check Balance')
        print('2.Deposit Amount')
        print('3.Withdraw ')
        print('4.Exit')
        print('**********************************')

        choice = input('Enter your choice from 1-4 ')

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit(balance)
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print('**********************************')
            print('Wrong choice,choose from 1-4')
            print('**********************************')
    print('**********************************')
    print('Thank you have a nice day') 
    print('**********************************')
if __name__=='main':
    main()


# In[ ]:


main()


# In[ ]:





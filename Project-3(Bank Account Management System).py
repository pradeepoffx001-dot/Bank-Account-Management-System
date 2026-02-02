accounts=[]
def create_account():
    acc_no=input('Account number: ')
    name=input('Name: ')
    acc_balance=int(input('Acc Balance: '))
    account={'acc_no':acc_no,
             'name':name,
             'acc_balance':acc_balance}
    accounts.append(account)
    print('✅ Account created successfully')
def view_accounts():
    if not accounts:
        print('❌ No accounts found')
    else:
        print('\n--- Account List ---')
        for a in accounts:
            print('Acc no: ',a['acc_no'],
                  'Name: ',a['name'],
                  'Acc Balance: ',a['acc_balance'])
def search_account():
    acc_no=input('Enter Account Number to search: ')
    for a in accounts:
        if a['acc_no']==acc_no:
            print('✅ Account found')
            print('Acc no: ',a['acc_no'])
            print('Name: ',a['name'])
            print('Acc Balance: ',a['acc_balance'])
            return
    print('❌ Account not found')
def add_amount():
    acc_no=input('Account number: ')
    amount=int(input('Enter the Amount to deposit: '))
    for a in accounts:
        if a['acc_no']==acc_no:
            a['acc_balance']+=amount
            print('✅ Amount deposited')
            print('Current Balance: ',a['acc_balance'])
            return
    print('❌ Account not found')
def withdraw_amount():
    acc_no=input('Account number: ')
    amount=int(input('Enter the Amount to withdraw: '))
    for a in accounts:
        if a['acc_no']==acc_no:
            if a['acc_balance']>=amount:
                a['acc_balance']-=amount
                print('✅ Withdrawal successful')
                print('Current Balance: ',a['acc_balance'])
            else:
                print('⚠ Insufficient balance')
                return
    print('❌ Account not found')
def delete_account():
    acc_no=input('Account number: ')
    for a in accounts:
        if a['acc_no']==acc_no:
            accounts.remove(a)
            print('✅ Account deleted')
            return
    print('❌ Account not found')
while True:
     print('\n--- Bank Management System ---')
     print('1.Create Account')
     print('2.View Accounts')
     print('3.Search Account')
     print('4.Add Amount')
     print('5.Withdraw Amount')
     print('6.Delete Account')
     print('7.Exit')
     choice=input('Enter Your Choice: ')
     if choice=='1':
         create_account()
     elif choice=='2':
         view_accounts()
     elif choice=='3':
         search_account()
     elif choice=='4':
         add_amount()
     elif choice=='5':
         withdraw_amount()
     elif choice=='6':
         delete_account()
     elif choice=='7':
         print('👋 Program closed')
         break
     else:
         print('❌ Invalid choice')

                

           
               
           
           
           


    
  
    
    
    
            
        

        


         
  
    

    

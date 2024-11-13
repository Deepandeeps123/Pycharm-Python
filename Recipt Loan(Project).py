Amount = int(input('Enter the amount:'))
if Amount>0:
 print('Choose the option from below:\n','1.Personal Loan\n','2.Crop Loan\n','3.House Loan\n','4.Car loan')

 option = int(input('Enter the option:'))
 if option == 1:
   interest = Amount * 11//100
   total = Amount + interest
   print('=' * 30)
   print(f'Amount = {Amount}')
   print(f'Interest = {interest}')
   print(f'Total = {total}')
   print('='*30)
 elif option == 2:
   interest = Amount * 3//100
   total = Amount + interest
   print('='*30)
   print(f'Amount = {Amount}')
   print(f'Interest = {interest}')
   print(f'Total = {total}')
   print('='*30)
 elif option == 3:
    interest = Amount * 15//100
    total = Amount + interest
    print('='*30)
    print(f'Amount = {Amount}')
    print(f'Interest = {interest}')
    print(f'Total = {total}')
    print('='*30)
 elif option == 4:
    interest = Amount * 20//100
    total = Amount + interest
    print('='*30)
    print(f'Amount = {Amount}')
    print(f'Interest = {interest}')
    print(f'Total = {total}')
    print('='*30)
 else:
    print('Invalid Option')
else:
    print('Not accept negative amount')
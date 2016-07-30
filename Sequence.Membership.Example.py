# check a user name and PIN code

database = [['albert', '1234'],
            ['dilbert','4242'],
            ['smith',  '7524'],
            ['jones',  '9843']]

username = input('User name: ')
pin = input('PIN code:  ')

if [username, pin] in database: print ('Access granted')

# Needs an  els statement to return for anouther attempt or maybe Start with
# Els loop


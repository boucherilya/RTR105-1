Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> if x < 10:
	print('Smaller')
	if x > 20:
		print('Bigger')
		print('Finis')

		
Smaller
>>> x = 5
>>> if x == 5 :
	print ('Equals 5')
	if x > 4 :
		print('Greater than 4')
		if x >= 5 :
			print('Greater than equals 5')
			if x < 6 : print('Less than 6')
			if x <= 5 :
				print('Less than or equals 5')
				if x != 6 :
					print('Not equal 6')

					
Equals 5
Greater than 4
Greater than equals 5
Less than 6
Less than or equals 5
Not equal 6
>>> x = 5
>>> print('Before 5')
Before 5
>>> if x == 5 :
	print('ls 5')
	print('is Still 5')
	print('Third 5')
	print('Afterwards 5')
	print('Before 6')
	if x == 6 :
		print('Is 6')
		print('Is Still 6')
		print('Third 6')
		print('Afterwards 6')

		
ls 5
is Still 5
Third 5
Afterwards 5
Before 6
>>> x = 5
>>> if x > 2 :
	print('Bigger than 2')
	print('Still bigger')
	print('done with 2')

	
Bigger than 2
Still bigger
done with 2
>>> for i in range(5) :
	print(i)
	if i > 2 :
		print('Bigger than 2')
		print('Done with i', i')
		      
SyntaxError: EOL while scanning string literal
>>> for i in range(5) :
	print(i)
	if i > 2 :
		print('Bigger than 2')
		print('Done with i, i')
		print('All done')

		
0
1
2
3
Bigger than 2
Done with i, i
All done
4
Bigger than 2
Done with i, i
All done
>>> x = 5
>>> if x > 2 :
	print('Bigger than 2')
	print('Stil bigger')
	print('Dne with 2')

	
Bigger than 2
Stil bigger
Dne with 2
>>> for i in range(5) :
	print(i)
	if i > 2 :
		print('bigger than 2')
		print('Done with i, i')
		print('All done')

		
0
1
2
3
bigger than 2
Done with i, i
All done
4
bigger than 2
Done with i, i
All done
>>> x = 42
>>> if x > 1 :
	print('More than one')
	if x < 100 :
		print('Less than 100')
		print('All done')

		
More than one
Less than 100
All done
>>> x = 4
>>> if x > 2 :
	print('Bigger')
	else :
		
SyntaxError: invalid syntax
>>> x = 4
>>> if x > 2 :
	print('Bigger')
	
>>> x = 4
>>> if x > 2 :
	print('Bigger')
	
>>> 
>>> x = 4
>>> if x > 2 :
	print('Bigger')
	else :
		
SyntaxError: invalid syntax
>>> x = 4
>>> if x > 2 :
	print('Bigger')
	ekse : print('Smaller')
	
SyntaxError: invalid syntax
>>> x = 4
>>> if x > 2 :
	print('Bigger')
	else : print('Smaller')
	
SyntaxError: invalid syntax
>>> x = 4 
if x > 2 :
	print('Bigger')
	else:
		
>>> x = 4
if x > 2 :
	print('Bigger')
	else :
		
>>> x = 4
>>> if x > 2 :
	print('Bigger')
else :
	
>>> x = 4
>>> if x > 2 :
	print('Bigger')
else :
	
>>> x = 4
>>> if x > 2 :
	print('Bigger')
else:
	
>>> 
================= RESTART: /home/user/RTR105-1/if_test_1.py =================
Bigger
All done
>>> 
================= RESTART: /home/user/RTR105-1/if_test_1.py =================
Bigger
All done
>>> 
================= RESTART: /home/user/RTR105-1/if_test_1.py =================
Bigger
All done
>>> 
================= RESTART: /home/user/RTR105-1/if_test_1.py =================
Bigger
All done
Bigger
All done
>>> 
================= RESTART: /home/user/RTR105-1/if_test_1.py =================
Bigger
All done
Bigger
All done
Medium
All done
>>> 
================= RESTART: /home/user/RTR105-1/if_test_1.py =================
Bigger
All done
Bigger
All done
Medium
All done
small
All done
>>> 
================= RESTART: /home/user/RTR105-1/if_test_1.py =================
Bigger
All done
Smaller
All done
small
All done
Medium
All done
LARGE
All done
>>> 
================= RESTART: /home/user/RTR105-1/if_test_1.py =================
Bigger
All done
Smaller
All done
small
All done
Medium
All done
LARGE
All done
Medium
All done
>>> 

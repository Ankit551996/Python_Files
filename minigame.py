import random
n=23
guessed=int(n*random.random())+1
print("if you want to close the game enter 101\n")
guess_no=int(input("Enter a new no.:->"))
while guess_no != guessed:
	if guess_no==101:
		break;
	if guess_no < 0:
		print("no. is too low\n")
		guess_no=int(input("enter new no.:->"))
	elif guess_no < guessed:
		print("no is littel bit near\n")
		guess_no=int(input("enter new no.:->"))
	elif guess_no > guessed:
		print("no is high\n")
		guess_no=int(input("enter new no.:->"))
	elif guess_no > 100:
		print("no. is too high\n")
		guess_no=int(input("enter new no.:->"))

if guess_no == guessed:
	print("!**Congress you win the game")
if guess_no == 101:
	print("So Sorry Try Again \n")
	print("no> is --->")
	print(guessed)

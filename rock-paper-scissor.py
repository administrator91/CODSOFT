import random
from colorama import init, Fore
l = ["rock", "scissor", "paper"]
init()
print(Fore.GREEN+"*" * 76)
print(Fore.YELLOW+f"\t  Heyy Buddy!! This is a Simple Rock-Paper-Scissor Game ")
print(Fore.YELLOW+f"\tMade By {Fore.RED}_R{Fore.YELLOW}a{Fore.GREEN}j{Fore.BLUE}a{Fore.MAGENTA}r{Fore.RED}s{Fore.YELLOW}h{Fore.GREEN}i_{Fore.YELLOW}With help of Python Programming Language")
print(Fore.GREEN+"*" * 76)
print(Fore.RESET)

red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW
reset = Fore.RESET

while True:
    ccount = 0
    ucount = 0

    uc = int(input('''
Game Start--
1 Yes
2 No|Exit
          '''))

    if uc == 1:
        for a in range(1, 6):
            userinput = int(input('''
______________________________________
Enter the number of your choice (1-3):
*************************************|
            1. Rock                  |
            2. Scissor               |
            3. Paper                 |
*************************************|
        '''))

            if userinput == 1:
                uchoice = "rock"
            elif userinput == 2:
                uchoice = "scissor"
            elif userinput == 3:
                uchoice = "paper"
            else:
                print(f"{red}Invalid Input")
                print(f"Please Enter a Valid Input..{reset}")
                continue  

            cchoice = random.choice(l)
            print("User choice:", uchoice)
            print("Computer choice:", cchoice)

            if cchoice == uchoice:
                print("Game Draw..\n")
                ucount += 1
                ccount += 1
            elif (uchoice == "rock" and cchoice == "scissor") or (uchoice == "paper" and cchoice == "rock") or (
                    uchoice == "scissor" and cchoice == "paper"):
                print("You Win..\n")
                ucount += 1
            else:
                print("Computer Wins...\n")
                ccount += 1

        if ucount == ccount:
            print(f"_____________{yellow}FINAL RESULT{reset}_____________")
            print(f"{red}Finally Game Draw...{reset}")
        elif ucount > ccount:
            print(f"_____________{yellow}FINAL RESULT{reset}_____________")
            print(f"{green}Finally You Win...{reset}")
        else:
            print(f"_____________{yellow}FINAL RESULT{reset}_____________")
            print(f"{blue}Finally Computer Wins...{reset}")

        print("User Score:", ucount)
        print("Computer Score:", ccount)
        print("______________________________________")

    elif uc == 2:
        print(f"{green}Game Exit..{reset}")
        break
    else:
        print(f"{red}Sorry You Choose Wrong Option..")
        print(f"Please Try Again..{reset}")
       

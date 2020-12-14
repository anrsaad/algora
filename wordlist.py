
import os, sys, pyfiglet, datetime
from termcolor import colored
from sys import platform


random_file = str(datetime.datetime.now().microsecond)

if platform == "win32" :

    os.chdir("C:\\Users\\Public\\Desktop")
    md = os.getcwd()
    mdfile = md +"\\wordlist"+random_file+".txt"
elif platform == "linux" or platform == "linux2" :
    os.chdir("/root/Desktop")
    md = os.getcwd()
    mdfile = md +"/wordlist"+random_file+".txt"
else:
    print(colored("sorry this program not working in your operation system", "red", attrs=["bold"]))

mini= colored("\nEnter the Minimum Number : ", "blue", attrs=["dark"])
maxi= colored("\nEnter the Maximum Number : ", "blue", attrs=["dark"])
saut = "\n"
space_line = " "

print(pyfiglet.figlet_format("Algora"),space_line *10, "Numberliste generator")

warn = colored("[!]", "yellow") 
print(saut * 2)
print(f"{warn} You must enter two number to start generate a numberliste : \n")

user_1 = input(mini)
user_2 = input(maxi)


if user_1.isdigit() and user_2.isdigit():

    if user_1 < user_2 :
        wordlist1 = int(user_1)
        wordlist = int(user_2)
        result = wordlist - wordlist1
        string = colored(str(result), "red")
        line1 = colored("==", "cyan")
        bar = colored("|", "cyan")
        msg1 =colored("         wordlist build successfully          ", "green", attrs=["bold"])
        msg2 =colored("keys generated on worldlist       ", "green", attrs=["bold"])
        space =" "*11
        jump = "\n"
        if platform == "win32" :
            os.system("cls")
        elif platform == "linux" or platform =="linux2" :
            os.system("clear")
        print(jump * 3)
        print("+", line1 * 36,"+", "\n|")
        print(bar,space, msg1, space, bar)
        print(bar,space, "     [", string, "]", msg2, space, bar)
        print(bar)
        print("+", line1 * 36, "+")
        print(jump *10)
        file=open(mdfile, "a")

        while True :
            wordlist1 += 1
            if wordlist1 == wordlist :
                break
            wordlist2 = wordlist1 + 1
            x = str(wordlist2)
            
            y = (x + "\n")
            file.write(y)
        file.close()

    elif  user_1 == user_2 :
        
        print(colored("\nthe maximum and minimum number shouldn't be egale\n", "red"))

    elif user_1 > user_2 :
        msg_erreur1 =colored("\n /!\\  WRONG ENTER : ", "red")
        print(msg_erreur1, user_1, ">", user_2, "      --must be the opposite-- ")
else :
    line2 = colored("__", "red")
    bar2 = colored("|", "red")
    msg_erreur2 = colored("You Must Enter A Numbers", "blue")
    space2 =" "
    
    print(" ",line2 *35)
    print(bar2, "")
    print(bar2, space2*25, msg_erreur2, space2*19, bar2)
    print(bar2, line2 *35, bar2)

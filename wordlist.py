
import os, sys, pyfiglet, datetime
from termcolor import colored
from sys import platform
from time import sleep


anim=""
def animation(ascii):
    print(colored("""\n              | ￣￣￣￣￣￣￣￣￣￣￣￣|
              |      SAHRA MAGHRIBIYA   |
              |＿＿＿＿＿＿＿＿＿＿＿＿ |
                    \  (^_^) /
                      \    /
                        ——
                       |  |
                       |_ |_ """, "yellow"))


random_file = str(datetime.datetime.now().microsecond)
if platform == "win32" :
    animation(anim)
    sleep(1.0)
    os.system("cls")
    os.chdir("C:\\Users\\Public\\Desktop")
    md = os.getcwd()
    mdfile = md +"\\wordlist"+random_file+".txt"
elif platform == "linux" or platform == "linux2" :
    animation(anim)
    sleep(1.5)
    os.system("clear")
    os.chdir("/root/Desktop")
    md = os.getcwd()
    mdfile = md +"\\wordlist"+random_file+".txt"
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

line2 = colored("__", "red")
bar2 = colored("|", "red")
space2 =" "

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
        sign = colored("~~~", "yellow")
        colormsg = colored("You find you file on desktop","cyan")
        colormsg1 = colored("Every file genrated took the same name + a random number","cyan")
        colormsg2 = colored("Program developed by : Anrsaad","cyan")
        print(space, sign, colormsg, "\n", space, sign, colormsg1, "\n",space, sign, colormsg2, "\n")
        print(jump *10)
        file=open(mdfile, "a")

        while True :
            wordlist1 += 1
            if wordlist1 == wordlist :
                break
            wordlist2 = wordlist1 -1
            wordlist3  = wordlist1 +1
            x = str(wordlist2)
            z = str(wordlist3)
            zprime = (z + "\n")
            y = (x + "\n")
            file.write(y)
        file.write(z)   
            
        file.close()

    elif  user_1 == user_2 :
        space3 = " "
        notice_msg =colored("NOTICE :", "red")
        print(f"\n\n\n{notice_msg}\n", line2*36, "\n")
        msg3=colored("the maximum and minimum number shouldn't be egale", "yellow")
        print(bar2, space3*10, msg3, space3*9, bar2)
        print(bar2, line2*35, bar2, "\n\n")

    elif user_1 > user_2 :
        space4 = " "
        notice_msg =colored("NOTICE :", "red")
        print(f"\n\n\n{notice_msg}\n", line2*36, "\n")
        
        panneau = colored("/!\\", "red")
        msg_erreur1 =colored("WRONG ENTER  ", "yellow")
        msg_erreur2 = colored("    --must be the opposite-- ", "yellow")
        print(bar2, space4*22, panneau,space4*2,msg_erreur1, space4*26, bar2)
        print(bar2, space4*19, user_2, ">", user_1, msg_erreur2, space4*12, bar2 )
        print(bar2, line2*35, bar2, "\n\n\n\n")


else :

    msg_erreur2 = colored("You Must Enter A Numbers not a characters", "yellow")
    panneau2 = colored("/!\\", "red")
    print("\n\n\n\n")
    print(colored("NOTICE : ", "red"))
    print(line2 *36)
    print(bar2, "")
    print(bar2, space2*15, panneau2, msg_erreur2, space2*8, bar2)
    print(bar2, line2 *35, bar2, "\n\n\n")

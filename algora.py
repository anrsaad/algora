#worldlist : python file
#write by Saad Anouar
#Work on windows and Linux (operation system)
#use for create a file.txt in Desktop with numbers list between to value given by user 
#useful for bruteforce cracking
#Needed :
#      - import termcolor module on operation system by write (pip install termcolor) or on linux
#        by writing (sudo apt-get install python-termcolor)
#      - if you have problem with Pip config please check network for answer by writing (instal pip on windows)
#      - import also pyfiglet module (this module for animation texte in intro of program) 

import os, sys, pyfiglet, datetime
from termcolor import colored
from sys import platform
from time import sleep

#import all module needded to use him on program 
#created definition to call him with sleep function() to show and gone after 1.5second
def animation():
    print(colored("""\n\n\n\n
      ======================================================================= 
      =                          _    _                                     =
      =                         / \  | | __ _  ___  _ __ __ _               =
      =                        / _ \ | |/ _` |/ _ \| '__/ _` |              =
      =                       / ___ \| | (_| | (_) | | | (_| |              =
      =                      /_/   \_\_|\__, |\___/|_|  \__,_|              =
      =                                 |___/                               =
      =                                         Numberliste generator.      =
      =                                                                     =
      =======================================================================
                             """, "yellow"))



# random_file : i use it to created random file on Desktop beacause i dont want import a random module 
# i do thid method of random just for fun, and i call a microsecond function() in datetime module to take the numbers
# of microsecond time from system to user him in name of file.

random_file = str(datetime.datetime.now().microsecond)
# i am using here the platform function () from sys module to check the operation system
# and use command prompt to erase the screen and show animation intro (animation) also create after a random file.txt
# if the user work on different OS (operation system), i use the else statement to show a message and gone
if platform == "win32" :
    os.system("cls")
    animation()
    sleep(1.5)
    os.system("cls")
    os.chdir("C:\\Users\\Public\\Desktop")
    md = os.getcwd()
    mdfile = md +"\\wordlist"+random_file+".txt"
elif platform == "linux" or platform == "linux2" :
    os.system("clear")
    animation()
    sleep(1.5)
    os.system("clear")
    os.chdir("/root/Desktop")
    md = os.getcwd()
    mdfile = md +"\\wordlist"+random_file+".txt"      # creat this variable for use it to write the file
else:
    print(colored("sorry this program not working in your operation system", "red", attrs=["bold"]))

# beacause you i cant use colored function from termcolor module, i create two variable with colored message to call him on input function()


mini= colored("\nEnter the Minimum Number : ", "blue", attrs=["dark"])
maxi= colored("\nEnter the Maximum Number : ", "blue", attrs=["dark"])
saut = "\n"
space_line = " "
print("\n\n")
print(pyfiglet.figlet_format("                      Algora"),space_line *36, "Numberliste generator.")

warn = colored("[!]", "yellow")
link = colored("https://github.com/anrsaad/algora", "yellow")
tube = colored("https://www.youtube.com/c/TechnoTech3301", "yellow")
print("")
print(link)
print(tube)
print(saut * 2)
print(f"{warn} You must enter two number to start generate a numberliste : \n")

# i create two variable and call colored message to use him on input function()
user_1 = input(mini)
user_2 = input(maxi)

line2 = colored("__", "red")
bar2 = colored("|", "red")
space2 =" "

# i am using if statement to check if user enter a integer or string input
# if user enter a integer the program continue if not jum to else statement and show message
if user_1.isdigit() and user_2.isdigit():
    # check if everything is normal and the user enter a integer and the second integer bigger than the first
    
    if user_1 < user_2 :
        wordlist1 = int(user_1)
        wordlist = int(user_2)
        result = wordlist - wordlist1  # here i create the variable to show how much line are wrinting
        string = colored(str(result), "red")  #and here i colored the result before use it in print
        line1 = colored("==", "cyan")
        bar = colored("|", "cyan")
        msg1 =colored("         wordlist build successfully          ", "green", attrs=["bold"])
        msg2 =colored("keys generated on worldlist       ", "green", attrs=["bold"])
        space =" "*11
        jump = "\n"
        #i use if statement here to check operation system again and erase the screen before show the succeful message
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
        colormsg2 = colored("Program developed by Saad Anouar","cyan")
        print(space, sign, colormsg, "\n", space, sign, colormsg1, "\n",space, sign, colormsg2, "\n")
        print(jump *10)
        file=open(mdfile, "a")     # create a variable to assign it to file.txt
        # loop with adding everytime +1 and keep calculate to arrive at number enter by user_2 and write this on file 
        # but before because the return resultat come in one line, i creat a variable to convert integer to string and use a (\n) to jump to the next line
         
        while True :
            wordlist1 += 1
            if wordlist1 == wordlist :
                break
            # because the accounting start from vraiable giver +1 i create a new acounting from variable given bu user -1

            wordlist2 = wordlist1 -1
            # whene the caculated finish he not arrived to egale variable giver by user, so i create second variable and adding +1 to complete the write
            wordlist3  = wordlist1 +1
            x = str(wordlist2)
            z = str(wordlist3)
            zprime = (z + "\n")
            y = (x + "\n")
            file.write(y)
        file.write(z)   
        # closing the file after the two variable be egale    
        file.close()
    # elif statement to check if user enter a egal degital variable, and show message  
    elif  user_1 == user_2 :
        space3 = " "
        notice_msg =colored("NOTICE :", "red")
        print(f"\n\n\n{notice_msg}\n", line2*36, "\n")
        msg3=colored("the maximum and minimum number shouldn't be egale", "yellow")
        print(bar2, space3*10, msg3, space3*9, bar2)
        print(bar2, line2*35, bar2, "\n\n")
    #check if user enter the first variable (variable whene program start caculating) bigger the second variable (variable the end of calculating)
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

# using else statement if the user not enter a integer and enter maybe a characters or not enter anything
else :

    msg_erreur2 = colored("You Must Enter A Numbers not a characters", "yellow")
    panneau2 = colored("/!\\", "red")
    print("\n\n\n\n")
    print(colored("NOTICE : ", "red"))
    print(line2 *36)
    print(bar2, "")
    print(bar2, space2*15, panneau2, msg_erreur2, space2*8, bar2)
    print(bar2, line2 *35, bar2, "\n\n\n")

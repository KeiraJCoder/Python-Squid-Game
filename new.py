import random

def game_three_start():

        shapes =[
            "Square",
            "Circle",
            "Star",
            "Spiral"
        ]
        
        shapes1 = random.choice(shapes)
        chance = 0
        
        
        print("It is time to make a choice, before you stands four doors.\n")
        print("Each door is emblazoned with a number\n")
       
        choice2 = int(input("Which door do you choose? 1, 2, 3 or 4? \n\n"))
        
        if chance <= 2:
            chance += 1
            if choice2 == 1:
                print("You have chosen the First door\n")
                print(f"Your shape will be {shapes1}\n")
                print("Good luck")
                
            elif choice2 == 2:
                print("You have chosen the Second door\n")
                print(f"Your shape will be {shapes1}\n")
                print("Good luck")
                
            elif choice2 == 3:
                print("You have chosen the Third door\n")
                print(f"Your shape will be {shapes1}\n")
                print("Good luck")
                
            elif choice2 == 4:
                print("You have chosen the Fourth door\n")
                print(f"Your shape will be {shapes1}\n")
                print("Good luck")
            else:
                print("Do not test me\n\n")
                game_three_start()
        elif chance >= 2:
            print("I told you not to test me\n\n")
            
game_three_start()





# import time

# GREEN   = '\033[32m'
# BLUE    = '\033[34m'
# BOLD    = '\033[1m'
# RESET_ALL = '\033[0m' 
# YELLOW  = '\033[33m'
# RED     = '\033[31m'
# UNDERLINE = '\033[4m'
# RED_bg     = '\033[41m'
# GREEN_bg   = '\033[42m'
# CYAN_bg    = '\033[46m'
# YELLOW_bg  = '\033[43m'
# BLACK_bg   = '\033[30m'
# BLACK   = '\033[30m'
# UNDERLINE = '\033[4m'
# BLUE_bg    = '\033[44m'

# attempts=0   #represent first level first challenge attemps total 4 if more than 4 game over
# attmps=0     #represents first level second challenge first letter attempts total 4 if more than 4 game over
# attmpsb=0    #represents first level second challenge second letter attempts total 4 if more than 4 game over
# attmpsc=0  
# attmpsd=0    


# #######################################################################################################

# def game():
#     def intro():
#         print("""     
#             ======================================================================================================       
#               The year is 2122 and global warming has taken effect.\n
#               Penguins have evolved and taken over the world.\n 
#               You are an astronaut and you just returned back to earth from a failed mission to seek a better world\n
#               Your spacecraft has crash landed on an unoccupied beach somewhere.\n 
#               You leave the space craft and familiarise yourself with the surroundings. \n
#               Suddenly friendly humans who've been brain-washed by penguins appear in the distance.\n
#             =========================================================================================================""")
        
#         print(f"""

#             ,88888b.                                  ,888888b.                   
#             .d888888888b                               .d888888888b                  
#         _..-'.`*'_,88888b                          _..-'.`*'_,88888b                 
#     ,'..-..`"ad88888888b.                      ,'..-..`"ad88888888b.               
#             ``-. `*Y888888b.                           ``-. `*Y888888b.             
#                 \   `Y888888b.                             \   `Y888888b.           
#                 :     Y8888888b.                           :     Y8888888b.         
#                 :      Y88888888b.                         :      Y88888888b.       
#                 |    _,8ad88888888.                        |    _,8ad88888888.      
#                 : .d88888888888888b.                       : .d88888888888888b.     
#                 \d888888888888888888                       \d888888888888888888     
#                 8888;'''`88888888888                       8888;ss'`88888888888     
#                 888'     Y8888888888                       888'N""N Y8888888888     
#                 `Y8      :8888888888                       `Y8 N  " :8888888888     
#                 |`      '8888888888                        |` N    '8888888888     
#                 |        8888888888                        |  N     8888888888     
#                 |        8888888888                        |  N     8888888888     
#                 |        8888888888                        |  N     8888888888     
#                 |       ,888888888P                        |  N    ,888888888P     
#                 :       ;888888888'                        :  N    ;888888888'     
#                 \      d88888888'                         :  N    ;888888888'     
#                 _.>,    888888P'                            \ N    d88888888'      
#                 <,--''`.._>8888(                             _.>N    888888P'        
#                 `>__...--' `''` SSt                       <,--'N`.._>8888(          
#                     _                                       `>__N..--' `''` SSt                     
#                                                                                                      """)
#         penguin_game()
#     ######################################################################################################
    
#     def penguin_game():
#         #   global getpass 
#         #   global pin
#         #   global first_challenge
#         #   global p
        
#         global number
#         global attmps
#         attmps=0
#         global attmpsb
#         attmpsb=0
#         global attmpsc
#         attmpsc=0
#         global attmpsd
#         attmpsd=0
#         global Name
#         global attempts
#         attempts=0
#         global t
#         global time
#         GAME_START=input("Press y to Enter into the Game:\n")
#         if GAME_START=="y"or GAME_START=="Y":
#             print(f"{RESET_ALL}{YELLOW}{GREEN}                       Welcome to Rise Of The Killer Penguins Game {RESET_ALL}\n\n\n\n")
#             enter_name()
#         #   elif GAME_EXIT=="N"or GAME_EXIT=="n":
#         #       print(f"")
#         else:
#             print(f"{RED}You Enter the Wrong Entry\n{RESET_ALL}")
#             intro()
#             penguin_game()
#     ######################################################################################################

#     def enter_name():
#         global Name
#         global GAME_START
#         global first_challenge
#         global number
#         Name=(input(f"Enter your Name to Continue: "))
#         print(f"{BLUE}Welcome {Name} {RESET_ALL}")
#         print(f"""
#                     _.._                   
#                 .-'    `-.                
#                 :          ;               
#                 ; ,_    _, ;               
#                 : \"  "/ :               
#                 ,'.'"=..=''.'.              
#             ; / \      / \ ;             
#             .' ;   '.__.'   ; '.           
#         .-' .'              '. '-.        
#         .'   ;                  ;   '.      
#     /    /                    \    \     
#     ;    ;                      ;    ;    
#     ;   `-._                  _.-'   ;    
#     ;      ""--.        .--""      ;     
#         '.    _    ;      ;    _    .'      
#         ""..' '._.-.    .-._.' '..""     
#         \           ;  ;           /       
#         :         :    :         :        
#         :         :.__.:         :        
#         \       /"-..-"\       /      
#             '-.__.'        '.__.-'               
#     {RESET_ALL} """)
                                                    

    
#         first_level_entry=input("Press y to let the game begins:\n")
#         if(first_level_entry=="y" or first_level_entry=="Y"):
#                 print(f"{YELLOW}{RED_bg}You have been captured by the Killer Penguins and sent to prison. You have just woken up in your cell with a banging migraine\n and everything looks blurry a because you were drugged.You must have to find the pin code and code letter to escape from prison. {RESET_ALL}")
#                 print("You are entering in to the first Level")
#                 first_level()
#         #    elif(GAME_EXIT=="N" or GAME_EXIT=="n"):
#         #          penguin_game()
                
#         else:
#                 print(f"{RED}You Enter the Wrong Entry\n{RESET_ALL}")
#                 intro()
#                 penguin_game()
#     #######################################################################################################
#     def first_level():
        
#         global password
#         global pwd
#         global Name
#         global GAME_START
#         global attempts
        
#         #   global time
#         #   global t
#         #   game_timer()
#         first_challenge=(input("Enter the four digit pin to open the first lock:\n"))
#         if (first_challenge)=="1234":
#             print("You passed your first Challenge")
#             print("Your Second Challenge is to get the password")
#             first_level_second_challengea()
#         #   elif():
#         #         first_challenge==string()
#         #         print("sdfdsgfd")
#         #         first_level()

#         else:
#             print("You put the wrong pin try again")
#             attempts=attempts+1
#             if(attempts>=4):
#                 print(f"{RED}You put to many wrong entries GAME OVER{RESET_ALL}")
#                 penguin_game()
#             else:
#                 first_level()      

#     #######################################################################################################

#     def first_level_second_challengea():
            
#             global GAME_START
#             global attmps
#             global attmpsb
#             password=["a","b","c","d"]
#             global pwd1,pwd2,pwd3
#             pwd=(input("Enter your first letter of code: "))
#             if (pwd==password[0]):
#                 print(password[0])
#                 first_level_second_challengeb()
                
#             else:
#                 print("Wrong Entry TRY AGAIN")
#                 attmps=attmps+1
#                 if(attmps>=4):
#                     print(f"{RED}You Put To many wrong entries GAME OVER{RESET_ALL}")
#                     penguin_game()
#                 else:
#                     first_level_second_challengea()

                
#     def first_level_second_challengeb():
#                 global attmpsb
#                 global attmpsc
#                 global attmps
#                 global number
#                 global Name
                
#                 global GAME_START
#                 password=["a","b","c","d"]
#                 global pwd2,pwd3
#                 pwd1=input("Enter your second letter of code you guess the first correctly: ")
#                 if pwd1==password[1]:
#                     print(f"you guesses two word perfectly")
#                     print(password[0])
#                     print(password[1])
#                     first_level_second_challengec()
#                 else:
#                     print("Wrong Entry TRY AGAIN")
#                     attmpsb=attmpsb+1
#                     if(attmpsb>=4):
#                         print(f"{RED}You Put To many wrong entries GAME OVER{RESET_ALL}")
#                         penguin_game()
#                     else:
#                         first_level_second_challengeb()
                        
                        
#     def first_level_second_challengec():
#                     global attmps
                    
#                     global attmpsc
#                     global number
#                     global Name
#                     global GAME_START
#                     password=["a","b","c","d"]
#                     global pwd3,pwd2,pwd1
#                     pwd2=input("enter your third letter you guess the first and second letter correctly: ")
#                     if pwd2==password[2]:
#                         print(f"YOU GUESSES THE three letters perfectly enter your fourth letter")
#                         print(password[0])
#                         print(password[1])
#                         print(password[2])
#                         first_level_second_challenged()
#                     else:
#                         print("Wrong Entry TRY AGAIN")
#                         attmpsc+=1
#                         if(attmpsc>=4):
#                             print(f"{RED}You Put To many wrong entries GAME OVER{RESET_ALL}")
#                             penguin_game()
#                         else:
#                             first_level_second_challengec()


                        
#     def first_level_second_challenged():
#         global puzzle
#         global attmpsd
#         global puzzle
#         global number
#         global Name
#         global GAME_START
#         password=["a","b","c","d"]
#         pwd3=input("Enter your 4th letter of the password: ")
#         if(pwd3==password[3]):
#             print("Congratulation you passed your first level here is your password")
#             print(password[0])
#             print(password[1])
#             print(password[2])
#             print(password[3])
#             Second_Level()
                                
                                
#         else:
#             print("Wrong Entry TRY AGAIN")
#             attmpsd=attmpsd+1
#             if(attmpsd>=4):
#                 print(f"{RED}You Put To many wrong entries GAME OVER{RESET_ALL}")
#                 penguin_game()
#             else:
#                 first_level_second_challenged()
                
                
                
                
#     #######################################################################################################################
#     #######################################################################################################################
#     #######################################################################################################################

#     def Second_Level():
        
#         print(f"""{YELLOW}{RED_bg}Congratulations you have escaped from the Level 1.\nYou have awarded a map that will direct you to the rebel base”\n\n {RESET_ALL}""")
#         print(f"""{YELLOW}{RED_bg}All the Instruction are inside the map, if you will encounter military penguins they will ask you few questions to check your loyality.
#                 You must have to answer the questions correctly otherwise you will go back to level_1{RESET_ALL}""")
#         print(f"{YELLOW}{RED_bg}\n\n\n\nUnfortunately Military pengunies catch you and asking you the security questions to recongnize you. {RESET_ALL}")
#         security_questionsa()
#     def security_questionsa():
#             input_sec=input("Press a to let the question begins: \nPress b to go to first level:\n")
#             if input_sec=="a" or input_sec=="A":
#                 inpt_ques=input(f"{YELLOW}{RED_bg}What is your Security Number: \na)45612\nb)56754\nc)57431\nd)15982\nEnter only one asnwer a,b,c or d:{RESET_ALL}")
#                 if(inpt_ques=="b"):
#                     print(f"{BLUE}Congrats you have passed your security check!!!!!!!!!!{RESET_ALL}")
#                     security_questionsb()
#                 else:
#                     print("Your answer is wrong try again")
#                     security_questionsa()
#             elif(input_sec=="b" or "B"):
#                 penguin_game()
#             else:
#                 print("you put the wrong entry try again")
#                 security_questionsa()
#     def security_questionsb():
#             input_sec=input("Press a to start the second question:\n")
#             if input_sec=="a" or input_sec=="A":
#                 inpt_ques=input(f"{YELLOW}{RED_bg}What is the uniform color of PENGUIN Army: \na)Blue\nb)Black\nc)Orange\nd)Green\nEnter only one aswer a,b,c,d: {RESET_ALL}")
#                 if(inpt_ques=="a"):
#                     print(f"{BLUE}Congrats you have passed your security check!!!!!!!!!! and moving to the next Level{RESET_ALL}")
#                     Level_3()
#                 else:
#                     print("Your answer is wrong try again")
#                     security_questionsb()
#             else:
#                 print("You put the wrong entry try again")
#             security_questionsb()   
#     def Level_3():
#         global number
#         global attmps
#         attmps=0
#         global attmpsb
#         attmpsb=0
#         global attmpsc
#         attmpsc=0
#         global attmpsd
#         attmpsd=0
#         global Name
#         global attempts
#         attempts=0
#         global t
#         global time
#         global puzzle
#         global inpt_q2
#         print(f"""{YELLOW}{RED_bg}Congratulations you have made it to the Rebel Base and are entering Level 3 of the game.{RESET_ALL}""") 
#         inpt_entergame=input("press a to continue to the rebilion base:\n" )
#         if (inpt_entergame=="a" ):
#                 print(f"""{YELLOW}{RED_bg}Now Your identity will be checked by answering 2 questions correctly.
#                     If you fail to answer you will be shot dead and the game will end.{RESET_ALL}""")
                
#                 inpt_q1=input("What is the Operation Name:\na)Icecap\nb)Thriller\nc)Skylight\n")
#                 if(inpt_q1=="b"):
                
#                     print(f"{YELLOW}{RED_bg}Congratulation,You get the first identity now you are moving to Question 2 {RESET_ALL}")
                
#                     second_id_qst()
#                 else:
#                     print("GAME OVER")
#                     penguin_game()

        
#         else:
#             print("you put the wrong entry try again, going back to Level 3")
#             Level_3()
            
            
            
#     def second_id_qst():
#         global number
#         global attmps
#         attmps=0
#         global attmpsb
#         attmpsb=0
#         global attmpsc
#         attmpsc=0
#         global attmpsd
#         attmpsd=0
#         global Name
#         global attempts
#         attempts=0
#         global t
#         global time
#         inpt_q2=input("What is the Rebilion Commander Name:\na)Commander Grand Admiral\nb)Commander Luke Moonwalker\nc)Commander Cobra\n")
#         if(inpt_q2=="b"):
        
#             print(f"{YELLOW}{RED_bg}Congratulation, Now you entered in to the Rebilion Base\nNow you meet the leader of the Rebilion who is working on a plot to overthrow the PENGUIN overlord\nYou and the rebels are now outside the Penguin Overlord base.\nTo gain entry into their base you must use the very same pass code that was used to escape the prison.{RESET_ALL}\n\n\n")
        
#         inpt_paswd=input("Do you remember it from before? press y for yes and n for No: \n")
#         if(inpt_paswd=="y"):
#             inpt_pascode=int(input("Enter the Prison Pass Code: "))
#             if(inpt_pascode==1234):
#                 last_puzzle()
#             else:
#                 print(f"{RED}Incorrect Prison Pass Code!!!!! Now you have been captured by the PENGUINs and send back to the prison.{RESET_ALL}")
#                 print(f"{RED} GAME OVER!!!!!! {RESET_ALL}")  
#                 penguin_game() 
#         elif(inpt_paswd=="n"):
#             (print(f"{RED}GAME OVER!!!!!!"))
#             penguin_game()
#         else:
#             print(f"{RED}GAME OVER{RESET_ALL}")
#             penguin_game()


#     def last_puzzle():
        
#         global number
#         global attmps
#         attmps=0
#         global attmpsb
#         attmpsb=0
#         global attmpsc
#         attmpsc=0
#         global attmpsd
#         attmpsd=0
#         global Name
#         global attempts
#         attempts=0
#         global t
#         global time
#         global time
#         global t
#         global puzzle_ans
#         print(f"{YELLOW}{RED_bg}Well done you remembered the correct pass code and you make it into the base.\n\n{RESET_ALL}")
#         time.sleep(2)
#         print(f"""{BLUE}If, however, you are successful you and the rebels try to infiltrate their base of all its operations.
#     You ambush and attack several guards.
#     Great you have now overcome the penguin guards.
#     Now your plan is to infiltrate the Penguin Overlord operational control room.
#     The penguins have a plan to secretly mine the earth for its natural resources until it is completely devoid of all its raw materials, and then they plan to destroy it.
#     It's a race against time.... By the time you and The Rebellion reach their base's operational control room, the penguins are already in the process of destroying the earth.\n\n\n{RESET_ALL}""")
#         # time.sleep(3)
#         print(f"{YELLOW}{RED}You now must solve a selection of 2 question and the outcome dictates the ending.{RESET_ALL}")
#         Second_puzzle_ques()
#     def Second_puzzle_ques():
#         global number
#         global attmps
#         attmps=0
#         global attmpsb
#         attmpsb=0
#         global attmpsc
#         attmpsc=0
#         global attmpsd
#         attmpsd=0
#         global Name
#         global attempts
#         attempts=0
#         global t
#         global time
#         global inpt_second_puzzle
#         global time
#         global t
#         inpt_second_puzzle=input("Rock band attempted to adapt J.R.R. Tolkien's The Lord of the Rings in 1968?\na)The Rolling Stones\nb)The Beatles\nc)The Who\nd)The Beates\n")
#         if(inpt_second_puzzle=="c"):
#             print("Congratulation you have passed the second question and moving to last question")
#             puzzle_timer()
#         else:
#             print("GAME OVER going back to level 2")
#         Second_Level()

#     def puzzle_timer():
#         #    global time
#         global inpt_second_puzzle
#         global time
#         t=10
#         while t:
#             mins=t//60
#             secs=t%60
#             timer='{:02d}:{:02d}'.format(mins,secs)
#             print("" + timer, end="\r") #overwrite previous line
            
#             #  puzzle_ans=input("Enter y for TRUE and n for FALSE:\n")
#             time.sleep(1)

#             t=t-1
#         Last_ques()
#     def Last_ques():
#         last_puzz=input(f"{YELLOW}{RED}Three ants are sitting at the three corners of an equilateral triangle. Each ant starts randomly picks a direction and starts to move along the edge of the triangle.\n is there any possibility  of the ants not to collide? Enter y or n\n{RESET_ALL}")
#         if(last_puzz=="y"):
#             print(f"{GREEN}C O N G R A T U L A T I O N S YOU HAVE SAVED THE WORLD AND WON THE GAME:{RESET_ALL}")
#         else:
#             print("The penguins Win and the earth is destroyed. Unfortunately you and the Rebellion have failed and the game is over.")
            
#             print("GAME OVER")
          
    
#     intro()
# game()


# ##Game created by the team Feb2022
# import sys
# import time
# import random

# def sprint(str): # sprint slowly function
#     for c in str + '\n': 
#         sys.stdout.write(c) # sprint 1 letter at a time
#         sys.stdout.flush() # clear the sprint buffer
#         time.sleep(0.00) # time delay

# def game():
#     def intro():
#         sprint("Welcome to the latest game for 2022, 'This is the Next Skyrim\' *[cough cough]*\n")
#         answer = input("Would you like to play...? (yes/no) ")
#         if answer == "yes" or answer == "y" or answer == "YES" or answer == "Y" or answer == "Yes":
#             stage_one()
            
#         elif answer == "no" or answer == "n" or answer == "NO" or answer == "N" or answer == "No":
#             sprint("You are boring\n")
#             sprint("Game Over!!")
#             game_over()
#         else:
#             sprint("This is not an option, type yes or no")
#             intro()
                   
# ##game_start() loops back to the beginning so user can input again
#     def stage_one(): 
#         name = input("What is your name? ").title()
#         sprint(f"Greetings, {name} lets start an adventure...")
#         sprint("You are in London on a friday night and have just finished your 9hrs\nshift as a NHS doctor at Sandmere NHS Practice.\n")
#         sprint("The NHS practice is in South London and you like to avoid taking\nthe tube because you can get a few journey beers on the way home.")
#         stage_two()
        
#     def stage_two():         
#         sprint("You are very thirsty and try to work out where you want to head to first,\n")
#         sprint("You know the quickest way to get a beer is at the local, two")
#         sprint("streets away, but it is a rough pint in a dirty glass - Pint A\n")
#         sprint("Your other option is to walk twice the distance to get a Frosted and Crisp ale")
#         sprint("at Londons finest tavern up North. It is clean and you are less likely to get ill - Pint B\n")
# #Input your drink order on the line below
#         answer2 = input("Do you fancy Pint A or Pint B...?")
# #Rough pint in a dirty glass at the nearest drinkery

#         if answer2 == "Pint A" or answer2 == "pint A" or answer2 == "pint a" or answer2 == "a" or answer2 == "A" or answer2 == "Pint a":
            
#             sprint("Urrrgh that beer nearly came back up, but you feel a")
#             sprint("bit more drunk, you just become more determined to get")
#             sprint("to a \'real\' party, that is a jumping rave!!!\n")
#             #continue Yes or No    
#             stage_three()
            
# #Frosted and crisp ale at Londons finest tavern up North
#         elif answer2 == "Pint B" or answer2 == "pint A" or answer2 == "pint b" or answer2 == "b" or answer2 == "B" or answer2 == "Pint b":
#             sprint("That was a cracking beer, you decide to have another")
#             sprint("as the barmaid was giving you the eye, then you move on")
#             stage_three()
#         else:
#             sprint("This is not an option, you need a drink")
#             sprint("Type \'Pint A\' or \'Pint B\'")
# #The stage_two just runs the function again till it gets true answer
#             stage_two()
# #Help the man, below, who is crying
#     def stage_three(): 
#         sprint("You stagger uptown to a crossroads that has an traffic island in the middle")
#         sprint("you see a man there, crying with his back to a lampost. He is wearing a suit")
#         sprint("and you notice in one hand he has a briefcase, with the initials M.H. on it.\n")
#         sprint("In his other hand he has an NHS leaflet and some envelopes. He looks down on his luck\n")
#         sprint("The man looks up and shouts over to you to come and speak to him")
#         sprint("He says if you help him to the nearby bench that he will give you a chance to")
#         sprint("win a prize if you can beat him at his game.\n")
        
#         answer3 = input("Do you help this man? (yes/no)")
        
#         if answer3 == "yes" or answer3 == "y" or answer3 == "YES" or answer3 == "Y" or answer3 == "Yes":
#             sprint("You help the man, he is very grateful and challenges you to a game\n")
#             stage_four()
            
#         elif answer3 == "no" or answer3 == "n" or answer3 == "NO" or answer3 == "N" or answer3 == "No":
#             sprint("Do not help him, you decide it is better to go to the shop and get a microwaveable")
#             sprint("meal and cry yourself to sleep. Game Over!!")
#             game_over()
            
#         else:
#             sprint("This is not an option, type yes or no")
#             stage_three()
# #insert word game here, Amar or joke we ran out of money
#     def stage_four(): 
#         answer3 = input("Do you want to play the word game for a prize\n (yes/no)")
#         if answer3 == "yes" or answer3 == "y" or answer3 == "YES" or answer3 == "Y" or answer3 == "Yes":
#             sprint("Unfortunately the coding team ran out of money and time, John got")
#             sprint("sacked for his imcompetence. The man gives you the prize anyway.")
#             sprint("He says he will give you an envelope depending on which direction")
#             sprint("you will walk next")
#             stage_five()
#         elif answer3 == "no" or answer3 == "n" or answer3 == "NO" or answer3 == "N" or answer3 == "No":
#             sprint("Do not help him, you decide it is better to go to the shop and get a microwaveable")
#             game_over()
# #insert yusef North, East, West here, below
#     def stage_five():
        
#         answer = input("Do you take the path to the North, East or West\n")
        
#         if answer == "North" or answer == "north":
#             sprint("you chose to go North\n")
#             stage_ten()
            
#         elif answer == "East" or answer == "east":
#             sprint("you chose to go east\n")
#             sprint("Go east to peckham")
#             sprint("You notice a gang following you and get a bit scared")
#             sprint("You run down an alley and feel something in the envelope")
#             sprint(" so you open it and find inside a BLOCK of CHEESE")
#             stage_seven()
            
#         elif answer == "West" or answer == "west":
#             sprint("you chose to go waest\n")
#             sprint("Go west to Chelsea there is a cash machine right in front of you")
#             sprint("a very rich area and")
#             sprint("you open the envolope and find a bank card and the pin number wrote on it")
#             stage_eight()
            
#         else:
#             sprint("This is not an option, type either East,west or North")
#             stage_five()

#     def stage_seven():
#         print("Hello")
#         exit()
#     def stage_eight():
#         print("Hello")
#         exit()
# #North route below
#     def stage_ten(): 
#         sprint("Go north towards Westminister, there is a large house with lots of lights")
#         sprint("and music coming out of it. you see the numbers 1 and 0 on a shiny black door.\n")
#         sprint("you open the envolope and see a hand written invitation from Boris johnson.")
#         sprint("You see a doorman who asks for your invitation. He asks who you here with...?")
#         guest_list()            
# # guest_who_invited_you
#     def guest_list():
#         question = int(input("""Who invited you? Please choose a name by typing the number
#             "1. Your friend Timmy",\n
#             "2. Sajid Javid",\n
#             "3. Boris Johnson",\n
#             "4. Matt Hancock,\n
#             "you choose ________"""))
        
#         if question == 1:
#             print("Your friend Jimmy\n")
#             print("The doorman does not know who this name is...")
#             print("you quickly guess again --->>>")
#             guest_list()
            
#         elif question == 2:
#             print("Sajid Javid\n")
#             print("The doorman is not happy with your policies")
#             print("on health and social care. He hits you and you are\n")
#             print("KNOCKED OUT...Game Over")
#                 # game_over()
#             exit()
            
#         elif question == 3:
#             print("Boris Johnson\n")
#             print("Ahhh Boza, my main man Boza, yeah he is inside")
#             print("Let the guy know he owes me some columbian green")
# ## First though I need to check your age, how old are you
# #insert next stage, meeting Boris then number game
#             stage_eleven() 
#             exit()
            
#         elif question == 4:
#             print("Matt Hancock\n")
#             print("Who M.H, he got sacked the other day for fooling")
#             print("around with the staff. I dont like the guy...")
#             print("but he is on the list. In you go buddy!!!")
# ## First though I need to check your age, how old are you
#             stage_eleven()
#             exit()
            
#         else:
#             print("Enter a number to continue")
#             print("It is cold and you do not want to be")
#             print("stuck out here all night")
#             guest_list()
#         guest_list()

# #imran & samman work! to go here, below  , age checker stage
#     def stage_eleven():     
#         age = input("Enter your age \n")
#         if int(age) >= (18):
#             sprint("you are old enough to play the number game \n let's start")
#             n_guess(x)
#         elif int(age) <= (17):
#             sprint("you are a kid")
#             sprint("game over!!")
#             exit()
#         else:
#             sprint("This is not an option")
#             stage_eleven()
# #imran & samman work! to go here, above


# # you meet boris and he asks you to play number game, below
# # do you play his game (yes/no)
#     def n_guess(x):
#         random_number = random.randint(1, 10)
#         guess = 0
#         while guess != random_number:
#             guess = int(input(f"Guess a number between 1 and 10 : "))
#             if guess < random_number:
#                 print("Sorry guess again too low")
#             elif guess > random_number:
#                 print("Sorry, guess again too high")
#             print(f"yay, congrats. you have guessed the number {guess} correctly")
#             n_guess(10)

#     def game_over():
#                 print("""
#          .88888.   .d888888  8888ba.88ba   88888888b     .88888.  dP     dP  88888888b  888888ba  
#         d8'   `88 d8'    88  88  `8b  `8b  88           d8'   `8b 88     88  88         88    `8b 
#         88        88aaaaa88a 88   88   88 a88aaaa       88     88 88    .8P a88aaaa    a88aaaa8P' 
#         88   YP88 88     88  88   88   88  88           88     88 88    d8'  88         88   `8b. 
#         Y8.   .88 88     88  88   88   88  88           Y8.   .8P 88  .d8P   88         88     88 
#         `88888'  88     88  dP   dP   dP  88888888P     `8888P'  888888'    88888888P  dP     dP 
#         oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#         """)
#                 exit()

#     intro()
# game()

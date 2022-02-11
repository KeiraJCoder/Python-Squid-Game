import time
import sys
import random
import turtle
from turtle import Turtle
from turtle import Screen



def game ():
    def sprint(str): # sprint slowly function
        for c in str + '\n': 
            sys.stdout.write(c) # sprint 1 letter at a time
            sys.stdout.flush() # clear the sprint buffer
            time.sleep(0.03) # time delay
    def ssprint(str): # sprint slowly function
        for c in str + '\n': 
            sys.stdout.write(c) # sprint 1 letter at a time 
            sys.stdout.flush() # clear the sprint buffer
            time.sleep(0.004) # time delay       
    def start():
        ssprint("""\033[31m
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        MMMMMMMMMMMMMMNNMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        MMMMMMMMms/-``````-+yNMMMMMMMMMMMMMM+ ```````````````````` `MMMMMMMMMMMMMMMMMMMMMMs-NMMMMMMMMMMMMMMM
                        MMMMMMh: :sdNMMMMNdo- /dMMMMMMMMMMMM+ yMMMMMMMMMMMMMMMMMMM `MMMMMMMMMMMMMMMMMMMMM+ `.dMMMMMMMMMMMMMM
                        MMMMN: +mMMMMMMMMMMMMm: +MMMMMMMMMMM+ yMMMMMMMMMMMMMMMMMMM `MMMMMMMMMMMMMMMMMMMN/ sN-`hMMMMMMMMMMMMM
                        MMMN. hMMMMMMMMMMMMMMMMs :MMMMMMMMMM+ yMMMMMMMMMMMMMMMMMMM `MMMMMMMMMMMMMMMMMMN-`hMMN: sMMMMMMMMMMMM
                        MMMo oMMMMMMSQUIDMMMMMMM/ yMMMMMMMMM+ yMMMMMMSQUIDMMMMMMMM `MMMMMMMMMMMMMMMMMm.`dMMMMM+ +MMMMMMMMMMM
                        MMM- mMMMMMMGAMEMMMMMMMMh /MMMMMMMMM+ yMMMMMMGAMEMMMMMMMMM `MMMMMMMMMMMMMMMMh`-mMMMMMMMs :NMMMMMMMMM
                        MMM: dMMMMMMMMMMMMMMMMMMs +MMMMMMMMM+ yMMMMMMMMMMMMMMMMMMM `MMMMMMMMMMMMMMMy :NMMSQUIDMMh`-NMMMMMMMM
                        MMMh -MMMMMMMMMMMMMMMMMN. mMMMMMMMMM+ yMMMMMMMMMMMMMMMMMMM `MMMMMMMMMMMMMMo +MMMMGAMEMMMd`.mMMMMMMMM
                        MMMMs :NMMMMMMMMMMMMMMm- hMMMMMMMMMM+ yMMMMMMMMMMMMMMMMMMM `MMMMMMMMMMMMM/ sMMMMMMMMMMMMMMm-`hMMMMMM
                        MMMMMd-`+dMMMMMMMMMMd/ :mMMMMMMMMMMM+ yMMMMMMMMMMMMMMMMMMM `MMMMMMMMMMMN-`hMMMMMMMMMMMMMMMMN: sMMMMM
                        MMMMMMMh/`./osyys+:``+dMMMMMMMMMMMMM+ +yyyyyyyyyyyyyyyyyyy `MMMMMMMMMMm. oyyyyyyyyyyyyyyyyyyy. +MMMM
                        MMMMMMMMMMmyo++++shmMMMMMMMMMMMMMMMMy+++++++++++++++++++++++MMMMMMMMMNo+++++++++++++++++++++++++hMMM
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                  \033[0;37;40m""")
        # start ends here
        intro()
            
    def intro():
            global intro
            answer=input("                                                              Do you want to play? ") 
            if answer.lower()=="yes" or answer.lower()=="y":
                character() 
            elif answer.lower()=="no" or answer.lower()=="n":
                sprint("                                                   You know where we are if you change your mind")
                exit 
            else:
                sprint("Okay then.")
                exit() 
                               
    def character():
            global name
            global number
            global number1
            global contestants
            global prize
            global chance
            
            
            chance = 0
            contestants = 456
            
            name=input("                                                               What is your name? ")
            if name == "keira".lower():
                sprint("                                                                   Welcome Creator")
            elif name == "frankie".lower():
                sprint("                                                                   Hello my love")
            person= input("                                                                   Type 1, 2 or 3 \n\n") 
            number=random.randint(1,456)
            number1=random.randint(1,222)
            prize=0
            if person =="1":      
                game_start()
            elif person =="2":
                game_start()
            elif person =="3":
                game_start()
            elif person =="1987":
                sprint("                                                                 Welcome Overseer\n\n")
                game_three()
            
    def game_start():
            global play_again
            global number
            global name
            global prize
            ssprint(f"""\033[0;32m                          
                                ===================================================================================
                                |             You are all here for the same reason, you all need money              |
                                |     You may have serious debts that you have no hope in paying without a miracle  |
                                |                           Think of this as your miracle                           |
                                |          If you win all of your games you will win the total prize pot            |
                                |                    There are currently {contestants} contestants competing                  |
                                |                        Each participant is worth around \033[94m£100,000\033[0;32m                  |
                                |                  There must be only one remaining after all games                 |
                                |                                     Good luck                                     |
                                ====================================================================================
                    \033[0;37;40m""") 
            
                   
            sprint(f"                                  Welcome to the first game. You have been randomly assigned as contestant {number}\n")
            sprint(f"                                                          The prize pot currently stands at \033[94m£{prize}\033[0;37;40m\n\n")
            sprint("                                                        Our first game is a childhood favourite.\n")
            ssprint(
                    """\033[0;32m
                                        ╔═══╗        ╔╗      ╔═══╗                    ╔═══╗
                                        ║╔═╗║        ║║      ║╔═╗║                    ║╔═╗║
                                        ║╚═╝║╔══╗╔══╗║║╔╗    ║╚═╝║╔══╗ ╔══╗╔══╗╔═╗    ║╚══╗╔══╗╔╗╔══╗╔══╗╔══╗╔═╗╔══╗
                                        ║╔╗╔╝║╔╗║║╔═╝║╚╝╝    ║╔══╝╚ ╗║ ║╔╗║║╔╗║║╔╝    ╚══╗║║╔═╝╠╣║══╣║══╣║╔╗║║╔╝║══╣
                                        ║║║╚╗║╚╝║║╚═╗║╔╗╗    ║║   ║╚╝╚╗║╚╝║║║═╣║║     ║╚═╝║║╚═╗║║╠══║╠══║║╚╝║║║ ╠══║
                                        ╝╚═╝╚══╝╚══╝╚╝╚╝     ╚╝   ╚═══╝║╔═╝╚══╝╚╝     ╚═══╝╚══╝╚╝╚══╝╚══╝╚══╝╚╝ ╚══╝
                                                                       ║║
                                                                       ╚╝
                    """
            )
            sprint("                                                You will choose how many rounds you play to beat the game")
            sprint("                                                          If you lose you will be eliminated\n\n")
            game_1()
                    
    def game_1():
        global name
        global number
        global contestants
        
        options = ['rock', 'paper', 'scissors']

        while True:
                try:
                    turns = int(input("Best of 3 or best of 5? "))
                    if turns == 3 or turns == 5:
                        break
                    continue
                except ValueError:
                    sprint("Invalid choice.")

        necessary_wins = int(turns/2) + 1

        player_wins = 0
        computer_wins = 0

        while True:

                while True:
                    player = input("rock, paper, scissors: ")
                    if player in options:
                        break

                computer = random.choice(options)

                if player == computer:
                    sprint('It is a tie')
                elif player == 'rock' and computer == 'paper':
                    sprint('I win, paper covers rock')
                    computer_wins += 1
                elif player == 'rock' and computer == 'scissors':
                    sprint('You win, rock smashes scissors')
                    player_wins += 1
                elif player == 'paper' and computer == 'rock':
                    sprint('You win, paper covers rock')
                    player_wins += 1
                elif player == 'paper' and computer == 'scissors':
                    sprint('I win, scissors cut paper')
                    computer_wins += 1
                elif player == 'scissors' and computer == 'rock':
                    sprint('I win, rock smashes scissors')
                    computer_wins += 1
                elif player == 'scissors' and computer == 'paper':
                    sprint('You win, scissors cut paper')
                    player_wins += 1

                if player_wins == necessary_wins or computer_wins == necessary_wins:
                    break

        if player_wins > computer_wins:
            sprint(f'                                       Congratulations contestant number {number} You may continue to the next game\n')
            contestants -= random.randint(95, 137)
            prize =+ random.randint(9500000, 13700000)
            sprint(f"                                                       There are {contestants} contestants remaining \n\n\n")
            sprint(f"                                                     The prize pot currently stands at \033[94m£{prize}\033[0;37;40m\n\n")
            game_two_intro()
        else:
            sprint(f'                                                          I win. You will now be eliminated. \n\n')
        game_over()
    
    def game_two_intro():
        global number1
        global number
        global name
        global prize
        sprint(f"                         Welcome to the second game. You are contestant {number}. We will be playing a game of chance.\n")
        game_two()
        
    def game_two():
        ssprint(
                                                        """
                                                     _______
                                                    /\ o o o\.
                                                   /o \ o o o\_______
                                                  <    >------>   o / |
                                                   \ o/  o   /_____/ o|
                                                    \/______/       |o|
                                                            |   o   |o/
                                                            |_______|/                                                                     
                                        DDDDDDDDDDDDD      IIIIIIIIII      CCCCCCCCCCCCCEEEEEEEEEEEEEEEEEEEEEE
                                        D::::::::::::DDD   I::::::::I   CCC::::::::::::CE::::::::::::::::::::E
                                        D:::::::::::::::DD I::::::::I CC:::::::::::::::CE::::::::::::::::::::E
                                        DDD:::::DDDDD:::::DII::::::IIC:::::CCCCCCCC::::CEE::::::EEEEEEEEE::::E
                                        D:::::D    D:::::D I::::I C:::::C       CCCCCC  E:::::E       EEEEEE
                                        D:::::D     D:::::DI::::IC:::::C                E:::::E             
                                        D:::::D     D:::::DI::::IC:::::C                E::::::EEEEEEEEEE   
                                        D:::::D     D:::::DI::::IC:::::C                E:::::::::::::::E   
                                        D:::::D     D:::::DI::::IC:::::C                E:::::::::::::::E   
                                        D:::::D     D:::::DI::::IC:::::C                E::::::EEEEEEEEEE   
                                        D:::::D     D:::::DI::::IC:::::C                E:::::E             
                                        D:::::D    D:::::D I::::I C:::::C       CCCCCC  E:::::E       EEEEEE
                                        DDD:::::DDDDD:::::DII::::::IIC:::::CCCCCCCC::::CEE::::::EEEEEEEE:::::E
                                        D:::::::::::::::DD I::::::::I CC:::::::::::::::CE::::::::::::::::::::E
                                        D::::::::::::DDD   I::::::::I   CCC::::::::::::CE::::::::::::::::::::E
                                        DDDDDDDDDDDDD      IIIIIIIIII      CCCCCCCCCCCCCEEEEEEEEEEEEEEEEEEEEEE
                                                                                                            
                                                                                                            
            
                            \n""")   
        
        sprint("                                        You have been assigned another contestant to play against.\n")
        sprint("                                             The person with the highest number wins each round\n")
        sprint("                                      The first contestant to get to 5 wins continues to the next game\n")
        sprint("                                                       The loser will be eliminated\n")
        sprint("                                                               Good luck\n \n")
        game_two_start()
        
    def game_two_start(): 
    
        # Initialise player scores to 0
        player1_score = 0
        player2_score = 0

        # Repeat everything in this block 10 times
        for i in range(15):

            # Generate random numbers between 1 and 6 for each player.
            player1_value = random.randint(1, 6)
            player2_value = random.randint(1, 6)
            
            # Display the values
            sprint(f"You rolled: {player1_value}")
                
            sprint(f"Contestant {number1} rolled: {player2_value}")

        # Selection: based on comparison of the values, take the appropriate path through the code.
            if player1_value == player2_value:
                sprint("Draw, no winner.\n")
                sprint("Play again.")
            elif player1_value > player2_value:
                sprint(f"\nYou win this round.\n")
                player1_score = player1_score + 1  # This is how we increment a variable
                ssprint(f"""
                                                            ===========================
                                                            Your score is {player1_score}
                                                            ===========================
                                                            Contestant {number1}'s score is {player2_score}
                                                            ===========================
                       """)
                input("\nPress enter to roll again ")
                if player1_score == 5:
                    ssprint(f"Congratulations contestant {number}, you may continue\n\n\n")
                    ssprint(f"""
                                                            ===========================
                                                             Your score was: {player1_score}
                                                            ==========================
                                                            Contestant {number1} score:, {player2_score}
                                                            ==========================
                           
                           """)
                    
                    input("\nPress enter to continue ")
                    congratulations()
            elif player2_value > player1_value:
                sprint(f"\nContestant {number1} wins this round\n\n")
                player2_score = player2_score + 1
                ssprint(f"""
                      
                                                            ===========================
                                                                Your score is {player1_score}
                                                            ===========================
                                                            Contestant {number1}'s score is {player2_score}
                                                            ===========================
                      """)
                input("\nPress enter to seal your fate \n")
                if player2_score >= 5:
                    ssprint(f"""
                                                            ==========================
                                                                Your score was:, {player1_score}
                                                            ==========================
                                                            Contestant {number1}'s score was:, {player2_score}
                                                            ===========================
                          """)
                    ssprint(f"""
                                                            ===============================
                                                    You lose contestant {number}. You will now be eliminated
                                                            ===============================
                           """)
                    ssprint(f""" 
                                                            ===============================
                                                                    Have a nice day
                                                            =============================== \n""")
                    input("                                     \nPress enter to continue ")
                    game_over()
            else:
                sprint("""
                                                                ==========================
                                                                |  THERE CAN BE NO DRAW  |
                                                                |      PLAY AGAIN        |
                                                                ==========================
                      
                      
                      \n""")
                game_three()
    def game_three():
        sprint(f"                         Welcome to the third game. You are contestant {number}. We will be playing a game of skill\n")
        ssprint(
                                                        """
                                             ________ __    __ _______  ________ __       ________ 
                                            |        \  \  |  \       \|        \  \     |        \.
                                             \▓▓▓▓▓▓▓▓ ▓▓  | ▓▓ ▓▓▓▓▓▓▓\\▓▓▓▓▓▓▓▓  ▓▓     | ▓▓▓▓▓▓▓▓
                                               | ▓▓  | ▓▓  | ▓▓ ▓▓__| ▓▓  | ▓▓  | ▓▓     | ▓▓__    
                                               | ▓▓  | ▓▓  | ▓▓ ▓▓    ▓▓  | ▓▓  | ▓▓     | ▓▓  \   
                                               | ▓▓  | ▓▓  | ▓▓ ▓▓▓▓▓▓▓\  | ▓▓  | ▓▓     | ▓▓▓▓▓   
                                               | ▓▓  | ▓▓__/ ▓▓ ▓▓  | ▓▓  | ▓▓  | ▓▓_____| ▓▓_____ 
                                               | ▓▓   \▓▓    ▓▓ ▓▓  | ▓▓  | ▓▓  | ▓▓     \ ▓▓     \.
                                                \▓▓    \▓▓▓▓▓▓ \▓▓   \▓▓   \▓▓   \▓▓▓▓▓▓▓▓\▓▓▓▓▓▓▓▓                                                                             
            
                            \n""")   
        
        sprint("                                          You will play this game alone, no others can help you\n")
        sprint("                                     The people able to complete the task within the time will continue\n")
        sprint("                                        Those who fail or who run out of time will be eliminated\n")
        
        sprint("                                                               Good luck\n \n")
        
        
        game_three_start()
        
    
    
    def game_three_start():
        global chance

        shapes =[
            "Square",
            "Circle",
            "Star",
            "Spiral"
        ]
        
        shapes1 = random.choice(shapes)

        
        sprint("It is time to make a choice, before you stands four doors.\n")
        sprint("Each door is emblazoned with a number\n")
       
        choice2 = int(input("Which door do you choose? 1, 2, 3 or 4? \n\n"))
        
        if chance <= 1:
            chance += 1
            if choice2 == 1:
                sprint("You have chosen the First door\n")
                sprint(f"Your shape will be {shapes1}\n")
                sprint("Good luck")
                
            elif choice2 == 2:
                sprint("You have chosen the Second door\n")
                sprint(f"Your shape will be {shapes1}\n")
                sprint("Good luck")
                
            elif choice2 == 3:
                sprint("You have chosen the Third door\n")
                sprint(f"Your shape will be {shapes1}\n")
                sprint("Good luck")
                
            elif choice2 == 4:
                sprint("You have chosen the Fourth door\n")
                sprint(f"Your shape will be {shapes1}\n")
                sprint("Good luck")
            else:
                sprint("Do not test me\n\n")
                game_three_start()
        else:
            sprint("I told you not to test me\n\n")
            game_over()
        
        
                    
    def drawing():
        wn=turtle.Screen()
        wn.bgcolor("green")
        
        player=turtle.Turtle()
        player.color("red")
        player.penup()
        
        speed = 1
    
    def turnleft():
        
        player.left(30)
        
        
        turtle.listen()
        turtle.onkey(turnleft, 'Left')
        
        while True:
            player.forward(speed)
        
        delay = input("Press enter to finish")
                
        
    def congratulations():

        ssprint("""
                                            db    db  .d88b.  db    db   db   d8b   db d888888b d8b   db
                                            `8b  d8' .8P  Y8. 88    88   88   I8I   88   `88'   888o  88
                                             `8bd8'  88    88 88    88   88   I8I   88    88    88V8o 88
                                               88    88    88 88    88   Y8   I8I   88    88    88 V8o88
                                               88    `8b  d8' 88b  d88   `8b d8'8b d8'   .88.   88  V888
                                               YP     `Y88P'  ~Y8888P'    `8b8' `8d8'  Y888888P VP   V8P
                            
                  """) 
            
        winnings = (45600000)
        sprint(f"                                               You won a grand total of \033[94m£{winnings}")
        sprint("                                                           And your life")
        sprint("                                           I hope you can live with the guilt of killing 455 others")
        exit()  
        
    def game_over():
        global game_over
     
        death_note = [
            "                                        You were impaled with a pair of giant scissors", 
            "                                               You were crushed by a giant rock",
            "                                           From one meter away, you were shot in the face", 
            "                                          Someone dressed as a MR-Man tickled to death",
            "                                        You were thrown from an airplane with no parachute", 
            "                                  You mysteriously vanished, your body washed up on a beach 1 year later", 
            "                                          You were cut by 1 million razor blades one at a time",
            "                                            You were killed by the Bay Harbour Butcher",
            "                                            You were suffocated in a vat of icecream",
            "                                        You were stoned to death by a jury of your peers",
            "                            A potent nerve gas was released into the room, killing you slowly and agnoisingly "
            ]
        
        count_down = 3
        while (count_down > 3):
            print(count_down)
            count_down -=  1
        print(random.choice(death_note)+" ")
        ssprint(""" 
                                        ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
                                        ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
                                        ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
                                        ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
                                        ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
                                        ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
                                        ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
                                            ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
                                            ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                                                                                ░                  
                            
        """)  
        exit()
    start()
game()            
                        
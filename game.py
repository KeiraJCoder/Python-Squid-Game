import time
import sys
import random



def game ():
    def sprint(str): # sprint slowly function
        for c in str + '\n': 
            sys.stdout.write(c) # sprint 1 letter at a time
            sys.stdout.flush() # clear the sprint buffer
            time.sleep(0.04) # time delay
    def ssprint(str): # sprint slowly function
        for c in str + '\n': 
            sys.stdout.write(c) # sprint 1 letter at a time
            sys.stdout.flush() # clear the sprint buffer
            time.sleep(0.005) # time delay       
    def start():
        ssprint("""
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
                  MMMh -MMMMMMMMMMMMMMMMMN. mMMMMMMMMM+ yMMMMMMMMMMMMMMMMMMM `MMMMMMMMMMMMMMo +MMMMGAMEMMMd`.mMMMMMMM
                  MMMMs :NMMMMMMMMMMMMMMm- hMMMMMMMMMM+ yMMMMMMMMMMMMMMMMMMM `MMMMMMMMMMMMM/ sMMMMMMMMMMMMMMm-`hMMMMMM
                  MMMMMd-`+dMMMMMMMMMMd/ :mMMMMMMMMMMM+ yMMMMMMMMMMMMMMMMMMM `MMMMMMMMMMMN-`hMMMMMMMMMMMMMMMMN: sMMMMM
                  MMMMMMMh/`./osyys+:``+dMMMMMMMMMMMMM+ +yyyyyyyyyyyyyyyyyyy `MMMMMMMMMMm. oyyyyyyyyyyyyyyyyyyy. +MMMM
                  MMMMMMMMMMmyo++++shmMMMMMMMMMMMMMMMMy+++++++++++++++++++++++MMMMMMMMMNo+++++++++++++++++++++++++hMMM
                  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                  """)
        # start ends here
        intro()
            
    def intro():
            global intro
            answer=input("Do you want to play? ") 
            if answer.lower()=="yes" or answer.lower()=="y":
                character() 
            elif answer.lower()=="no" or answer.lower()=="n":
                sprint("You know where we are if you change your mind")
                exit 
            else:
                sprint("Okay then.")
                exit() 
                               
    def character():
            global name
            global number
            global number1
            name=input("What is your name? ")
            if name == "keira".lower():
                sprint("Welcome Creator")
            person= input("Choose 1, 2 or 3 ") 
            number=random.randint(1,456)
            number1=random.randint(1,222)
            if person == "1":
                sprint(f"Hello {name} Welcome to Squid Game. You have been assigned the number {number}")       
                game_start()
            elif person =="2":
                sprint(f"Hello {name} Welcome to Squid Game. You have been assigned the number {number}")
                game_start()
            elif person =="3":
                sprint(f"Hello {name} Welcome to Squid Game. You have been assigned the number {number}")
                game_start()
            else:
                sprint("Welcome Overseer")
                game_two()
            
    def game_start():
            global play_again
            global number
            global name
            sprint(f"Welcome to the first game. You are contestant {number} {name}. We will be playing an old favourite.")
            ssprint(
                """
        ╔═══╗        ╔╗      ╔═══╗                    ╔═══╗
        ║╔═╗║        ║║      ║╔═╗║                    ║╔═╗║
        ║╚═╝║╔══╗╔══╗║║╔╗    ║╚═╝║╔══╗ ╔══╗╔══╗╔═╗    ║╚══╗╔══╗╔╗╔══╗╔══╗╔══╗╔═╗╔══╗
        ║╔╗╔╝║╔╗║║╔═╝║╚╝╝    ║╔══╝╚ ╗║ ║╔╗║║╔╗║║╔╝    ╚══╗║║╔═╝╠╣║══╣║══╣║╔╗║║╔╝║══╣
        ║║║╚╗║╚╝║║╚═╗║╔╗╗    ║║   ║╚╝╚╗║╚╝║║║═╣║║     ║╚═╝║║╚═╗║║╠══║╠══║║╚╝║║║ ╠══║
        ╚╝╚═╝╚══╝╚══╝╚╝╚╝    ╚╝   ╚═══╝║╔═╝╚══╝╚╝     ╚═══╝╚══╝╚╝╚══╝╚══╝╚══╝╚╝ ╚══╝
                                    ║║
                                    ╚╝
                    """
            )
            sprint("You will choose how many rounds you play to beat the game")
            sprint("If you lose you will be eliminated")
            game_1()
                    
    def game_1():
        global name
        global number
        
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
            sprint(f' Congratulations contestant number {number} You may continue to the next game\n')
            game_two_intro()
        else:
            sprint(f'I win. You will now be eliminated. \n\n')
        game_over()
    
    def game_two_intro():
        global number1
        global number
        global name
        sprint(f"Welcome to the second game. You are contestant {number} {name}. We will be playing a game of chance.\n")
        game_two()
        
    def game_two():
        ssprint(
                """
               _______
              /\ o o o\.
             /o \ o o o\_______
            <    >------>   o /|
             \ o/  o   /_____/o|
              \/______/     |oo|
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
        
        sprint("You have been assigned another contestant to play against.\n")
        sprint("The person with the highest number wins each round\n")
        sprint("The first contestant to get to 5 wins and can continue to the next game\n")
        sprint("The loser will be eliminated\n")
        sprint("Good luck\n \n")
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
                    ssprint(f"Congratulations contestant {number}, you may continue\n")
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
                sprint(f"\nContestant {number1} wins this round\n")
                player2_score = player2_score + 1
                ssprint(f"""
                      
                                ===========================
                                Your score is {player1_score}
                                ===========================
                                Contestant {number1}'s score is {player2_score}
                                ===========================
                      """)
                input("\nPress enter to roll again ")
                if player2_score >= 5:
                    sprint(f"""
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
                    ssprint(f""" ===============================
                                        Have a nice day
                                =============================== """)
                    input("       \nPress enter to continue ")
                    game_over()
            else:
                sprint("""
                                ==========================
                                |  THERE CAN BE NO DRAW  |
                                |      PLAY AGAIN        |
                                ==========================
                      
                      
                      \n""")
                game_two_start()
                
        
    def congratulations():

        ssprint("""
                            db    db  .d88b.  db    db   db   d8b   db d888888b d8b   db
                            `8b  d8' .8P  Y8. 88    88   88   I8I   88   `88'   888o  88
                            `8bd8'  88    88 88    88   88   I8I   88    88    88V8o 88
                              88    88    88 88    88   Y8   I8I   88    88    88 V8o88
                              88    `8b  d8' 88b  d88   `8b d8'8b d8'   .88.   88  V888
                              YP     `Y88P'  ~Y8888P'    `8b8' `8d8'  Y888888P VP   V8P
                            
                  """) 
            
        winnings = random.randint(2773411000, 5283211000)
        sprint(f"You won a grand total of £{winnings}")
        sprint("And your life")
        exit()  
        
    def game_over():
        global game_over
     
        death_note = [
            "You were impaled with a pair of giant scissors", 
            "You were crushed by a giant rock",
            "From one meter away, you were shot in the face", 
            "Someone dressed as a MR Man tickled to death",
            "You were thrown from an airplane with no parachute", 
            "You mysteriously vanished, your body washed up on a beach 1 year later", 
            "You were cut by 1 million razor blades one at a time",
            "You were killed by the Bay Harbour Butcher",
            "You were suffocated in a vat of icecream",
            "You were stoned to death by a jury of your peers",
            "A potent nerve gas was released into the room, killing you slowly and agnoisingly "
            ]
        
        count_down = 3
        while (count_down):
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
                    
                            
                            
                            
                            
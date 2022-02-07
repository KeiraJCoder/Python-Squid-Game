from random import randint
import random



def game ():
    def start():
        print("""
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
                print("You know where we are if you change your mind")
                exit 
            else:
                print("Okay then.")
                exit() 
                               
    def character():
            global name
            global number
            global number1
            name=input("What is your name? ")
            if name == "keira".lower():
                print("Welcome Creator")
            person= input("Choose 1, 2 or 3 ") 
            number=random.randint(1,456)
            number1=random.randint(1,222)
            if person == "1":
                print(f"Hello {name} Welcome to Squid Game. You have been assigned the number {number}")       
                game_start()
            elif person =="2":
                print(f"Hello {name} Welcome to Squid Game. You have been assigned the number {number}")
                game_start()
            elif person =="3":
                print(f"Hello {name} Welcome to Squid Game. You have been assigned the number {number}")
                game_start()
            else:
                print("Welcome Overseer")
                game_two()
            
    def game_start():
            global play_again
            global number
            global name
            print(f"Welcome to the first game. You are contestant {number} {name}. We will be playing an old favourite.")
            print(
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
            print("You will choose how many rounds you play to beat the game")
            print("If you lose you will be eliminated")
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
                    print("Invalid choice.")

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
                    print('It is a tie')
                elif player == 'rock' and computer == 'paper':
                    print('I win, paper covers rock')
                    computer_wins += 1
                elif player == 'rock' and computer == 'scissors':
                    print('You win, rock smashes scissors')
                    player_wins += 1
                elif player == 'paper' and computer == 'rock':
                    print('You win, paper covers rock')
                    player_wins += 1
                elif player == 'paper' and computer == 'scissors':
                    print('I win, scissors cut paper')
                    computer_wins += 1
                elif player == 'scissors' and computer == 'rock':
                    print('I win, rock smashes scissors')
                    computer_wins += 1
                elif player == 'scissors' and computer == 'paper':
                    print('You win, scissors cut paper')
                    player_wins += 1

                if player_wins == necessary_wins or computer_wins == necessary_wins:
                    break

        if player_wins > computer_wins:
            print(f' Congratulations contestant number {number} You may continue to the next game')
            game_two_intro()
        else:
            print(f'I win. You will now be eliminated. \n\n')
        game_over()
    
    def game_two_intro():
        global number1
        global number
        global name
        print(f"Welcome to the second game. You are contestant {number} {name}. We will be playing a game of chance.\n")
        game_two()
        
    def game_two():
        print(
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
        
        print("You have been assigned another contestant to play against.\n")
        print("You will have 5 chances to roll the dice each\n")
        print("The person with the highest number wins each round\n")
        print("You have to win 3 rounds out of 5 to continue\n")
        print("The loser will then be eliminated\n")
        print("Good luck\n \n")
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
            print(f"You rolled:", player1_value)
                
            print(f"Contestant {number1} rolled:", player2_value)

        # Selection: based on comparison of the values, take the appropriate path through the code.
            if player1_value == player2_value:
                print("Draw, no winner.\n")
                print("Next round")
            elif player1_value > player2_value:
                print(f"\nYou win this round.\n")
                player1_score = player1_score + 1  # This is how we increment a variable
                print(f"Your score is {player1_score}")
                print(f"Contestant {number1}'s score is {player2_score}")
                input("\nPress enter to roll again ")
                if player1_score >= 5:
                    print(f"Congratulations contestant {number}, you may continue\n")
                    print("Your score was:", player1_score)
                    print(f"Contestant {number1} score:", player2_score)
                    input("\nPress enter to continue ")
                    congratulations()
            elif player2_value > player1_value:
                print(f"\nContestant {number1} wins this round\n")
                player2_score = player2_score + 1
                print(f"Your score is {player1_score}")
                print(f"Contestant {number1}'s score is {player2_score}")
                input("\nPress enter to roll again ")
                if player2_score >= 7:
                    print("Your score was:", player1_score)
                    print(f"Contestant {number1} score:", player2_score)
                    print(f"You lose contestant {number}. You will now be eliminated")
                    input("\nPress enter to continue ")
                    game_over()
            else:
                print("""
                      
                      ==========================
                      |  THERE CAN BE NO DRAW  |
                      ==========================
                      
                      
                      \n""")
                game_two_start()
                
        
    def congratulations():

        print("""
                 db    db  .d88b.  db    db   db   d8b   db d888888b d8b   db
                 `8b  d8' .8P  Y8. 88    88   88   I8I   88   `88'   888o  88
                 `8bd8'  88    88 88    88   88   I8I   88    88    88V8o 88
                    88    88    88 88    88   Y8   I8I   88    88    88 V8o88
                     88    `8b  d8' 88b  d88   `8b d8'8b d8'   .88.   88  V888
                     YP     `Y88P'  ~Y8888P'    `8b8' `8d8'  Y888888P VP   V8P
                  
                  """) 
            
        winnings = random.randint(2773411000, 5283211000)
        print(f"You won a grand total of £{winnings}")
        print("And your life")
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
        print("""
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
                    
                            
                            
                            
                            
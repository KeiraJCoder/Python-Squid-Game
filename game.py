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
            if answer.lower()=="yes":
                character() 
            elif answer.lower()=="no":
                print("You know where we are if you change your mind")
                exit 
            else:
                print("Okay then.")
                exit() 
                               
    def character():
            global name
            global number
            name=input("What is your name? ")
            person= input("Choose 1, 2 or 3 ") 
            number=random.randint(1,456)
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
                game()
            game_start()
            
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
                    print('Computer wins, rock smashes scissors')
                    computer_wins += 1
                elif player == 'scissors' and computer == 'paper':
                    print('You win, scissors cut paper')
                    player_wins += 1

                if player_wins == necessary_wins or computer_wins == necessary_wins:
                    break

        if player_wins > computer_wins:
            print(f' Congratulations contestant number {number} You may continue to the next game')
            game_two()
        else:
            print(f' I win. You will now be eliminated. ')
        game_over()
        
        
    def congratulations():
            global congratulations  
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
    
    
            # red light green light 
    
    def game_two():
        game_two() 
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
                    
                            
                            
                            
                            
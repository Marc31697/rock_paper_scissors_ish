import random

class game():

    def __init__(self, player_wins = 0, player_losses = 0):
        self.player_wins = player_wins
        self.player_losses = player_losses
    
    def getPlayerRoll():
        r = input("\nRock, paper, or scissors? ")
        return r
    
    def getComputerRoll():
        key = random.randint(1,3)

        if key == 1:
            return 'Rock'
        elif key == 2:
            return 'Paper'
        else:
            return "Scissors"
    
    def getPlayerDirection():
        r = input("\nLeft, Right, Up, or Down? ")
        return r
    
    def getComputerDirection():
        key = random.randint(1,4)

        if key == 1:
            return 'Right'
        elif key == 2:
            return "Left"
        elif key == 3:
            return 'Up'
        else:
            return 'Down'
    
    def determineWinner(self):
        player = game.getPlayerRoll()
        computer = game.getComputerRoll()
        points = 0

        if player.lower() == 'rock' and computer.lower() == 'scissors':
            points += 1
            print('\nYou win the first round! Rock beats scissors!')
        elif player.lower() == 'rock' and computer.lower() == 'paper':
            points += 2
            print('\nYou lose the first round. Rock loses to paper!')
        elif player.lower() == 'paper' and computer.lower() == 'scissors':
            points += 2
            print('\nYou lose the first round. Paper loses to scissors!')
        elif player.lower() == 'paper' and computer.lower() == 'rock':
            points += 1
            print('\nYou win the first round! Paper beats rock!')
        elif player.lower() == 'scissors' and computer.lower() == 'rock':
            points += 2
            print('\nYou lose the first round. Scissors loses to rock!')
        elif player.lower() == 'scissors' and computer.lower() == 'paper':
            points += 1
            print('\nYou win the first round! Scissors beats paper!')
        elif player.lower() == computer.lower():
            print('\nDraw!')
            return
        
        player = game.getPlayerDirection()
        computer = game.getComputerDirection()

        if player.lower() == computer.lower():
            points += 1
        else:
            print('\n\nMissed!')
            return

        if points == 2:
            print("\nYou win this round!")
            self.player_wins += 1
        elif points == 3:
            print("\nI win this round!")
            self.player_losses += 1
        
    def retrieveScore(self):
        print(f'\nHere is the score!\nPlayer: {self.player_wins}\nMy Wins: {self.player_losses}')


        

# Run the game
def run():
    newGame = game()
    print("\nWelcome to the most exciting game of rock, paper, scissors yet!\n")
    print("This game is going to be a little different...Instead of rock, paper, scissors - We will be playing variant with a little bit of a twist.\n")
    print("The game is called 'ISH' and the rules are simple. After winning the initial round, there will be an extra step.\n")
    print("For the second step, you will be choosing a direction (left, right, up, down), if you and the opponent pick the same direction, you win!\n")
    print("Basically you will need to win both rounds in a row in order to get a point. Good Luck!\n")

    while True:
        newGame.determineWinner()
        r = input("Type 'Quit' to leave the game, 'Score' to see the current score, or press enter to continue. ")
        if r.lower() == 'quit':
            break
        elif r.lower() == 'score':
            newGame.retrieveScore()

    newGame.retrieveScore

run()
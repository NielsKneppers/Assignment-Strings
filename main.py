# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#### THIS IS PART 1 OF THE EXERCISE###
name_scorer = "Ruud Gullit" # the name of scorer 1
name_scorer2 = "Marco van Basten"  # the name of scorer 2
goal_0 = 32 # the first goal was in de 32nd minute of the game
goal_1 = 54 # the second goals in in the 54th minute of the game 
scorers = name_scorer + " " + str(goal_0) + ", " + name_scorer2 + " " + str(goal_1) #making a string with the scorers and corresponding minutes of the goals
report = F"{name_scorer} scored in the {goal_0}nd minute\n{name_scorer2} scored in the {goal_1}th minute" #making a variable report inwhere the players and minutes are placed

### THIS IS PART 2 OF THE EXERCICE###
# one of the players name is Ruud Gullit
player = 'Ronald Koeman'  # the name of one of the players during the game
first_name = player[0:player.find(' ')] # isolating the first name of the player
last_name_len = len(player[player.find(' ') + 1:]) # isolating the last name of the palyer and show how many characters they are
name_short = str(player[0] + '. ' + player[player.find(' ') + 1:]) # Writing the name of the player in the format: R. Koeman
chant = (first_name + '! ') * (len(first_name) - 1) + (first_name + '!') # multiple the first name of the player 5 times and removing the last space
good_chant = chant[-1] != ' ' # to check if the last character isn't a space






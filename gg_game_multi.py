# Glupska grisen
# Ante, Teo Elmfeldt
from random import randint

def rand_dice(n): # generates a random number, remember to put n = 1 when calling
    return randint(n, 6)  # to be able to exclude 1 as a possibility


def one_round():
    total_this_round = 0
    current_dice_value = rand_dice(2) 
    print "\nFirst strike: %d" % current_dice_value
    
    players_still_playing = True #long (good) names help the reader of the code
    while players_still_playing: # loop as long as you want to
        players_still_playing = False #We set this to True if someone continue
        total_this_round += current_dice_value
        print "Total this round is : %d" % total_this_round
        
        for player in players: #take out the players from the list
            if current_dice_value != 1:
                if player['playing']: #the player is still in the game
                    player['currentScore'] += current_dice_value
                    ans = raw_input("%s, press ENTER to strike again (anything else to save)>" % player['name']) #get the name from the player 
                    if ans == "":
                        players_still_playing = True #At least this player is still in the game, we should do an other round
                    else:
                        save_player_points(player)
            else:
                if player['playing']:
                    print player['name'] + ", You lost the points for this round"
                    player['currentScore'] = 0 #set the players score to 0
                    save_player_points(player) #save that zero 
                
        current_dice_value = rand_dice(1) # save return value of one_strike() to current_dice_value
        print "\nNew strike: %d" % current_dice_value
        
        

def restart_players(players):
    for player in players:
        player['playing'] = True
        print "\n", player['name'] + ':'
        print "This is your score: ", player['score'], ' total: ', sum(player['score']) 
        
        
def save_player_points(player):
    player['score'].append(player['currentScore'])
    player['currentScore'] = 0
    player['playing'] = False

def save_list(t, points): # called to save the result to list
    print "Adding %d to total sum." % t
    points.append(t)
    s = 0
    #print "You've got %r points" % points
    for count in points:
        #print "Here are your totals: %d" % count
        s += count
    print "Points now: ", points
    print "Overall total: %d\n" % s


i = 0
rounds = int(raw_input("How many rounds? ")) # ask for how many turns to run
players = []
points = []
enterPlayers = True
while enterPlayers:
    name = raw_input("Player name: ")
    players.append({'name': name, 'score': [], 'currentScore': 0, 'playing': True}) #add a new player object to the list of players
    more = ''
    while more != 'Y' and more != 'n':
        more = raw_input("Add more players ? (Y/n):")
    enterPlayers = more =='Y' #This is a one liner istead of using a if statement
    
while i < rounds: # runs until specified amount of time
    one_round()
    restart_players(players)
    i += 1

print "\nThat's great!"
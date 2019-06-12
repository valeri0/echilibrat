from copy import deepcopy

# function used to get the total ranking of a team
# aka the sum of all the rankings
calculate_team_score = lambda team: sum(tup[1] for tup in team)



def distribute_players_to_teams(players):

    # Initialize each team with an empty list

    team_1 = []
    team_2 = []



    # Sort the input players descending by their ranking
    sorted_players = sorted(players,key=lambda tup:tup[1],reverse=True)


    # add the top 2 players in a separate team
    best_player = sorted_players[0]
    second_best_player =sorted_players[1]




    team_1.append(best_player)
    team_2.append(second_best_player)

    # remove them from the sorted list of players
    sorted_players.remove(best_player)
    sorted_players.remove(second_best_player)


    # Once the top two players are allocated to a team, then we will go to the remaining players in descending order of their rank and will
    # allocate them to a team based on the equality of the updated ranking of the two teams
    #
    # Let's say we have team_1 = [('A',10)] and team_2 = ['B',9'] and the remaining players are  = [('C',6),('D',5')]
    #
    # Solution 1:
    # team_1 = [('A',10'),('C',6)] => score: 16
    # team_2 = [('B',9),('D',5)] => score: 14
    #
    # Solution 2:
    # team_1 = [('A',10'),('D',5)] => score: 15
    # team_2 = [('B',9),('C',6)] => score: 15
    #
    # Based on the simulated teams above we will decide to go forward with Solution 2 since the difference between the ranking is closest to 0 (it's even 0 in this case)

    while sorted_players != []:

        # if there is only one remaining player, he will be allocated to the team with lower ranking:
        if len(sorted_players) == 1:
            if calculate_team_score(team_1) < calculate_team_score(team_2):
                team_1.append(sorted_players[0])
                sorted_players.remove(sorted_players[0])


            else:
                team_2.append(sorted_players[0])
                sorted_players.remove(sorted_players[0])

        else:



            # copy the existing teams to auxiliary variables
            team_1_aux = deepcopy(team_1)
            team_2_aux = deepcopy(team_2)


            # Simulate first allocation
            team_1_aux.append(sorted_players[0])
            team_2_aux.append(sorted_players[1])


            # Calculate the difference between the two teams
            difference_between_teams_in_first_allocation = abs(calculate_team_score(team_1_aux)-calculate_team_score(team_2_aux))


            # Reset auxiliary variables to the current teams
            team_1_aux = deepcopy(team_1)
            team_2_aux = deepcopy(team_2)

            # Simulate second allocation
            team_1_aux.append(sorted_players[1])
            team_2_aux.append(sorted_players[0])


            # Calculate again the difference between the two teams
            difference_between_teams_in_second_allocation = abs(calculate_team_score(team_1_aux)-calculate_team_score(team_2_aux))


            # Which allocation has the difference between team closest to 0, that is the correct one
            if difference_between_teams_in_first_allocation < difference_between_teams_in_second_allocation:
                team_1.append(sorted_players[0])
                team_2.append(sorted_players[1])

            else:
                team_1.append(sorted_players[1])
                team_2.append(sorted_players[0])


            # Remove the players which were allocated in this iteration
            sorted_players.remove(sorted_players[0])
            sorted_players.remove(sorted_players[0])



    return team_1,team_2

def display_team(team):
    for player in team:
        print "{} --- {}".format(player[0],player[1])

def main():
    # Input players which is represented by a list of tuples containing: (Name, Ranking)

    players = [
        ('Costros', 4),
        ('Catalin', 10),
        ('Ciprian', 7),
        ('Silviu', 7),
        ('Valerio',4),
        ('Ionut',5),
        ('Luci',9),
        ('Capitanu',6),
        ('Anatolii',7),
        ('Cozma',4),
        ('Robert',6),
        ('Ifrim',9),
        ('Alin',7),
        ('George',4),
        ('Iulica',4),
        ('Sergiu',8)



    ]

    team_1,team_2 = distribute_players_to_teams(players)

    print "Team A\nScore: "+str(calculate_team_score(team_1))
    display_team(team_1)


    print "--------------------------"
    print "--------------------------"

    print "Team B\nScore: "+str(calculate_team_score(team_2))
    display_team(team_2)

main()
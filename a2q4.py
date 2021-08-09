"Raimbek Nussipkhozhin, NFU892, 11313819, Jeffrey Long"
"Question 4"
n_games = int(input("Enter the number of games played: "))
time_per_game = float(input("Enter the average length of a game (in minutes): "))
tips = float(input("Enter the amount of tips you received: "))
n_players = int(input("Enter the amount of players escorted: "))
price_per_player = float(input("Enter the charging price per player: "))
def time(n_games, time_per_game):
    """
    This function computes the total time spent playing Fortnite
    n_games: an integer of the number of played games
    time_per_game: a float for the average length of the game
    total_time: a float for the total time spent
    returns: the total time
    """
    total_time = n_games * time_per_game / 60
    return total_time
def revenue(tips, n_players, price_per_player):
    """
    This function computes the total revenue
    tips: a float for the amount of money received in tips
    n_players: an integer of the number of players escorted
    price per player: a float for the price charged per person
    total_revenue: a float for the total amount of money received
    returns: the total revenue
    """
    total_revenue = tips + price_per_player * n_players
    return total_revenue
def rate_of_pay():
    """
    This function computes the rate of pay
    x: a float for the rate of pay
    revenue(tips, n_players, price_per_player): a float function that represents a total revenue
    time(n_games, time_per_game): a float function that represents the total time spent
    returns: the rate of pay
    """
    x = revenue(tips, n_players, price_per_player) / time(n_games, time_per_game)
    return x
print ("Revenue: $" + str(revenue(tips, n_players, price_per_player)))
print ("Total Time (in hours): " + str(time(n_games, time_per_game)))
print ("Pay Rate: $" + str(rate_of_pay()))
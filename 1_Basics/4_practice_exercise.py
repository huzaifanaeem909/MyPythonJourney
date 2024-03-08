""" Write a Python program to add two numbers entered by the user. """

num_1 = float(input("enter first number="))
num_2 = float(input("enter seccond number="))
sum = num_1 + num_2
print(f"The sum of two numbers entered by user is = {sum}")

""" Write a Python program to calculate the average of three numbers entered by the user. """

num_1 = float(input("enter first number="))
num_2 = float(input("enter second number="))
num_3 = float(input("enter third number="))
average = (num_1 + num_2 + num_3) / 3
print(f"The average of entered number are = {average}")

""" Ask number of games played in a tournament. Ask the user number of games won and number of games loss. Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points) """

game_played = int(input("Number of Games played="))
game_won = int(input("Total Games Won="))
game_lost = int(input("Total Game Loss="))
game_tie = game_played - game_won - game_lost
print(f"Total game tie = {game_tie}")
total_points = (game_won * 4) + (game_tie * 2)
print(f"Total points = {total_points}")

# Pay rate

## Description

Siblings John and Jane want to buy their first dog, sadly, COVID has made selling lemonade difficult. Fortunately, both John and Jane are excellent Fortnite players, and have started charging other players to carry them to victory. However, they weren’t sure about what their hourly rate of pay was.

## Problem description

The task is to write a Python program that calculates and displays the hourly pay rate for the youths after taking their effort into consideration. To accomplish this, three Python functions are needed: time, revenue, and rate_of_pay.

The time function should take parameters n_games (the number of games played), time_per_game (average length of a game in minutes), and return the total time spent playing Fortnite. The total time is:

![image](https://user-images.githubusercontent.com/86201781/128758730-2969e7b0-d34c-41e3-86e6-6f9b4e711cde.png)

The revenue function should take parameters tips (the amount of money donated by grateful players),
n_players (the number of players escorted), price_per_player (the selling price for carrying one player) and return the total amount of money earned. The total money earned is:

![image](https://user-images.githubusercontent.com/86201781/128758792-eda666df-7c8f-4f0b-82a5-8c8f1d8a4579.png)

The rate_of_pay function determines the net profit (net money earned) by the youth. It should:
- call time and revenue and use their return values to compute the rate of pay earned by the siblings;
- return the rate of pay for each sibling in dollars per hour.

The parameters of the rate_of_pay function should be chosen so that they provide the necessary information required to call the time and revenue functions. The rate of pay is:

![image](https://user-images.githubusercontent.com/86201781/128758853-cc262d02-7252-4439-b00c-c2e5f1852dc0.png)

Here is an example of how the program’s console output might look. Green text was entered by the user;
blue text came from data returned by the function.

![image](https://user-images.githubusercontent.com/86201781/128758905-fb7a4d57-d3a9-454f-801e-d5595d8f3740.png)

## How to use

Here are the steps for how to open, use and utilize the program:

First, download all of the files listed above;
Put all the files in one folder;
Open the file Projec_pr.py;
The program will open a command console which will ask you to input the number of games, average lenght of the game, number of players, the cost of service, and total tips.

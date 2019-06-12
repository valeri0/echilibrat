# echilibrat
A little project for distributing players based on their ranking in two (almost) equally teams

# Purpose:

Given the following list of tuples, in which a tuple consists of ```('Player Name', Ranking)```, the script will distribute players in two (almost) equally ranked teams.

# How to run:

1. Fill in the players array with the necessary tuples:
```
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
```
2. Run the python script :)
3. You should observe the results displayed in the console:
```
Team A
Score: 50
Catalin --- 10
Sergiu --- 8
Silviu --- 7
Alin --- 7
Robert --- 6
Costros --- 4
Cozma --- 4
Iulica --- 4
--------------------------
--------------------------
Team B
Score: 51
Luci --- 9
Ifrim --- 9
Ciprian --- 7
Anatolii --- 7
Capitanu --- 6
Ionut --- 5
Valerio --- 4
George --- 4
```

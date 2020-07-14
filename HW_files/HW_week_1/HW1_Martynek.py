#!/usr/bin/python2.7

#The goal of this script is to take in the files that have the list of choices made by player 1 and player 2 in their 100 games of rock, paper, scissors and return a file that has the result of each of the 100 games. please make sure the output file is called "" a list of game results that are "\n" delimited.

#We have provided you the input files for player 1 and player 2 on the course Github account and we would like you to use the functions in this file to complete this coding assignment.

#The player choices are in the form of a string for each round of "R", "P", or "S" (rock, paper, or scissors) separated by "\n"

#The file2List function is designed to take the data files from player 1 and player 2 and convert them to a list data structure.

def file2List():
	player_1 = open("player1Choices.txt", "r")
	content = player_1.read()
	#print(content)

	player_1_list = content.split("\n")
	player_1.close()

	#print(player_1_list)

	player_2 = open("player2Choices.txt", "r")
	content_2 = player_2.read()
	#print(content)

	player_2_list = content_2.split("\n")
	player_2.close()

	#print(player_2_list)

	return player_1_list, player_2_list

#The compareChoices function is designed to take in a choice string from player 1 and a choice string from player 2 and assess what the result of each game was.
#If player 1 won it should return the string "P1"
#If player 2 won it shold return the string "P2"
#If the players tied it should return the string "tie"
def compareChoices(data):
	# print data[1]
	p1data = data[0]
	p2data = data[1]
	for p1, p2 in zip(p1data, p2data):

		if str(p1) == "R" and str(p2) == "S":
			print "P1"
		elif str(p1) == "R" and str(p2) == "P":
			print "P2"
		elif str(p1) == "R" and str(p2) == "R":
			print "tie"
		elif str(p1) == "S" and str(p2) == "S":
			print "tie"
		elif str(p1) == "S" and str(p2) == "P":
			print "P1"
		elif str(p1) == "S" and str(p2) == "R":
			print "P2"
		elif str(p1) == "P" and str(p2) == "P":
			print "tie"
		elif str(p1) == "P" and str(p2) == "R":
			print "P1"
		elif str(p1) == "P" and str(p2) == "S":
			print "P2"


	pass

#You need a main function for all python scripts please use the main function to organized the other functions of this script.
def main():
	
	compareChoices(file2List())
	pass

if __name__ == "__main__":
    main()

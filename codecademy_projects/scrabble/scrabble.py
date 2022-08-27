# Python 3 (Coded 2021)
# Use dictionaries to organize players, words, and points from data from a group of friends playing scrabble. 


# There are two lists, _letters_ and _points_ and then dictionary called _letter_to_points_ that maps each letter to its point value.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Dictionary with zip comprehension:
letters_to_points = {
  key: value
  for key, value
  in zip(letters, points)
  }
#print(letters_to_points)


# There is no key:value to account for blank tiles, so we add an element with a key of " " and a point value of 0
letters_to_points[" "] = 0
print(letters_to_points)


# function _score_word_ that will take in a word and return how many points that word is worth.

def score_word(word):
  point_total = 0
  for letter in word.upper():
    point_total += letters_to_points.get(letter,0)
  return point_total

brownie_points = score_word("Brownie")
print(brownie_points) # 15 points



# Dictionary _player_to_words_ maps players to a list of the words they have played. 

player_to_words = {
  "player1" : ["BLUE", "TENNIS", "EXIT"],
  "wordNerd" : ["EARTH", "EYES", "MACHINE"],
  "Lexi Con" : ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}
#print(player_to_words["player1"])

# Empty dictionary _player_to_points will be filled with a _player_ value as key and a value of _player_points_ with a loop (right below).
player_to_points = {}



# Iterate through the items in player_to_words. Each player is _player_ and each list of words is _words_. 
# Within the loop, a variable called player_points (set to 0) will add the score per word passed for another loop within the loop wit word as input.

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player]= player_points
  #print (player, player_points)

#print(player_to_words)

for player, total_points in player_to_points.items():
  print (player, total_points)


# REF: https://www.youtube.com/watch?v=WjVJcCBazNI
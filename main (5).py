'''Implement a class called player that represents a cricket player.The player class should have a method called play() Which prints"The player is playing cricke.
Derive two classes, Batsman and bowler, from the player class.Override the play() method in each derived class to print"The batsman is batting and"The bowler is bowling", respectively.
write a program to create objects of both the Batsman and bowler classes and call the play() method for each object.'''
#Define the base class player
class Player:
  def play(self):
    print("The Player is playing cricket.")

#Define the derived class Batsman
class Batsman(Player):
  def play(self):
    print("The Batsman is batting.")

#Define the derived class Bowler
class Bowler(Player):
  def play(self):
    print("The Bowler is bowling.")

#Create Objects of Batsman and Bowler classes
batsman=Batsman()
bowler=Bowler()

#Call the play() method for each Object
batsman.play()
bowler.play()
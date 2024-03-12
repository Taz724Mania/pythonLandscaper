import sys

player = {
    "money": 0,
    "tool": 0
}

tools = [
    {"name": "teeth", "price": 0, "earns": 1},
    {"name": "scissors", "price": 5, "earns": 5},
    {"name": "push-mower", "price": 25, "earns": 50},
    {"name": "electric-mower", "price": 250, "earns": 100},
    {"name": "students", "price": 500, "earns": 250},
]

def getInput():
    result = input("You may [m]ow, [u]pgrade, or [c]lose. Choose one: ")

    if(result == "m"):
        earnMoney()
        
    
    if(result == "u"):
        upgradeTools()
        
    
    if(result == "c"):
        close()
        
    print("Choose a valid option")

    getInput()


def earnMoney():

    print(f"You mowed a lawn and earned ${tools[player["tool"]]["earns"]}!")

    player["money"] += tools[player["tool"]]["earns"]

    print (f"You now have ${player["money"]}")

    getInput()


def upgradeTools():
    # check how much money the player has
    player_money = player["money"]
    # check which tool the player has
    player_tool = player["tool"]
    # write an if statement that checks if there is enough money to buy the tool and if there is they buy and upgrade, but if not, a womp womp message is returned
    if player_money >= tools[player_tool + 1]["price"]:
       # subtract the cost from player money 
       player_money -= tools[player_tool + 1]["price"]
       player_tool += 1
       print(f"You bought a {tools[player_tool]["name"]}!")
    else:
       if player_money < tools[player_tool + 1]["price"]:
          print("You don't have enough money for that!")

    getInput()


def close():

    print("Goodbye!")

    sys.exit()


def win():
  
  if player["money"] == 1000 and tools[player["tool"]]["name"] == "students":

    return "You have won! Congratulations!"
  
  else:

    print("You haven't won yet! Keep on mowing!")

    getInput()


getInput()
import sys

player = {
    "money": 0,
    "tools": 0
}

tools = [
    {"name": "teeth", "price": 0, "earns": 1},
    {"name": "scissors", "price": 5, "earns": 5},
    {"name": "push-mower", "price": 25, "earns": 50},
    {"name": "electric-mower", "price": 250, "earns": 100},
    {"name": "students", "price": 500, "earns": 250},
]

def getInput():
    result = input("You may [m]ow, [u]pgrade, [r]eset, or [c]lose. Choose one.")

    if(result == "m"):
        earnMoney()
        
    
    if(result == "u"):
        upgradeTools()
        
    
    if(result == "r"):
        reset()
        
    
    if(result == "c"):
        close()
        
    
    print("Choose a valid option")

    getInput()

def earnMoney():

    print(f"You mowed a lawn and earned ${tools[player["tools"]]["earns"]}!")

    player["money"] += tools[player["tools"]]["earns"]

    print (f"You now have {player["money"]}")

    win()

    getInput()


def upgradeTools():
  
  if player["money"] < tools[player["tools"]]["price"]:

    print(f"You have purchased a new tool!")

    player["tools"] += 1

    print(f"You now have {tools[player['tools']]['name']}")

    win()

  else:

    print("You don't have enough money for that! Mow more lawns to earn more money!")

    getInput()


def reset():

    print("You've restarted the game. Time to get mowing!")

    player["money"] == 0

    tools[player["tools"]] == 0

    getInput()


def close():

    print("Goodbye!")

    sys.exit()


def win():
  
  if player["money"] == 1000 and tools[player["tools"]]["name"] == "students":

    return "You have won! Congratulations!"
  
  else:

    print("You haven't won yet! Keep on mowing!")
    
    getInput()


getInput()
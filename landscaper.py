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
    result = input("You may [m]ow, [u]pgrade, or [r]eset")

    if(result == "m"):
        earnMoney()
        return 1
    
    if(result == "u"):
        upgradeTool()
        return 2
    
    if(result == "r"):
        reset()
        return 3
    
    print("choose a valid option")
    getInput()


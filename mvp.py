import pickle
userData = None

class Schema():
    def __init__(self):
        self.grandparents = {}
        
    def addIncomeSource(self, sourceName, amount):
        self.grandparents[sourceName] = {
                "amount": amount,
                "accounts": {},
                "remaining":amount
                }


    def addAccount(self, grandparent, name, weight):
        identifier = weight[0]
        remaining = self.grandparents[grandparent]["remaining"]
        amount = self.grandparents[grandparent]["amount"]
       
        if name != "savings":
            takeFromRemainingOrTakeFromSrc = input("Take from income source total or what is left over?(src/l): ")
        else:
            takeFromRemainingOrTakeFromSrc = "src"
        if takeFromRemainingOrTakeFromSrc == "src":
            if identifier == 'f':
                val = float(weight[1:])
                self.grandparents[grandparent]["accounts"][name] = {"weight":weight, "srcOrLeft":takeFromRemainingOrTakeFromSrc, "weight value": val, "current":val, "children":{}}
                self.grandparents[grandparent]["remaining"] = remaining - val
            elif identifier == '%':
                val = amount * (float(weight[1:])/100)
                self.grandparents[grandparent]["accounts"][name] = {"weight":weight, "srcOrLeft":takeFromRemainingOrTakeFromSrc, "weight value":val, "current":val, "children":{}}
                                                                                                                                         
         

        elif takeFromRemainingOrTakeFromSrc == 'l':
            if identifier == 'f':
                val = float(weight[1:])
                self.grandparents[grandparent]["accounts"][name] = {"weight":weight, "srcOrLeft":takeFromRemainingOrTakeFromSrc, "weight value": val, "current":val, "children":{}}
                self.grandparents[grandparent]["remaining"] = remaining - val
            elif identifier == '%':
                val = remaining * (float(weight[1:])/100)
                self.grandparents[grandparent]["accounts"][name] = {"weight":weight, "srcOrLeft":takeFromRemainingOrTakeFromSrc, "weight value":val, "current":val, "children":{}}
        


        self.grandparents[grandparent]["remaining"] = remaining - val
                                                                                                                                    

    def addCategory(self, grandparent, parent, child, weight):
        identifier = weight[0]
        amount = self.grandparents[grandparent]["accounts"][parent]["current"]
        val = float(weight[1:])

        self.grandparents[grandparent]["accounts"][parent]["children"][child] = {"weight":weight, "weight value":val, "current":val, "children":{}}

        self.grandparents[grandparent]["accounts"][parent]["current"] = amount - val


    def check(self):
        print()
        print()
        print(self.grandparents)
        print()
        print()
        for grandparent in self.grandparents:
            print("==================================================")
            print("Grandparent: ", grandparent)
            print("Amount:", self.grandparents[grandparent]["amount"])
            print("Remaining:", self.grandparents[grandparent]["remaining"])
            

            for parent in self.grandparents[grandparent]["accounts"]:
                print(parent)
            print()
            print("==================================================")
            print() 
        print(                                                   )       



    def getSources(self):
        return [key for key in  self.grandparents]

def save():
    with  open("finances", "wb") as f:    
        pickle.dump(userData, f)

def loadUserdata():
    global userData
    try:
        with open("finances", "rb") as f:
            userData =  pickle.load(f)
    except FileNotFoundError:
        print("no current save file")
        userData = Schema()



def main():
    global userData
    status = True

    print("""
1. Add recurring income source
2. Add Account
3. Add Category
4. Check

-1. exit
         """) 
    choice = input("What do you want to do? ")
    match choice:
        case '-1':
            status = False
        case '1':
            incomeSrcName = input("input name: ")
            amount = float(input("Input amount: "))
            userData.addIncomeSource(incomeSrcName, amount)
            savingsBool = input("Do you want a savings account with this income source? (y/n): ")
            if savingsBool == 'y':
                flatOrPercentage = input("Flat or percentage for savings account? (f/p)")
                if flatOrPercentage == 'f':
                    flatAmt = 'f' + input("Input flat amount: ")
                    userData.addAccount(incomeSrcName, "Savings", flatAmt)
                elif flatOrPercentage == 'p':
                    percentage = '%' + input("Input percentage of amount to add to savings: ")
                    userData.addAccount(incomeSrcName, "Savings", percentage)

        case '2':
            inputSources = userData.getSources()
            incomeSrcName = input(f"Input name of input source{inputSources}: ")
            accountName = input("Input name of new account: ")
            flatOrPercentage = input("Flat or percentagefor account? (f/p)")
            if flatOrPercentage == 'f':
                weight = 'f' + input("Input flat amount")
            elif flatOrPercentage == 'p':
                weight = '%' + input("Input percentage of amount to go to this account: ")
            userData.addAccount(incomeSrcName, accountName, weight)
        case '3': 
            grandparent = input("input name: ")
            parent = input("Input name of new account: ")
            child = input("Input name of category to create: ")
            flatOrPercentage = input("Flat or percentage for category? (f/p)")
            if flatOrPercentage == 'f':
                weight = 'f' + input("Input flat amount")
            elif flatOrPercentage == 'p':
                weight = '%' + input("Input percentage of amount to go to this category: ")
            userData.addCategory(grandparent, parent, child, weight):
        case '4':
            userData.check()
    save()
    return status



#start    
if __name__ == "__main__":
    status = True
    if userData == None:
        loadUserdata()
    while(status):
        status = main()
        print(status)


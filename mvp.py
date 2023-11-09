import pickle
userData = None

class Schema():
    #constructor
    def __init__(self):
        self.grandparents = {}
    
    #method to add income source
    def addIncomeSource(self, sourceName, amount):
        self.grandparents[sourceName] = {
                "amount": amount,
                "accounts": {},
                "remaining":amount
                }

    #method to add account
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
                self.grandparents[grandparent]["remaining"] = remaining - val

        elif takeFromRemainingOrTakeFromSrc == 'l':
            if identifier == 'f':
                val = float(weight[1:])
                self.grandparents[grandparent]["accounts"][name] = {"weight":weight, "srcOrLeft":takeFromRemainingOrTakeFromSrc, "weight value": val, "current":val, "children":{}}
                self.grandparents[grandparent]["remaining"] = remaining - val
            elif identifier == '%':
                val = remaining * (float(weight[1:])/100)
                self.grandparents[grandparent]["accounts"][name] = {"weight":weight, "srcOrLeft":takeFromRemainingOrTakeFromSrc, "weight value":val, "current":val, "children":{}}
        

        if name == 'savings':
            self.grandparents[grandparent]["remaining"] = self.grandparents[grandparent]["ammount"] - val
        else:
            self.grandparents[grandparent]["remaining"] = remaining - val
                                                                                                                            
    #method to add category                                                                                                                        
    def addCategory(self, grandparent, parent, child, weight):
        identifier = weight[0]
        takeFromRemainingOrTakeFromSrc = input("Take from income source total or what is left over?(src/l): ")
        amount = self.grandparents[grandparent]["accounts"][parent]["weight value"] 
        remainder = self.grandparents[grandparent]["accounts"][parent]["current"]
        
        if takeFromRemainingOrTakeFromSrc == "src":
            if identifier == 'f':
                val = float(weight[1:])
            elif identifier == '%':
                val = float(weight[1:]) * amount / 100


        elif takeFromRemainingOrTakeFromSrc == 'l':

            if identifier == 'f':
                val = float(weight[1:])
            elif identifier == '%':
                val = float(weight[1:]) * remainder / 100

        self.grandparents[grandparent]["accounts"][parent]["current val"] = remainder - val
            
        self.grandparents[grandparent]["accounts"][parent]["children"][child] = {"weight":weight, "weight value":val, "current":val, "children":{}}


    #method to check account data
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



    #get all keys from sources
    def getSourcesList(self):
        return [key for key in  self.grandparents]

    #method to get parent keys
    def getParentsList(self, grandparent):
        return [key for key in self.grandparents[grandparent]["accounts"]]

    #method to get children data
    def getChildrenList(self, grandparent, parent):
        return [key for key in self.grandparents[grandparent]["accounts"][parent]["children"]]

    #method to get all grandchildren keys
    def getGrandChildrenList(self, grandparent, parent, child):
        return [key for key in self.grandparents[grandparent]["accounts"][parent]["children"][child]["children"]]
    
    #method to get all grandchildre information
    def getGrandChildData(self, grandparent, parent, child, grandchild):
        return self.grandparents[grandparent]["accounts"][parent]["children"][child]["children"][grandchild]        

    #method to add purchase
    def addPurchase(self):
        grandparent = input(f"Which income source do you want to spend from?{userData.getSourcesList()}: ")
        
        parent = input(f"Which account  do you want to spend from?{userData.getParentsList(grandparent)}: ")
        children = userData.getChildrenList(grandparent, parent)
        typeOfPurchase = input(f"Input type of purchase {children}: ")
        name = input("Purchase: ")
        cost = float(input("Cost: "))
        current = self.grandparents[grandparent]["accounts"][parent]["children"][typeOfPurchase]["current"]
        #use newCurrent to check for out of budget later on
        newCurrent = current - cost 
        description = input("Description of purchase: ")

        entry = {name, cost, description}
    
        confirm = input("Confirm purchase(y/n): ")
        if confirm == 'y':
            self.grandparents[grandparent]["accounts"][parent]["children"][typeOfPurchase]["children"][name] = entry  
            self.grandparents[grandparent]["accounts"][parent]["children"][typeOfPurchase]["current"] = newCurrent 
            self.grandparents[grandparent]["accounts"][parent]["current"] = self.grandparents[grandparent]["accounts"][parent]["current"] - cost
            self.grandparents[grandparent]["remaining"] =  self.grandparents[grandparent]["remaining"] - cost 
        else:
            print("rip")


    #method to traverse tree and show traversal
    def traverseTree(self):
        dct = {}
        grandparents = userData.getSourcesList()
        for grandparent in grandparents:
            parents = userData.getParentsList(grandparent)
            for parent in parents:
                children = userData.getChildrenList(grandparent, parent)
                for child in children:
                    grandChildren = userData.getGrandChildrenList(grandparent, parent, child)
                    for grandChild in grandChildren:
                        print(grandparent, " -> ", parent, " -> ", child, " -> ", grandChild, " -> ", userData.getGrandChildData(grandparent, parent, child, grandChild))
                        dct[grandChild] = [grandparent, parent, child]
        return dct
   

   #method to remove purchase
    def removePurchase(self, dct):
        items = [x for x in dct]
        toRemove = input(f"Which item to remove {items}")
        grandparent = dct[toRemove][0]
        parent = dct[toRemove][1]
        child = dct[toRemove][2]


        del self.grandparents[grandparent]["accounts"][parent]["children"][child]["children"][toRemove]



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
4. Add purchase
5. Traverse Tree
6. Remove item
9. Check


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
                flatOrPercentage = input("Flat or percentage for savings account? (f/p): ")
                if flatOrPercentage == 'f':
                    flatAmt = 'f' + input("Input flat amount: ")
                    userData.addAccount(incomeSrcName, "Savings", flatAmt)
                elif flatOrPercentage == 'p':
                    percentage = '%' + input("Input percentage of amount to add to savings: ")
                    userData.addAccount(incomeSrcName, "Savings", percentage)

        case '2':
            inputSources = userData.getSourcesList()
            incomeSrcName = input(f"Input name of input source{inputSources}: ")
            accountName = input("Input name of new account: ")
            flatOrPercentage = input("Flat or percentagefor account? (f/p): ")
            if flatOrPercentage == 'f':
                weight = 'f' + input("Input flat amount")
            elif flatOrPercentage == 'p':
                weight = '%' + input("Input percentage of amount to go to this account: ")
            userData.addAccount(incomeSrcName, accountName, weight)
        
        case '3': 
            inputSources = userData.getSourcesList()
            grandparent = input(f"Input name of input source{inputSources}: ")
            
            inputSources = userData.getParentsList(grandparent)
            parent = input(f"Input name of account to add to{inputSources}: ")
            child = input("Input name of category to create: ")
            flatOrPercentage = input("Flat or percentage for category? (f/p): ")
            if flatOrPercentage == 'f':
                weight = 'f' + input("Input flat amount: ")
            elif flatOrPercentage == 'p':
                weight = '%' + input("Input percentage of amount to go to this category: ")
            userData.addCategory(grandparent, parent, child, weight)
        
        case '4':
            userData.addPurchase()
    
        case '5':
            userData.traverseTree()
        case '6':
            userData.removePurchase(userData.traverseTree())
            #must update values of current and remaining
        case '9':
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


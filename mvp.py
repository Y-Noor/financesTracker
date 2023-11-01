import pickle

userData = None

class Schema():
    def __init__(self):
        self.grandparents = {}
        

        #self.grandparents[name] = {
         #       'amount':amount,
          #      'accounts':{},
           #     'category':{},
            #    'grandchildren':{}
            #}
    def addIncomeSource(self, sourceName, amount):
        self.grandparents[sourceName] = {
                'amount': amount,
                'accounts': {},
                'category': {},
                'grandchildren': {}
                }


    def addAccount(self, grandparent, name, weight):
        identifier = weight[0]
        print(name)
        print(weight)
        if identifier == 'f':
            self.grandparents[grandparent]['accounts'] = {name:self.grandparents[grandparent]['amount']-float(weight[1:])}
        elif identifier == '%':
            self.grandparents[grandparent]['accounts'] = {name:self.grandparents[grandparent]['amount']*float(weight[1:])/100}
            print(self.grandparents)

    def check(self):
        print()
        for grandparent in self.grandparents:
            print('Grandparent: ', grandparent)
            print('Amount:', self.grandparents[grandparent]['amount'])
            print('Parents', self.grandparents[grandparent]['accounts'])
            print('Category', self.grandparents[grandparent]['category'])
            print('Grandchildren', self.grandparents[grandparent]['grandchildren'])
            print()
        print() 
        print(self.grandparents)
        

    def getSources(self):
        return [key for key in  self.grandparents]

def save():
    with  open('finances', 'wb') as f:    
        pickle.dump(userData, f)

def loadUserdata():
    global userData
    try:
        with open('finances', 'rb') as f:
            userData =  pickle.load(f)
    except FileNotFoundError:
        print('no current save file')
        userData = Schema()



def main():
    global userData
    status = True

    print('''
1. Add recurring income source
2. Add Account
3. Add Category
4. Check

-1. exit
         ''') 
    choice = input('What do you want to do? ')
    match choice:
        case '-1':
            status = False
        case '1':
            incomeSrcName = input('input name: ')
            amount = float(input('Input amount: '))
            userData.addIncomeSource(incomeSrcName, amount)
            savingsBool = input('Do you want a savings account with this income source? (y/n): ')
            if savingsBool == 'y':
                flatOrPercentage = input('Flat or percentage for savings account? (f/p)')
                if flatOrPercentage == 'f':
                    flatAmt = 'f' + input('Input flat amount: ')
                    userData.addAccount(incomeSrcName, 'Savings', flatAmt)
                elif flatOrPercentage == 'p':
                    percentage = '%' + input('Input percentage of amount to add to savings: ')
                    userData.addAccount(incomeSrcName, 'Savings', percentage)

        case '2':
            #accountName = input('Input name of new account: ')
            for i in userData.getSources():
                print(i)
            #userData.addAccount(incomeSrcName, accountName)
        case '3':
            userData.check()
    save()
    return status



    
if __name__ == '__main__':
    status = True
    if userData == None:
        loadUserdata()
    while(status):
        status = main()
        print(status)


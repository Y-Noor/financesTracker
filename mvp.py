class AddIncomeSource():
    def __init__(self, name, amount):
        self.grandparents = {name: {
            'amount':amount,
            'accounts':{},
            'category':{},
            'grandchildren':{}
            }}
    
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


def main():
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
            incomeSrc = AddIncomeSource(incomeSrcName, amount)
            savingsBool = input('Do you want a savings account with this income source? (y/n): ')
            if savingsBool == 'y':
                flatOrPercentage = input('Flat or percentage for savings account? (f/p)')
                if flatOrPercentage == 'f':
                    flatAmt = 'f' + input('Input flat amount: ')
                    incomeSrc.addAccount(incomeSrcName, 'Savings', flatAmt)
                elif flatOrPercentage == 'p':
                    percentage = '%' + input('Input percentage of amount to add to savings: ')
                    incomeSrc.addAccount(incomeSrcName, 'Savings', percentage)
            incomeSrc.check()
        case '2':
            accountName = input('Input name of new account: ')
            incomeSrc.addAccount(incomeSrcName, accountName)
        case '3':
            incomeSrc.check()
    
    return status
if __name__ == '__main__':
    status = True
    while(status):
        status = main()
        print(status)


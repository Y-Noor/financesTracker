class AddIncomeSource():
    def __init__(self, name, amount):
        self.grandparents = {name: {
            'amount':amount,
            'parents':{},
            'children':{},
            'grandchildren':{}
            }}

    def check(self):
        print()
        for grandparent in self.grandparents:
            print('Grandparent: ', grandparent)
            print('Amount:', self.grandparents[grandparent]['amount'])
            print('Parents', self.grandparents[grandparent]['parents'])
            print('Children', self.grandparents[grandparent]['children'])
            print('Grandchildren', self.grandparents[grandparent]['grandchildren'])

        print()
        print()


def main():
    status = True
    print('''
1. Add recurring income source
2. Add Account
3. Add Category

-1. exit
         ''') 
    choice = input('What do you want to do? ')
    match choice:
        case '-1':
            status = False
        case '1':
            name = input('input name: ')
            amount = float(input('Input amount: '))
            incomeSrc = AddIncomeSource(name, amount)       
            incomeSrc.check()

    return status
if __name__ == '__main__':
    status = True
    while(status):
        status = main()
        print(status)


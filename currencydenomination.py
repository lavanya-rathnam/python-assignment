class Currencydeno():
    def countCurrency(self,amount):
        notes = [2000,1000,500,200,100,50,20,2,1]
        countof_note = [0,0,0,0,0,0,0,0,0]
        for i,j in zip(notes,countof_note):
            if amount>=i:
                j = amount//i
                amount = amount - j*i
                print ("currency",i, " : count_of_currency ", j)

if __name__ == '__main__':
    amount = int(input("Enter the withdrawl amount"))
    curreny_denomination =  Currencydeno()
    curreny_denomination.countCurrency(amount)
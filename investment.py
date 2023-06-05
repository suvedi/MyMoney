import math

class Investment:
    def __init__(self, equity, debt, gold):
        #self.equity = equity
        self.debt = debt
        self.gold = gold
        self._equity = None
        self.equity = equity

    monthbymonth = {}
    monthlyInvestment = {'month': '', 'equity':0, 'debt':0, 'gold':0}
    totalInvestment = {'equity':0, 'debt':0, 'gold':0}
  

    def setInvestment(self,line):
        allocations = line.split()
        self.equity = float(allocations[1])
        self.debt = float(allocations[2])
        self.gold = float(allocations[3])

    def setSIPInvestments(self, line):
        sipallocations = line.split()
        self.equity += float(sipallocations[1])
        self.debt += float(sipallocations[2])
        self.gold += float(sipallocations[3])
    
    def add_percentage(self, original_number, percentage):
        new_number = math.floor(original_number + (percentage / 100) * original_number)

        return new_number

    def convert_percentage_to_float(self, percentage_str):
        percentage = float(percentage_str.replace('%', ''))  # Remove the percentage sign
        return percentage

    # accept change
    def changeInvestment(self,line):
        changeAllocation = line.split()
        equityPercent = self.convert_percentage_to_float(changeAllocation[1])
        debtPercent = self.convert_percentage_to_float(changeAllocation[2])
        goldPercent = self.convert_percentage_to_float(changeAllocation[3])

        self.equity = self.add_percentage(float(self.equity), equityPercent)
        self.debt = self.add_percentage(float(self.debt), debtPercent)
        self.gold = self.add_percentage(float(self.gold), goldPercent)
        
    def setTotalInvestment(self):
        self.totalInvestment.update({'equity': self.equity, 'debt': self.debt, 'gold': self.gold})

    #check balance
    def balance(self, month):
        return self.monthbymonth[month]
    
    def setBalance(self, month):
        self.monthbymonth[month] = [math.floor(self.equity), math.floor(self.debt), math.floor(self.gold)]

    #rebalance
    def rebalance(self):
        #write code to rebalance the amounts to 60%, 30% and 10%
        #calculate total
        #allocate based on %
        total = self.totalInvestment['equity'] + self.totalInvestment['debt'] + self.totalInvestment['gold']
        self.totalInvestment['equity'] = math.floor(0.6 * total)
        self.totalInvestment['debt'] = math.floor(0.3 * total)
        self.totalInvestment['gold'] = math.floor(0.1 * total)
        return self.totalInvestment
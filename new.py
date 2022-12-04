# Create a calculator to give you the return on investment for a rental property
#first have to declare class with attributes 

class RoiOfRentalProperty():
    def __init__(self, mont_income, mont_expenses, tot_investment):
        self.mont_income = mont_income        # How much rent you will charge tenants
        self.mont_expenses = mont_expenses    # Tax, Insurance, Utilities, Mortgage, repairs, vacancy, etc
        # subtracting monthly rent income from monthly expenses
        self.annual_cash_flow = (self.mont_income - self.mont_expenses)*12 
        self.tot_investment = tot_investment  # How much down payment + closing costs + initial rehab
        #divide annual cash flow by total investment, then multiply the answer by 100 to get the percent 
        self.cash_on_cash_roi = (self.annual_cash_flow / self.tot_investment)*100 

    # next creat a function that will return annual cash flow
    def annualCashFlow(self):
        if self.mont_income == 0 and self.expenses == 0:
            return print("Please enter an amount greater than 0.")
        else:
            return self.annual_cash_flow
            
    # next create a function that will return the cash on cash roi     
    def cashOnCashRoi(self):
        return self.cash_on_cash_roi
    



        



roi = RoiOfRentalProperty(int(input('Monthly Rent Income: ')), 
                         int(input('Monthly Expenses (Mortgage + Tax + Insurance + Utilities + etc...): ')),
                         int(input('Total Investment: ')))


print(f'\nAnnual cash flow: ${roi.annual_cash_flow}')
print('\nCash on Cash ROI:', str(roi.cash_on_cash_roi) + '%')
import yfinance as yf
import pandas as pd 

class BalanceRating:
    def __init__(self,stock):
        stock = yf.Ticker(stock)
        self.balance_sheet = stock.get_balancesheet().iloc[ :,::-1]
        self.cash_flow = stock.get_cashflow().iloc[ :,::-1]
        self.income_statement = stock.get_incomestmt().iloc[ :,::-1]
        self.all_values = pd.concat([self.balance_sheet,self.cash_flow,self.income_statement])
    
        #We write the first two values as the balance sheet value we want to compare, 
        #and our third value is the expected correlation value.
        self.all_values_corelationlist = [["GrossProfit","TotalRevenue",0.7]]

    def get_balance_rating(self):
        row= len(self.all_values_corelationlist)
        score = 0
        for i in range(row):
            self.data = pd.DataFrame({
                '{}'.format(self.all_values_corelationlist[i][0]): list(self.all_values.loc[self.all_values_corelationlist[i][0]]),
                '{}'.format(self.all_values_corelationlist[i][1]): list(self.all_values.loc[self.all_values_corelationlist[i][1]])
            }, index=["2020", "2021", "2022"])
            corelation_rate = self.all_values_corelationlist[i][2]


            corelation = self.data.corr().iloc[0,1]
            print("Expected correlation:",corelation_rate)
            print("Correlation coefficient:", corelation)
            print()
            if corelation_rate<0:
                if corelation_rate>corelation:
                    score+=1
                
            else:
                if corelation_rate<corelation:
                    score+=1
                    
        percentile_score = (score/row)*100
        print("Score:",percentile_score)

    def save_excel(self):
        self.all_values.to_excel("data_excel.xlsx")

BalanceRating("SASA.IS").save_excel()
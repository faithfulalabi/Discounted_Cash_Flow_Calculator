# Discounted_Cash_Flow_Calculator: Project Overview

P.S. I did this project before formally learning Pandas. I will be creating a Version 2.0 later down the road.

The motivation behind this project is due to the fact that I manage my own investment portfolio, and love learning about different ways to analyze and manage a portfolio. One of my favorite investment Youtube Channels (Learn to Invest) created a [Discounted Cash Flow explanation video](https://www.youtube.com/watch?v=fd_emLLzJnk&list=WL&index=9&t=631s&ab_channel=LearntoInvest) and an excel template to use for yourself. Every weekend I would use his excel template to quantitatively analyze companies I was interested in investing in. After learning Python, I knew life would be so much easier automating this process. Rather than spending an hour every weekend to determine what price to buy a company, I now spend seconds because of this script. It not only tells me the price to buy a company, it also gives me their average revenue growth rate, their buy price with their total debt factored in, their average free cashflow to net income margins, their average revenue to net income margins, their weight of asset, and their weight of debt all over a 10 year period. 


# Features 

This code takes in the company's ticker symbol as a string, your API key as a string, and your Required Rate of Return as an integer.

It Outputs the information down below about the company passed in: 

* The price to buy the company without their debt factored in.
* The price to buy the company with their debt factored in.
* A 10 year average of thier revenue growth rate.
* A 10 year average of their net income margins.
* A 10 year average of their revenue to net income margins.
* The weight of their debt (0-100%)
* The weight of their asset (0-100%)

# Discounted Cash Flow Explaination

What Discounted Cash Flow(DCF) does is it helps you calculate the intrensic value of a stock, meaning calculating the vaule of the company today from all expected free cash flow(free money the company will have) from the future. There are a couple of things to know before we can use DCF.

## Company must meet one of these 4 criteria before you can apply DCF calaculator:
1. The company doesn't pay any dividends
2. The company pays dividends but the dividends are very little in comparision to how much they can really afford to pay out.
3. Free cash flow aligns with company's profitablity (The company is profitable)
4. Investor is taking a control prospective(Purchasing significant amount of shares)

## Calculation

There are 3 main sources for our data:
1. The company's Income Statement - Shows the company's revenues and expenses over a period of time. 
2. The company's Balance Sheet - A statement of the assets, liabilities, and capital of a business at a particular point in time.
3. The company's Cash Flow Statement - Shows you the actual cash being paid by and to the company for a given time period. 

### The data we will need from each statements:

* From the Income Statement we will need:
1. Revenue - Tell you how much the company makes before any expenses.
2. Interest Expense - Interest the company pays for their debts(i.e bonds,loans, or line of credit).
3. Income before Tax - Money the company makes before paying taxes. (same as EBT)
4. Income Tax Expense - The amount of expense that the company recognizes in an accounting period for the government tax. (this amount can vary year to year)
5. Net Income - The amount of money left over after the company passes for the cost of goods sold, selling, general and administrative expenses, operating expenses, depreciation, interest, taxes, and other expenses. (The company's profit)

* From the CashFlow Statement we will need:

1. Cash Flow from Operating Activities - The amount of money a company brings in from its ongoing, regular business activities, such as manufacturing and selling goods or providing a service to customers.
2. Capital Expenditures - What a company spends on assets it needs to run the business.(i.e buillding,equipment,furnitures,vechiles,etc).
3. Free Cash Flow - Cash Flow the company's make after accounting for Capital Expenditures. 

* From the Balance Sheet Statement we will need:

1. Short Term Debt - Debt that is due for the company within the next 12 months.
2. Long Term Debt - Debt that is due in more than a year.
3. Cash and Short Term Investments - The sum of the cash and short term investments(money can be quickly converted to cash) the company has.

### Steps for calculation:

1. Calculate the Free Cash Flow to Net Income Margins for the company. Free Cash Flow divided by Net Income.
2. Figure out the Revenue Growth rate by subtracting the current year revenue minus the previous year revenue, divided by current revenue) ex: (rev2021 - rev2020)/rev2021).
3. Next we will need to project the revenue for the next 4 years based on the revenue growth rate we calculated above in step 2. Take the lastest revenue and multiple by growth rate calculate. 
4.  After, we will need to calculate our Revenue to Net Income Margins by dividing Revenue by Net Income (Rev2019/NetIncome2019)
5.  We will need to project the Net Income of what the company will have over the next 4 years. We do this by using our Revenue projections from step 3 and our hostiorical Revenue to Net Income margins.
6.  We can now project the Free Cash Flow the company will have over the next 4 years by using our projected Net Income from step 5 and the historic Free Cash Flow to Net Income margins from step 1.
7.  Next we will need to understand 3 variables. First is Perpetual Growth Rate, which is how much we think the company will grow forever. For this I used 2.5% which is about the rate of inflation. Second is the Shares Outstanding, this is how much shares the company currently has issued in the stock market. Last is your Required Rate of Return(RROR) or discouted factor, this is how much return you want to get on your investment. With all of this we can now calculate the companies Terminal Value. We calculate this by taking the latest year of the projected Free Cash Flow we calaculated, multiple it by our Perpetual Growth rate and then divide by over required rate of return minus our perpetual growth rate. ((latest_free_cash_flow * perpetual_growth_rate)/(RROR-perpetual_growth_rate))
8.  Lastly, we can now calculate the price to buy the company by taking your all the projected Free Cash Flow with plus Terminal Value and dividing by your required rate of return raised to the year of your projection that are in, then taking each output, sum them together and divide by the companies Shares Outstanding. This will give you the currently price of the company based off projected cash flow.

# Install 

* Requests
* Pandas
* Numpy
* Matplotlib
* Obtaining API Key [Click Here](https://financialmodelingprep.com/developer/docs/)

DISCLOSURE: I am not a financial advisor. The code and information written above are for learning purposes only. You are responsible for your own financial decisions.

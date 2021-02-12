# Discounted_Cash_Flow_Calculator: Project Overview

The motivation behind this project is due to the fact that I manage my own investment portfolio, and love learning about different ways to analyze and manage a portfolio. One of my favorite investment Youtube Channels (Learn to Invest) created a [Discounted Cash Flow explanation video](https://www.youtube.com/watch?v=fd_emLLzJnk&list=WL&index=9&t=631s&ab_channel=LearntoInvest) and an excel template to use for yourself. Every weekend I would use his excel template to quantitatively analyze companies I was interested in investing in. After learning Python, I knew life would be so much easier automating this process. Rather than spending an hour every weekend to determine what price to buy a company, I now spend seconds because of this script. It not only tells me the price to buy a company, it also gives me their average revenue growth rate, their buy price with their total debt factored in, their average free cashflow to net income margins, their average revenue to net income margins, their weight of asset, and their weight of debt all over a 10 year period.


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
1. Cash Flow from operating activities - The amount of money a company brings in from its ongoing, regular business activities, such as manufacturing and selling goods or providing a service to customers.
2. Capital Expenditures - What a company spends on assets it needs to run the business.(i.e buillding,equipment,furnitures,vechiles,etc)
3. Free Cash Flow - Cash Flow the company's make after accounting for Capital Expenditures. 



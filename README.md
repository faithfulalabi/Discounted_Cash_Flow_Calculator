# Discounted_Cash_Flow_Calculator: Project Overview

The motivation behind this project is due to the fact that I manage my own investment portfolio, and love learning about different ways to analyze and manage a portfolio. One of my favorite investment Youtube Channels (Learn to Invest) created a [Discounted Cash Flow explanation video](https://www.youtube.com/watch?v=fd_emLLzJnk&list=WL&index=9&t=631s&ab_channel=LearntoInvest) and an excel template to use for yourself. Every weekend I would use his excel template to quantitatively analyze companies I was interested in investing in. After learning Python I knew life would be so much easier automating this process. rather than me spending an hour every weekend to determine what price to buy a company, I now spend seconds to determine it because I wrote this code. It not only tells me the price to buy a company, but also over a 10 year period it gives me their average revenue growth rate, their buy price with their total debt factored in, their average free cashflow to net income margins, their average revenue to net income margins, their weight of asset, and their weight of debt.


# Discounted Cash Flow Explaination

What Discounted Cash Flow(DCF) does is help you calculate the intrensic value of a stock, meaning calculating the vaule of the company today from all expected free cash flow from the future. There are a couple of things to know before we can use DCF.

## Company must meet one of these 4 criteria before you can apply DCF calaculator:
1. The company doesn't pay any dividends
2. Company pays dividends but the dividends are very little in comparision to how much they can really pay out.
3. Free cash flow aligns with company's profitablity (The company is profitable)
4. Investor is taking a control prospective(Purchasing significant amount of shares)

## Calculation
There are 3 main sources for our data:
1. Income Statement : Shows the company's revenues and expenses over a period of time. 
2. Balance Sheet : A statement of the assets, liabilities, and capital of a business at a particular point in time.
3. Cash Flow Statement: Shows you the actual cash being paid by and to the company for a given time period. 

### The data we will need from each statements:



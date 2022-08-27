LEARN PYTHON 3
Carly's Clippers
You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

You have been provided with three lists:

hairstyles: the names of the cuts offered at Carly’s Clippers.
prices: the price of each hairstyle in the hairstyles list.
last_week: the number of purchases for each hairstyle type in the last week.
Each index in hairstyles corresponds to an associated index in prices and last_week.

For example, The hairstyle "bouffant" has an associated price of 30 from the prices list, and was purchased 2 times in the last week as shown in the last_week list. Each of these elements are in the first index of their respective lists.

Let’s get started!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

# instractions

Tasks
0/13 Complete
Mark the tasks as complete by checking them off
Prices and Cuts: 1.
Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.

First, let’s sum up all the prices of haircuts. Create a variable total_price, and set it to 0.

Stuck? Get a hint 2.
Loop through the prices list and add each price to the variable total_price.

Stuck? Get a hint 3.
After your loop, create a variable called average_price that is the total_price divided by the number of prices.

You can get the number of prices by using the len() function.

Stuck? Get a hint 4.
Print the value of average_price so the output looks like:

Average Haircut Price: <average_price>

Stuck? Get a hint 5.
That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.

Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.

Stuck? Get a hint 6.
Print new_prices.

Stuck? Get a hint
Revenue: 7.
Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.

Create a variable called total_revenue and set it to 0.

8.
Use a for loop to create a variable i that goes from 0 to len(hairstyles)

Hint: You can use range() to do this!

Stuck? Get a hint 9.
Add the product of prices[i] (the price of the haircut at position i) and last_week[i] (the number of people who got the haircut at position i) to total_revenue at each step.

Stuck? Get a hint 10.
After your loop, print the value of total_revenue, so the output looks like:

Total Revenue: <total_revenue> 11.
Find the average daily revenue by dividing total_revenue by 7. Call this number average_daily_revenue and print it out.

12.
Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.

Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.

You can use range() in your list comprehension to make i go from 0 to len(new_prices) - 1.

Stuck? Get a hint 13.
Print cuts_under_30.

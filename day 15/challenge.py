#Daily Challenge: "The Price Calculator"
#Scenario: You have a list of prices in Dollars, and you want to convert them all to Nepalese Rupees (NPR).

#Instructions:
#Create a list: prices_usd = [10, 25, 50, 100].
#Set an exchange rate: rate = 134.
#Use a List Comprehension to create prices_npr.
#The expression should be price * rate.
#Print the final list.

prices_usd = [10, 25, 50, 100]
rate = 134
prices_npr = [i*rate for i in prices_usd]
print(prices_npr)
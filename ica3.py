import pandas as pd

frame = pd.read_csv("lego_setsHB.csv", usecols=["list_price", "prod_id", "review_difficulty"])
price = {}
difficulty = {}
for i in range(1000):
	price[frame.at[i, "prod_id"]] = frame.at[i, "list_price"]
	difficulty[frame.at[i, "prod_id"]] = frame.at[i, "review_difficulty"]

print(price)
print(difficulty)

#Only 736 unique prod_id's 

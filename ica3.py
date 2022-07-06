import pandas as pd

frame = pd.read_csv("lego_setsHB.csv", usecols=["list_price", "prod_id", "review_difficulty"])
price = {}
difficulty = {}
price2 = {}
difficulty2 = {}
for i in range(1000):
	price[frame.at[i, "prod_id"]] = frame.at[i, "list_price"]
	difficulty[frame.at[i, "prod_id"]] = frame.at[i, "review_difficulty"]
	price2.setdefault(frame.at[i, "prod_id"], []).append(frame.at[i, "list_price"])
	difficulty2.setdefault(frame.at[i, "prod_id"], []).append(frame.at[i, "review_difficulty"])

#736 unique prod_ids
print(price)
print("\n")
print(difficulty)
print("\n--------------------------\n")
#All values per prod_id entry
print(price2)
print("\n")
print(difficulty2)

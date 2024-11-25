import pandas as pd

df = pd.read_excel("sup_first_hour_sales.xlsx")

df = df.set_index("Transaction ID")
df = df.drop(["Till ID", "Unnamed: 0"], axis = 1)

df = df.dropna(how="any")

df = df.drop_duplicates()

df.at[15.0, "Cost"] = 6.00
print(df)
# print(df[df.duplicated()])


def float_to_time(time_record):
    time_record = str(time_record)
    hours, minutes = time_record.split(".")
    timestamp = f"{int(hours):02}:{int(minutes):02}"
    return timestamp 

df["Time"] = df["Time"].apply(float_to_time)
df["Time"] = pd.to_datetime(df["Time"])
print(df)

print(df["Basket"].mode())

def split_basket(basket_string):
    items = basket_string.split(",")
    # "Tea, Tea, Tea"
    # ["Tea", " Tea", " Tea"]

    # stripped_items = []
    # for item in items:
    #     stripped_items.append(item.strip())
    stripped_items = [item.strip() for item in items]
    return stripped_items

df["Basket"] = df["Basket"].apply(split_basket)
print(df)

exploded_data = df.explode(["Basket"])
print(exploded_data)

print(exploded_data["Basket"].mode())
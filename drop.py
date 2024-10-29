import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("main3.csv")
# df = df.replace("-1", np.nan)
# df = df.replace(-1, np.nan)
# df = df.replace(-1.0, np.nan)
# df = df.replace("-1.0", np.nan)
# df.to_csv("clear_main.csv", index=False)

# def price_for_meter(location):
#     city = df[df["location"] == location]
#     city_price = city["price"].sum()

#     cleaned_data = [x.replace("м²", "").strip() for x in city["total_meters"]]
#     cleaned_data = [x.replace("-1", "0").strip() for x in cleaned_data]
#     cleaned_data = [x.replace("���", "0").strip() for x in cleaned_data]
#     df.to_csv("main1.csv", index=False)
#     cleaned_data = pd.to_numeric(
#         [x.replace(",", ".").strip() for x in cleaned_data]
#     ).sum()

#     return round(city_price / cleaned_data, 2)

# for col in df.columns:
#     pct_missing = np.mean(df[col].isnull())
#     print("{} - {}%".format(col, round(pct_missing * 100)))


# def cleaner(location):
#     city = df[df["location"] == location]

# print(df.shape)
# df = df.dropna(subset=['floors_count', 'floor', 'rooms_count'])
# df["floors_count"] = df["floors_count"].astype(int)
# df["floor"] = df["floor"].astype(int)
# df["rooms_count"] = df["rooms_count"].astype(int)

# df["kitchen_meters"] = (df["kitchen_meters"].str.replace("\xa0м²", "").str.replace(",", ".").astype(float))
# df['living_meters'] = df['living_meters'].str.replace('\xa0м²', '').str.replace(',', '.').astype(float)
# df.to_csv("main4.csv", index=False)
list_of_cities = df['location'].unique()

def price_for_meter(location):
    city = df[df['location']==location]
    city_price = city['price'].sum()
    cleaned_data = city['total_meters'].sum()
    return round(city_price/cleaned_data,2)
with open("dash_info_fourth.csv", 'w', newline='', encoding='UTF-8') as csvfile:
    fieldnames = ['city', 'price_for_meter']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for city in list_of_cities:
        writer.writerow({'city': city, 'price_for_meter': price_for_meter(city)})
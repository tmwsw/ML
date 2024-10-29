import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

df = pd.read_csv("my_df.csv", index_col=0)
# list_of_cities = df["location"].unique()
# # print(list_of_cities)


# # Function for calculate price for meter^2
dict_city = df['location'].unique()

def price_for_meter(location):
    city = df[df['location'] == location]
    price_for_city = city['price'].sum()
    
    clean_data = city['total_meters'].sum()
    
    return round(price_for_city/clean_data, 2)

with open('info.csv', 'w', newline='', encoding='UTF-8') as csvfile:
    names = ['city', 'price_for_meter']
    writer = csv.DictWriter(csvfile, fieldnames=names)
    writer.writeheader()
    for city in dict_city:
        writer.writerow({'city': city, 'price_for_meter': price_for_meter(city)})

# dash_info = pd.read_csv("df_city_meters.csv", index_col=0)
# dash_info.sort_values(["price_for_meter"], axis=0, ascending=[False], inplace=True)
# sns.set_style("whitegrid")
# sns.barplot(x="city", y="price_for_meter", data=dash_info, palette="dark:pink")
# plt.xticks(rotation=75)
# plt.show()

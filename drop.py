import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("main.csv")

# df = df.replace(-1,np.nan)
# df = df.replace("-1",np.nan)
# df = df.replace(-1.0,np.nan)
# df = df.replace("-1.0",np.nan)
# df = df.dropna(subset=['location', 'price', 'rooms_count'])
# df.to_csv('main.csv', index=False)

# df.to_csv('main.csv')

# df["floors_count"] = df["floors_count"].astype(int)
# df.drop('Unnamed: 0')

# df.to_csv('main.csv')

# def filter_properties_until_2024(df):
#     df["year_of_construction"] = df["year_of_construction"].fillna(-1)
#     df["year_of_construction"] = df["year_of_construction"].astype(int)
#     filtered_df = df[df["year_of_construction"] <= 2024]
#     filtered_df.to_csv("main1.csv", index=False, encoding="utf-8")
#     return filtered_df

# output_csv_path = "main1.csv"
# df_filtered = filter_properties_until_2024(df)

# print(f"Отфильтрованные данные сохранены в файл: {output_csv_path}")


# list = [
#     "Напишите автору",
#     "Залоговая недвижимость",
#     "Аукцион",
#     "Позвоните автору",
#     "Подписаться на дом",
# ]
# for obj in list:
#     df = df.replace(obj, np.nan)
# df.to_csv("main1.csv", index=True)


# print(df.head(10), "\n", df.shape)


# df = df.replace(-1,np.nan)
# df = df.replace("-1",np.nan)
# df = df.replace(-1.0,np.nan)
# df = df.replace("-1.0",np.nan)
# df.to_csv('main.csv', index=False)
# перед этим избавиться от символа м²
# df["kitchen_meters"] = (df["kitchen_meters"].str.replace("\xa0м²", "").str.replace(",", ".").astype(float))
# df['living_meters'] = df['living_meters'].str.replace('\xa0м²', '').str.replace(',', '.').astype(float)
# df.to_csv('main1.csv', index=0)
# df = df.replace("-1.0", np.nan)
# df.to_csv("clear_main.csv", index=False)

# def price_for_meter(location):
#     city = df[df["location"] == location]
#     city_price = city["price"].sum()

#     cleaned_data = [x.replace("м²", "").strip() for x in city["total_meters"]]
#     cleaned_data = [x.replace("-1", "0").strip() for x in cleaned_data]
#     cleaned_data = [x.replace("���", "0").strip() for x in cleaned_data]
#     df.to_csv("main1.csv", index=False)
# cleaned_data = pd.to_numeric(
#     [x.replace(",", ".").strip() for x in cleaned_data]
# ).sum()

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
# list_of_cities = df['location'].unique()

# def price_for_meter(location):
#     city = df[df['location']==location]
#     city_price = city['price'].sum()
#     cleaned_data = city['total_meters'].sum()
#     return round(city_price/cleaned_data,2)
# with open("info.csv", 'w', newline='', encoding='UTF-8') as csvfile:
#     fieldnames = ['city', 'price_for_meter']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for city in list_of_cities:
#         writer.writerow({'city': city, 'price_for_meter': price_for_meter(price_for_meter)})

# list_of_cities = df['location'].unique()

# # Функция для расчета price_for_meter
# def price_for_meter(location):
#     city = df[df['location'] == location]
#     city_price = city['price'].sum()
#     cleaned_data = city['total_meters'].sum()
#     return round(city_price / cleaned_data, 2)

# # Открываем файл для записи
# with open("info.csv", 'w', newline='', encoding='UTF-8') as csvfile:
#     fieldnames = ['city', 'price_for_meter']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for city in list_of_cities:
#         writer.writerow({'city': city, 'price_for_meter': price_for_meter(city)})

# print("Файл info.csv успешно создан.")

info = pd.read_csv("info.csv")
info.sort_values(["price_for_meter"], axis=0, ascending=[False], inplace=True)
info.to_csv("info.csv", index=False)
# print(df['location'].unique())
import pandas as pd

# Укажите правильный разделитель и кодировку
df = pd.read_csv("moskva.csv", sep=";", encoding="UTF-8").drop_duplicates()

print(df.head())

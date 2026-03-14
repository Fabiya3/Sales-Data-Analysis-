#This file for taking the code

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("sales_data.csv")

df.head()

df.shape

df.info()

df.isnull().sum()

#Data Cleaning

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

df["Postal Code"] = df["Postal Code"].fillna(0)

df["Year"] = df["Order Date"].dt.year

df["Month"] = df["Order Date"].dt.month

df.duplicated().sum()

df.describe()

total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

#Sales by Category

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,6))
sns.barplot(x=category_sales.index, y=category_sales.values)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

#Sales by Region

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,6))
sns.barplot(x=region_sales.index, y=region_sales.values)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

#Monthly Sales Trend

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(10,6))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

#Top 10 Products

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(y=top_products.index, x=top_products.values)

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")
plt.show()

#Segment Analysis

segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(8,6))
sns.barplot(x=segment_sales.index, y=segment_sales.values)

plt.title("Sales by Customer Segment")
plt.xlabel("Segment")
plt.ylabel("Sales")
plt.show()


summary = df.describe()
summary.to_csv("summary_statistics.csv")

#1. Technology category generates the highest sales.
#2. West region contributes the largest revenue share.
#3. Consumer segment produces the highest number of orders.

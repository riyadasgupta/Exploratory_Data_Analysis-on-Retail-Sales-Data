import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset loading
data = pd.read_csv("D:/EDA on Retail/retail_sales_dataset.csv")

print("First 5 rows:\n", data.head())

data.columns = data.columns.str.strip()

# Data cleaning
print("\nData Types:\n", data.dtypes)
print("\nMissing Values: \n", data.isnull().sum())
print("\nDuplicate Values: \n", data.duplicated())

data = data.dropna().drop_duplicates()
print("\nSummary Statistics:\n", data.describe())

# Descriptive Statistics
print("\n--- Descriptive Statistics ---")

mean_amount = data['Total Amount'].mean()
median_amount = data['Total Amount'].median()
mode_amount = data['Total Amount'].mode()[0]
std_amount = data['Total Amount'].std()

print("Mean:", mean_amount)
print("Median:", median_amount)
print("Mode:", mode_amount)
print("Standard Deviation:", std_amount)


# Time Series Analysis of Retail Sales
#  Converting the Date Column to datetime Format
data['Date'] = pd.to_datetime(data['Date'])

# Setting the Date Column as Index 
data.set_index('Date', inplace=True)


# Plotting Sales Over Time
daily_sales = data['Total Amount'].resample('D').sum()

plt.figure(figsize=(12, 5))
daily_sales.plot()
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.show()


# Plotting Monthly Sales Trend
monthly_sales = data['Total Amount'].resample('M').sum()

plt.figure(figsize=(12, 5))
monthly_sales.plot(marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.show()


# Moving Average
# This helps remove noise and show the overall trend more clearly:
monthly_sales.rolling(window=3).mean().plot(label='3-Month Moving Avg', color='orange')
monthly_sales.plot(label='Monthly Sales', alpha=0.5)
plt.legend()
plt.title('Monthly Sales with 3-Month Moving Average')
plt.show()



print(data.columns)

# Gender-wise sales
gender_sales = data.groupby('Gender')['Total Amount'].sum()
gender_sales.plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6), title='Sales Distribution by Gender')
plt.ylabel("")
plt.show()

# top customers by purchase value
top_customers = data.groupby('Customer ID')['Total Amount'].sum().sort_values(ascending=False).head(10)

print(top_customers)

top_customers.plot(kind='bar', figsize=(10, 5), title='Top 10 Customers by Total Purchase')
plt.ylabel("Total Amount Spent")
plt.tight_layout()
plt.show()


# most purchased product
top_products = data['Product Category'].value_counts().head(10)

print(top_products)

top_products.plot(kind='barh', figsize=(10, 6), color='skyblue')
plt.title("Top 10 Most Purchased Products")
plt.xlabel("Number of Purchases")
plt.tight_layout()
plt.show()

# customer purchase frequency
purchase_freq = data['Customer ID'].value_counts().head(10)

purchase_freq.plot(kind='bar', figsize=(10, 4))
plt.title("Top 10 Customers by Purchase Frequency")
plt.ylabel("Number of Transactions")
plt.tight_layout()
plt.show()





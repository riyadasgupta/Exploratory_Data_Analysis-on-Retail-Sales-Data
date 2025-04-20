# Exploratory_Data_Analysis-on-Retail-Sales-Data

This project performs **Exploratory Data Analysis (EDA)** on a retail sales dataset using Python. The goal is to uncover insights from the data, identify customer and product trends, and visualize time-based patterns in sales.

## 📁 Dataset

- Source: `retail_sales_dataset.csv`
- Contains transaction-level sales data including:
  - Date of purchase
  - Customer ID
  - Gender
  - Product Category
  - Total Amount

## 📊 Libraries Used

- `pandas` – data manipulation
- `matplotlib` – data visualization
- `seaborn` – enhanced visual plots

## ✅ Project Highlights

### 1. Data Cleaning
- Removed missing values and duplicate records
- Stripped column names for consistency

### 2. Descriptive Statistics
- Calculated **mean**, **median**, **mode**, and **standard deviation** for Total Amount
- Generated summary statistics using `.describe()`

### 3. Time Series Analysis
- Converted `Date` column to datetime format
- Resampled data by:
  - 📅 Day – Daily Sales Trend
  - 📆 Month – Monthly Sales Trend
- Applied a **3-month moving average** to smooth sales trends

### 4. Sales Insights
- 🔹 **Gender-wise Sales Distribution** using a pie chart
- 🔹 **Top 10 Customers by Purchase Value**
- 🔹 **Top 10 Most Frequently Purchased Products**
- 🔹 **Top 10 Customers by Purchase Frequency**

## 📈 Visualizations
- Line plots for daily/monthly trends
- Bar charts for customer and product analysis
- Pie chart for gender-based sales distribution

## 💡 Key Insights
- Identified top-spending and most loyal customers
- Discovered best-selling product categories
- Observed monthly and seasonal sales trends
- Helped define customer segments based on gender and frequency

## 🚀 Getting Started

### Prerequisites

Install the required libraries:

```bash
pip install pandas matplotlib seaborn


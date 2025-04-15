import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a sample CSV file (sales_data.csv)
data = {
    "Date": ["2024-01-01", "2024-01-01", "2024-01-02", "2024-01-03", "2024-02-01"],
    "Product": ["Laptop", "Mobile", "Laptop", "Headphones", "Mobile"],
    "Units Sold": [5, 10, -2, 8, 12],
    "Revenue": [5000, 3000, -2000, 800, 3600],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Electronics"]
}

# Save to CSV file
sales_data_file = "sales_data.csv"
pd.DataFrame(data).to_csv(sales_data_file, index=False)

# Step 2: Load the CSV file into a DataFrame
sales_df = pd.read_csv(sales_data_file)
print("First few rows of the dataset:")
print(sales_df.head())

# Step 3: Check and handle missing values
if sales_df.isnull().sum().any():
    print("Missing values found, filling with default values.")
    sales_df.fillna(0, inplace=True)

# Step 4: Ensure Date column is in datetime format
sales_df["Date"] = pd.to_datetime(sales_df["Date"])

# Step 5: Remove rows with negative Units Sold or Revenue
sales_df = sales_df[(sales_df["Units Sold"] >= 0) & (sales_df["Revenue"] >= 0)]

# Step 6: Calculate total revenue per product
total_revenue_by_product = sales_df.groupby("Product")["Revenue"].sum()
print("Total revenue by product:")
print(total_revenue_by_product)

# Step 7: Calculate average units sold per product
average_units_sold = sales_df.groupby("Product")["Units Sold"].mean()
print("Average units sold per product:")
print(average_units_sold)

# Step 8: Identify the product with highest revenue and units sold
highest_revenue_product = total_revenue_by_product.idxmax()
highest_units_sold_product = sales_df.groupby("Product")["Units Sold"].sum().idxmax()
print(f"Product with highest revenue: {highest_revenue_product}")
print(f"Product with highest units sold: {highest_units_sold_product}")

# Step 9: Data Visualization
# Bar chart for total revenue by product
total_revenue_by_product.plot(kind="bar", title="Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

# Line plot for revenue trend over time
sales_df.groupby("Date")["Revenue"].sum().plot(title="Revenue Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Revenue")
plt.show()

# Pie chart for revenue distribution by category
sales_df.groupby("Category")["Revenue"].sum().plot(kind="pie", autopct="%1.1f%%", title="Revenue Distribution by Category")
plt.ylabel("")  # Hide y-label for better visuals
plt.show()

# Bonus: Calculate growth rate of revenue for each product
sales_df["Month"] = sales_df["Date"].dt.to_period("M")
monthly_revenue = sales_df.groupby(["Month", "Product"])["Revenue"].sum().unstack()

growth_rate = ((monthly_revenue.iloc[-1] - monthly_revenue.iloc[0]) / monthly_revenue.iloc[0]) * 100
growth_rate = growth_rate.dropna()  # Drop products without data for both months
print("Growth rate of revenue by product:")
print(growth_rate)

highest_growth_product = growth_rate.idxmax()
print(f"Product with highest growth rate: {highest_growth_product}")

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the CSV file using Pandas
df = pd.read_csv('sales_data.csv')

# Step 2: Perform basic analysis
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset shape (rows, columns):")
print(df.shape)

print("\nDataset information:")
print(df.info())

print("\nChecking for NaN values:")
print(df.isna().sum())

# Step 3: Group sales by product and region
# Total sales by product
product_sales = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
print("\nTotal sales by product:")
print(product_sales)

# Total sales by region
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print("\nTotal sales by region:")
print(region_sales)

# Sales by both product and region
product_region_sales = df.groupby(['Product', 'Region'])['Sales'].sum().unstack()
print("\nSales by product and region:")
print(product_region_sales)

# Step 4: Visualize total sales using a bar chart
plt.figure(figsize=(10, 6))
product_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product', fontsize=16)
plt.xlabel('Product', fontsize=14)
plt.ylabel('Total Sales ($)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('sales_chart.png')  # Save the chart
plt.show()

# Step 5: Demonstrate filtering and selection
# Filtering - products with sales > 1000
high_sales = df[df['Sales'] > 1000]
print("\nProducts with sales > $1000:")
print(high_sales)

# Using loc[]
print("\nUsing loc[] to select specific rows and columns:")
print(df.loc[[0, 2, 4], ['Product', 'Sales']])

# Using iloc[]
print("\nUsing iloc[] to select by index positions:")
print(df.iloc[1:4, 0:3])

# Additional analysis
# Top selling product
top_product = product_sales.idxmax()
print(f"\nTop selling product: {top_product} with ${product_sales.max()} in sales")

# Lowest selling product
low_product = product_sales.idxmin()
print(f"Lowest selling product: {low_product} with ${product_sales.min()} in sales")

# Sales summary statistics
print("\nSales summary statistics:")
print(df['Sales'].describe())

# Quantity vs Sales scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Quantity', y='Sales', hue='Product', s=100)
plt.title('Quantity vs Sales', fontsize=16)
plt.xlabel('Quantity Sold', fontsize=14)
plt.ylabel('Sales ($)', fontsize=14)
plt.grid(linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
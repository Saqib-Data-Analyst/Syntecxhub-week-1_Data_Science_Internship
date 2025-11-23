import pandas as pd

# -> REAd CSV / EXCEL 

df = pd.read_csv("amazon_sales_2025_INR.csv")

# Inspect dataset
print("\n Head: ")
print(df.head())

print("\n Tail: ")
print(df.tail())

print("\n Data types: ")
print(df.dtypes)

# -> SUMMARY STATISTICS (MEAN, MEDIAN, etc.)

print("\n Summary Stats: ")
print(df.describe(include='all'))

# Individual stats (numeric columns only)
print("\n Mean: ")
print(df.mean(numeric_only=True))

print("\n Median: ")
print(df.median(numeric_only=True))

print("\n Min: ")
print(df.min(numeric_only=True))

print("\n Max: ")
print(df.max(numeric_only=True))

print("\n COUNT: ")
print(df.count())

# -> FILTER ROWS, SELECT COLUMNS and SLICE 

filtered_df = df[df['price'] > 500] if 'price' in df.columns else df

selected_df = df[['product_name', 'price', 'rating']] \
    if set(['product_name', 'price', 'rating']).issubset(df.columns) else df

slice_df = df.iloc[:100]

print("\n Filtered data: ")
print(filtered_df.head())

# -> SAVE FILTERED RESULTS to CSV/EXCEL

filtered_df.to_csv("filtered_output.csv", index=False)
filtered_df.to_excel("filtered_output.xlsx", index=False)

print("\n Files saved: filtered_output.csv & filtered_output.xlsx")

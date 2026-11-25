import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

data = {
    'CustomerID': range(101, 121),
    'Age': [25, 34, 45, 23, 31, 52, 46, np.nan, 29, 38, 41, 27, 33, 49, 36, 28, 44, 39, 135, 30],
    'Tenure_Months': [12, 24, 36, 6, 18, 48, 40, 15, np.nan, 28, 32, 10, 22, 50, 26, 14, 38, 30, 20, 16],
    'Monthly_Charges': [55.0, 70.5, 85.0, 45.0, 62.0, 95.0, 88.5, 60.0, 58.0, 75.0,
                        80.0, 50.0, np.nan, 98.0, 72.0, 54.0, 86.0, 78.0, 650.0, 61.0],
    'Churn': ['No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'No',
              'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No']
}
df = pd.DataFrame(data)

print("--- FIRST 5 RECORDS ---")
print(df.head())

print("\n--- DATASET INFO ---")
df.info()

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

num_cols = ['Age', 'Tenure_Months', 'Monthly_Charges']

print("\n--- DESCRIPTIVE STATISTICS SUMMARY ---")
print(df[num_cols].describe())

for col in num_cols:
    print(f"\nStatistics for {col}:")
    print(f"  Mean:               {df[col].mean():.2f}")
    print(f"  Median:             {df[col].median():.2f}")
    print(f"  Mode:               {df[col].mode()[0]:.2f}")
    print(f"  Standard Deviation: {df[col].std():.2f}")
    print(f"  Variance:           {df[col].var():.2f}")
    print(f"  Minimum:            {df[col].min():.2f}")
    print(f"  Maximum:            {df[col].max():.2f}")
    quantiles = df[col].quantile([0.25, 0.50, 0.75]).to_dict()
    print(f"  Quantiles (25%, 50%, 75%): {quantiles}")

plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
plt.hist(df['Age'].dropna(), bins=8, color='skyblue', edgecolor='black')
plt.title('Age Distribution (Histogram)')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.subplot(2, 2, 2)
sns.boxplot(y=df['Monthly_Charges'], color='lightcoral')
plt.title('Box Plot of Monthly Charges')
plt.ylabel('Monthly Charges')

plt.subplot(2, 2, 3)
plt.scatter(df['Tenure_Months'], df['Monthly_Charges'], color='teal', alpha=0.7)
plt.title('Tenure vs Monthly Charges')
plt.xlabel('Tenure (Months)')
plt.ylabel('Monthly Charges')

plt.subplot(2, 2, 4)
corr_matrix = df[num_cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Heatmap')

plt.tight_layout()
plt.show()

print("\n--- MISSING VALUES BEFORE CLEANING ---")
missing_counts = df.isnull().sum()
print(missing_counts)

if missing_counts.sum() > 0:
    df_dropped = df.dropna()
    print(f"\nRows remaining if dropped (dropna): {len(df_dropped)}")

    df_clean = df.copy()
    for col in num_cols:
        df_clean[col] = df_clean[col].fillna(df_clean[col].mean())
else:
    df_clean = df.copy()

print("\n--- DATASET AFTER HANDLING MISSING DATA ---")
print(df_clean.head(10))

z_scores = df_clean[num_cols].apply(zscore)
outlier_mask = (z_scores.abs() > 3).any(axis=1)

print("\n--- DETECTED OUTLIER RECORDS (|Z-score| > 3) ---")
print(df_clean[outlier_mask])

df_no_outliers = df_clean[(z_scores.abs() <= 3).all(axis=1)].copy()
print("\n--- OPTION 1: DATASET AFTER REMOVING OUTLIERS ---")
print(f"Records count: {len(df_no_outliers)}")

df_capped = df_clean.copy()
for col in num_cols:
    upper_limit = df_capped[col].mean() + 3 * df_capped[col].std()
    lower_limit = df_capped[col].mean() - 3 * df_capped[col].std()
    df_capped[col] = df_capped[col].clip(lower=lower_limit, upper=upper_limit)

print("\n--- OPTION 2: DATASET AFTER CAPPING OUTLIERS ---")
print(df_capped.tail())

final_df = df_no_outliers

print("\n--- VERIFICATION: REMAINING MISSING VALUES ---")
print(final_df.isnull().sum())

remaining_z = final_df[num_cols].apply(zscore)
remaining_outliers = (remaining_z.abs() > 3).sum()
print("\n--- VERIFICATION: REMAINING OUTLIERS (|Z-score| > 3) ---")
print(remaining_outliers)

print("\n--- FINAL CLEANED DATASET ---")
print(final_df.head())

final_df.to_csv('cleaned_customer_churn.csv', index=False)
print("\nCleaned dataset saved successfully to 'cleaned_customer_churn.csv'.")

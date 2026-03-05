import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set_theme(style="whitegrid")

# Directory for Task 2
base_dir = r"d:\sricharan-A\documents\Apex_Software_solutions\T2"
csv_path = os.path.join(base_dir, "sales_data.csv")
plots_dir = os.path.join(base_dir, "plots")

if not os.path.exists(plots_dir):
    os.makedirs(plots_dir)

def perform_eda():
    """
    Performs Exploratory Data Analysis by loading sales data, calculating 
    summary statistics, and generating various visualizations.
    """
    # Load data
    df = pd.read_csv(csv_path)
    
    # 1. Summary Statistics
    stats = df.describe()
    stats.to_csv(os.path.join(base_dir, "summary_statistics.csv"))
    
    # 2. Univariate Analysis
    
    # Histogram: Amount Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Amount'], kde=True, color='skyblue')
    plt.title('Distribution of Transaction Amounts')
    plt.xlabel('Amount ($)')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(plots_dir, 'amount_distribution.png'))
    plt.close()
    
    # Histogram: Age Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], kde=True, color='salmon')
    plt.title('Distribution of Customer Ages')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(plots_dir, 'age_distribution.png'))
    plt.close()
    
    # Bar Chart: Transactions by Category
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Category', data=df, palette='viridis')
    plt.title('Number of Transactions by Category')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.savefig(os.path.join(plots_dir, 'category_counts.png'))
    plt.close()
    
    # 3. Multivariate Analysis
    
    # Scatter Plot: Age vs Amount
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Age', y='Amount', data=df, hue='Category', alpha=0.6)
    plt.title('Customer Age vs. Transaction Amount')
    plt.xlabel('Age')
    plt.ylabel('Amount ($)')
    plt.savefig(os.path.join(plots_dir, 'age_vs_amount.png'))
    plt.close()
    
    # Heatmap: Correlation
    plt.figure(figsize=(8, 6))
    corr = df[['Amount', 'Age']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.savefig(os.path.join(plots_dir, 'correlation_heatmap.png'))
    plt.close()
    
    # Box Plot: Amount by Category
    plt.figure(figsize=(12, 7))
    sns.boxplot(x='Category', y='Amount', data=df, palette='Set2')
    plt.title('Transaction Amount Range by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount ($)')
    plt.savefig(os.path.join(plots_dir, 'amount_by_category.png'))
    plt.close()
    
    print("EDA Analysis complete! Visualizations saved in 'plots' folder.")

if __name__ == "__main__":
    print("Starting Exploratory Data Analysis...")
    perform_eda()
    print("Usage: python eda_analysis.py (ensure sales_data.csv exists in the same directory)")

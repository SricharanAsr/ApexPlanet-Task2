import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Set global style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12

def perform_eda(csv_path, plots_dir):
    """
    Performs Exploratory Data Analysis by loading sales data, calculating 
    summary statistics, and generating advanced visualizations.
    """
    if not os.path.exists(csv_path):
        logger.error(f"Data file not found at {csv_path}")
        return

    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
        logger.info(f"Created plots directory: {plots_dir}")

    try:
        # Load data
        logger.info("Loading sales data...")
        df = pd.read_csv(csv_path)
        df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'])
        
        # 1. Summary Statistics
        logger.info("Calculating summary statistics...")
        stats = df.describe()
        stats_path = os.path.join(os.path.dirname(csv_path), "summary_statistics.csv")
        stats.to_csv(stats_path)
        
        # 2. Univariate Analysis
        
        # Plot 1: Amount Distribution
        logger.info("Generating transaction amount distribution...")
        plt.figure()
        sns.histplot(df['Amount'], kde=True, color='royalblue')
        plt.title('Distribution of Transaction Amounts')
        plt.xlabel('Amount ($)')
        plt.ylabel('Frequency')
        plt.savefig(os.path.join(plots_dir, 'amount_distribution.png'))
        plt.close()
        
        # Plot 2: Age Distribution
        logger.info("Generating customer age distribution...")
        plt.figure()
        sns.histplot(df['Age'], kde=True, color='crimson')
        plt.title('Distribution of Customer Ages')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.savefig(os.path.join(plots_dir, 'age_distribution.png'))
        plt.close()
        
        # Plot 3: Category Distribution (Pie Chart)
        logger.info("Generating category distribution pie chart...")
        plt.figure(figsize=(8, 8))
        df['Category'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, cmap='Pastel1')
        plt.title('Market Share by Category')
        plt.ylabel('')
        plt.savefig(os.path.join(plots_dir, 'category_market_share.png'))
        plt.close()
        
        # 3. Multivariate Analysis
        
        # Plot 4: Age vs Amount
        logger.info("Generating Age vs Amount scatter plot...")
        plt.figure()
        sns.scatterplot(x='Age', y='Amount', data=df, hue='Category', alpha=0.6, style='Category')
        plt.title('Customer Age vs. Transaction Amount Trends')
        plt.savefig(os.path.join(plots_dir, 'age_vs_amount.png'))
        plt.close()
        
        # Plot 5: Monthly Sales Trend
        logger.info("Generating monthly sales trend...")
        monthly_sales = df.resample('M', on='Purchase_Date')['Amount'].sum()
        plt.figure()
        monthly_sales.plot(marker='o', linestyle='-', color='darkgreen')
        plt.title('Monthly Sales Revenue Trend')
        plt.xlabel('Month')
        plt.ylabel('Total Revenue ($)')
        plt.savefig(os.path.join(plots_dir, 'monthly_revenue_trend.png'))
        plt.close()
        
        # Plot 6: Amount by Category (Box Plot)
        logger.info("Generating category amount box plot...")
        plt.figure()
        sns.boxplot(x='Category', y='Amount', data=df, palette='Set2')
        plt.title('Transaction Amount Variance by Category')
        plt.savefig(os.path.join(plots_dir, 'amount_by_category_variance.png'))
        plt.close()
        
        logger.info(f"EDA Analysis complete! Visualizations saved in: {plots_dir}")

    except Exception as e:
        logger.error(f"Error during EDA: {e}")

if __name__ == "__main__":
    # Project Paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_p = os.path.join(base_dir, "sales_data.csv")
    plots_p = os.path.join(base_dir, "plots")
    
    perform_eda(csv_p, plots_p)


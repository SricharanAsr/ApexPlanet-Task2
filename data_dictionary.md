# 📖 Data Dictionary: Synthetic Sales Dataset

This document provides a detailed description of the fields present in the `sales_data.csv` dataset used for the EDA and Business Intelligence analysis.

| Column Name | Data Type | Description | Example |
| :--- | :--- | :--- | :--- |
| **Transaction_ID** | Integer | A unique identifier for each sales transaction. Starts from 1001. | 1025 |
| **Customer_Name** | String | The name of the customer who made the purchase. | Jane Smith |
| **DOB** | Date (YYYY-MM-DD) | The Date of Birth of the customer. Used for demographic analysis. | 1985-05-12 |
| **Purchase_Date** | Date (YYYY-MM-DD) | The date when the transaction occurred (ranging from 2023-01-01 onwards). | 2023-11-20 |
| **Amount** | Float | The total monetary value of the transaction in USD ($). | 450.75 |
| **Category** | String | The product category of the purchase (Electronics, Clothing, Home, Groceries, Beauty). | Electronics |
| **Age** | Integer | Calculated age of the customer based on the current year and DOB. | 39 |

---
## Business Logic Notes
- **Transaction Amount**: Generated based on category-specific ranges (e.g., Electronics have higher average values than Groceries).
- **Date Range**: Purchase dates are synthetically generated to simulate a 15-month activity period.
- **Demographics**: Customer ages range from 18 to 64 years.

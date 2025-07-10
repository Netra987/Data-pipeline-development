# Data-pipeline-development

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : NETRA ALLE

*INTERN ID* : CT04DG3270

*DOMAIN* : DATA SCIENCE

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH

ETL Pipeline for Customer Data Preprocessing
A complete ETL (Extract, Transform, Load) pipeline built with Python to automate the preprocessing of customer data using pandas and scikit-learn.
This script processes real-world datasets (e.g., from Kaggle) and prepares them for machine learning or analytics by handling missing data, scaling numeric features, and encoding categorical features.

Tools & Libraries Used
Tool / Library	Purpose
pandas	Reading CSV data and handling tabular data
scikit-learn	Preprocessing (imputation, scaling, encoding)
Pipeline & ColumnTransformer	Organize and automate the transformation process
Python 3.7+	Scripting language
Jupyter / VS Code	Development environment (optional)

What the Code Does
This ETL pipeline automates the following:

1. Extract
Reads a CSV file using pandas.read_csv().
Path is defined once in the script.

2. Transform
Identifies numeric and categorical columns.
Handles missing values:
Numerical: Replaces with column mean.
Categorical: Replaces with the most frequent value.
Scales numeric data using StandardScaler.
One-hot encodes categorical data with OneHotEncoder.
Combines transformations using ColumnTransformer.

3. Load
Converts the processed array into a new DataFrame.
Optionally adds back the original CustomerID and target variable.
Saves the final DataFrame to a new CSV (processed_customers.csv).

How I Performed This Project
Explored a Kaggle customer dataset with rich features like Age, Income, Gender, and Profession.
Designed a clear ETL flow in Python following best practices.
Broke the pipeline into modular functions (extract_data, transform_data, load_data) for maintainability and scalability.
Handled real-world issues like missing values, categorical encoding, and data standardization using scikit-learn tools.
Validated output using printed column names and data preview.
Ensured the pipeline is reusable with just a single change in file path.

📂 Folder Structure
bash
Copy
Edit
etl-customer-data/
├── etl_pipeline.py                # Main Python script
├── Customers.csv                  # Raw dataset (input)
├── processed_customers.csv        # Cleaned dataset (output)
└── README.md                      # Project documentation
⚙️ How to Run the Project
1. Install Requirements
pip install pandas scikit-learn
2. Prepare Dataset
Place your dataset in the same folder and name it Customers.csv
(Or update the path in the code).
3. Run the Script
pipeline.py
📈 Expected Input Columns
Your CSV file should contain:
Column	Type
CustomerID	Integer
Age	Numerical
Gender	Categorical
Profession	Categorical
Annual Income ($)	Numerical
Work Experience	Numerical
Family Size	Numerical
Spending Score (1-100)	Target

💾 Output
A new file processed_customers.csv will be saved with:
Scaled numeric features
One-hot encoded categorical features
Target and ID columns preserved

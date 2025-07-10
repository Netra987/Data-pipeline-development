import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# === STEP 1: EXTRACT DATA ===
def extract_data(file_path):
    print("📥 Extracting data...")
    return pd.read_csv(file_path)

# === STEP 2: TRANSFORM DATA ===
def transform_data(df):
    print("🔄 Transforming data...")

    # Identify feature types based on the dataset
    numeric_features = ['Age', 'Annual Income ($)', 'Work Experience', 'Family Size']
    categorical_features = ['Gender', 'Profession']
    
    # Target variable (if needed for modeling)
    target_feature = 'Spending Score (1-100)'

    # Define pipelines
    numeric_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),  # Handle missing numeric values
        ('scaler', StandardScaler())  # Standardize numeric features
    ])

    categorical_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),  # Handle missing categorical values
        ('encoder', OneHotEncoder(handle_unknown='ignore'))  # One-hot encode categories
    ])

    # Combine pipelines
    preprocessor = ColumnTransformer([
        ('num', numeric_pipeline, numeric_features),
        ('cat', categorical_pipeline, categorical_features)
    ])

    # Fit and transform the data
    processed_array = preprocessor.fit_transform(df)

    # Get column names
    numeric_columns = numeric_features
    categorical_columns = preprocessor.named_transformers_['cat']['encoder'].get_feature_names_out(categorical_features)
    all_column_names = list(numeric_columns) + list(categorical_columns)

    # Convert to DataFrame
    processed_df = pd.DataFrame(
        processed_array.toarray() if hasattr(processed_array, 'toarray') else processed_array,
        columns=all_column_names
    )

    # Add back ID and target columns if needed
    if 'CustomerID' in df.columns:
        processed_df['CustomerID'] = df['CustomerID'].values
    if target_feature in df.columns:
        processed_df[target_feature] = df[target_feature].values

    return processed_df

# === STEP 3: LOAD DATA ===
def load_data(df, output_path):
    print("💾 Loading data...")
    df.to_csv(output_path, index=False)
    print(f"✅ Processed data saved to: {output_path}")

# === MAIN ETL FUNCTION ===
def etl_pipeline(input_path, output_path):
    df = extract_data(input_path)
    transformed_df = transform_data(df)
    load_data(transformed_df, output_path)

# === RUN THE PIPELINE ===
if __name__ == "__main__":
    input_file = "C:/Users/netra/Downloads/Customers.csv"  # Update with your actual file path
    output_file = "processed_customers.csv"
    etl_pipeline(input_file, output_file)

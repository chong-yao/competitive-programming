import pandas as pd
import numpy as np

def clean_and_transform_data():
    """
    Cleans, transforms, and documents the house prices dataset.
    
    This function performs the following steps:
    1.  Loads the train, test, and data description files.
    2.  Corrects known typos and inconsistencies in the data.
    3.  Combines train and test sets for consistent processing.
    4.  Strategically handles missing values for both categorical and numerical features.
    5.  Applies one-hot encoding to all categorical features to make them model-ready.
    6.  Splits the data back into cleaned training and testing sets.
    7.  Updates the data description file to reflect all transformations.
    8.  Saves the cleaned data and the new description to separate files.
    """
    try:
        # --- 1. Load Data ---
        print("Loading datasets...")
        train_df = pd.read_csv('train.csv')
        test_df = pd.read_csv('test.csv')
        with open('data_description.txt', 'r') as f:
            data_description = f.read()

        print("Data loaded successfully.")

        # --- 2. Initial Cleaning and Preparation ---
        print("Performing initial cleaning...")
        # Correct known typos in the test set to ensure consistency
        test_df['Exterior2nd'] = test_df['Exterior2nd'].replace({'Brk Cmn': 'BrkComm', 'CmentBd': 'CemntBd'})
        
        # MSSubClass is a categorical feature represented by numbers; convert to string
        train_df['MSSubClass'] = train_df['MSSubClass'].astype(str)
        test_df['MSSubClass'] = test_df['MSSubClass'].astype(str)

        # Store IDs and SalePrice for later re-attachment
        train_id = train_df['Id']
        test_id = test_df['Id']
        train_sales_price = train_df['SalePrice']

        # Drop columns that are not features for the model
        train_df = train_df.drop(['Id', 'SalePrice'], axis=1)
        test_df = test_df.drop('Id', axis=1)

        # Combine dataframes to ensure consistent encoding and imputation
        combined_df = pd.concat([train_df, test_df], axis=0, ignore_index=True)
        print(f"Combined dataset shape: {combined_df.shape}")

        # --- 3. Handle Missing Values ---
        print("Handling missing values...")
        # For these columns, 'NA' is a meaningful category (e.g., "No Alley")
        cols_na_as_category = [
            'Alley', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1',
            'BsmtFinType2', 'FireplaceQu', 'GarageType', 'GarageFinish',
            'GarageQual', 'GarageCond', 'PoolQC', 'Fence', 'MiscFeature'
        ]
        for col in cols_na_as_category:
            combined_df[col] = combined_df[col].fillna('NA_cat')

        # Impute missing numerical features with the column's median
        numerical_cols = combined_df.select_dtypes(include=np.number).columns
        for col in numerical_cols:
            if combined_df[col].isnull().any():
                median_val = combined_df[col].median()
                combined_df[col] = combined_df[col].fillna(median_val)
        
        # --- 4. One-Hot Encode Categorical Features ---
        print("Applying one-hot encoding...")
        categorical_cols = combined_df.select_dtypes(include=['object']).columns.tolist()
        
        combined_df_encoded = pd.get_dummies(combined_df, columns=categorical_cols, dummy_na=False, dtype=int)
        print(f"Shape after one-hot encoding: {combined_df_encoded.shape}")

        # --- 5. Split back into train and test sets ---
        print("Splitting data back into train and test sets...")
        train_cleaned = combined_df_encoded.iloc[:len(train_df)]
        test_cleaned = combined_df_encoded.iloc[len(train_df):]

        # Re-attach original Id and SalePrice columns
        train_cleaned.insert(0, 'Id', train_id.values)
        train_cleaned['SalePrice'] = train_sales_price.values
        test_cleaned.insert(0, 'Id', test_id.values)

        # --- 6. Update Data Description File ---
        print("Updating data description file...")
        # Correct general typos in the description text
        data_description = data_description.replace('Poured Contrete', 'Poured Concrete')
        data_description = data_description.replace('Gabrel (Barn)', 'Gambrel (Barn)')
        data_description = data_description.replace('CemntBd', 'CementBd')

        new_description_lines = []
        lines = data_description.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i]
            if not line.strip():
                new_description_lines.append(line)
                i += 1
                continue

            col_name = line.split(':')[0].strip()
            
            # Replace original categorical descriptions with new one-hot encoded column lists
            if col_name in categorical_cols:
                new_description_lines.append(f"{col_name}: This feature has been one-hot encoded into the following binary columns (1 for presence, 0 for absence):")
                encoded_cols = sorted([c for c in combined_df_encoded.columns if c.startswith(f"{col_name}_")])
                for encoded_col in encoded_cols:
                    new_description_lines.append(f"       {encoded_col}")
                
                # Skip the old description lines for this feature
                i += 1
                while i < len(lines) and (lines[i].strip() == '' or lines[i].startswith('\t') or lines[i].startswith(' ')):
                    i += 1
            else:
                new_description_lines.append(line)
                i += 1
        
        data_description_cleaned = "\n".join(new_description_lines)

        # --- 7. Save Cleaned and Transformed Files ---
        print("Saving cleaned files...")
        train_cleaned.to_csv('train_cleaned.csv', index=False)
        test_cleaned.to_csv('test_cleaned.csv', index=False)
        with open('data_description_cleaned.txt', 'w') as f:
            f.write(data_description_cleaned)
            
        return "Process complete. Files 'train_cleaned.csv', 'test_cleaned.csv', and 'data_description_cleaned.txt' have been created successfully."

    except FileNotFoundError as e:
        return f"An error occurred: The file {e.filename} was not found. Please ensure all original files are in the same directory as the script."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# --- How to Run ---
# 1. Save the code above as a Python file (e.g., `process_data.py`).
# 2. Place it in the same folder as your original `train.csv`, `test.csv`, and `data_description.txt` files.
# 3. Run the script from your terminal: `python process_data.py`
#
# # Example of direct execution:
result_message = clean_and_transform_data()
print(result_message)
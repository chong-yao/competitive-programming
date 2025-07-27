import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import time
import warnings

# Suppress warnings for cleaner output (some models might warn with default settings)
warnings.filterwarnings("ignore")

# --- 1. Load and Prepare Data ---
print("Loading and preparing data...")
train_df = pd.read_csv('train_cleaned.csv')
test_df = pd.read_csv('test_cleaned.csv')

# Prepare the data
X_full = train_df.drop(['Id', 'SalePrice'], axis=1)
y_full = train_df['SalePrice']
X_test_final = test_df.drop('Id', axis=1)

# Align columns between training and test sets
# Get list of columns from training data
train_cols = X_full.columns
test_cols = X_test_final.columns

# Handle missing columns by adding them and filling with 0
# Columns in train but not test (for test set)
missing_in_test = set(train_cols) - set(test_cols)
for c in missing_in_test:
    X_test_final[c] = 0

# Columns in test but not train (for train set) - This should ideally be empty if test is pre-aligned
missing_in_train = set(test_cols) - set(train_cols)
for c in missing_in_train:
    X_full[c] = 0

# Ensure column order is consistent
X_test_final = X_test_final[train_cols]

# --- 2. Create Train/Validation Split ---
# Split the full training set to have a validation set for scoring
X_train, X_val, y_train, y_val = train_test_split(
    X_full, y_full, test_size=0.2, random_state=42
)

print(f"Training set size: {X_train.shape}")
print(f"Validation set size: {X_val.shape}")
print(f"Final test set size: {X_test_final.shape}")

# --- 3. Import All Scikit-Learn Regressors ---
# Dynamically import regressors to avoid listing them manually
from sklearn.utils import all_estimators

# Get all regressor classes from sklearn
regressors = all_estimators(type_filter='regressor')

# Filter out regressors that might cause issues or are not suitable for this task
# (e.g., require specific parameters, are experimental, or are not standard)
skip_list = [
    'CCA', 'IsotonicRegression', 'MultiOutputRegressor',
    'RegressorChain', 'StackingRegressor', 'VotingRegressor',
    'OrthogonalMatchingPursuitCV', 'LassoLarsCV', 'LarsCV', 'LassoCV',
    'RidgeCV', 'ElasticNetCV', 'MultiTaskElasticNetCV',
    'MultiTaskLassoCV', 'PLSCanonical', 'PLSRegression'
]

# --- 4. Evaluate Models ---
results = []
print("\nEvaluating models...")
for name, RegressorClass in regressors:
    if name in skip_list:
        continue
    try:
        # Record start time
        start_time = time.time()

        # Instantiate the model with default parameters
        # Handle special cases if needed (e.g., MLPRegressor needs max_iter)
        if name == 'MLPRegressor':
             model = RegressorClass(max_iter=500, random_state=42) # Increase max_iter for convergence
        else:
             model = RegressorClass(random_state=42) if 'random_state' in RegressorClass().get_params() else RegressorClass()

        # Fit the model
        model.fit(X_train, y_train)

        # Predict on validation set
        y_pred_val = model.predict(X_val)

        # Calculate MSE
        mse = mean_squared_error(y_val, y_pred_val)

        # Record end time
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Store results
        results.append({'Model': name, 'MSE': mse, 'Time (s)': elapsed_time})
        print(f"Model: {name}, MSE: {mse:.2f}, Time: {elapsed_time:.2f}s")

    except Exception as e:
        print(f"Error with model {name}: {e}")
        results.append({'Model': name, 'MSE': np.nan, 'Time (s)': np.nan})


# --- 5. Determine Best Model ---
print("\n--- Model Evaluation Results ---")
results_df = pd.DataFrame(results)

# Sort by MSE (lower is better), handling potential NaNs
results_df_sorted = results_df.sort_values(by='MSE', ascending=True, na_position='last').reset_index(drop=True)
print(results_df_sorted)

# Find the best model (lowest MSE)
if not results_df_sorted.empty and not results_df_sorted['MSE'].isna().all():
    best_model_info = results_df_sorted.iloc[0]
    best_model_name = best_model_info['Model']
    best_model_mse = best_model_info['MSE']
    print(f"\n--- Best Model (based on MSE on validation set) ---")
    print(f"Model Name: {best_model_name}")
    print(f"Validation MSE: {best_model_mse:.2f}")

    # --- 6. Retrain Best Model and Make Final Predictions ---
    print(f"\nRetraining {best_model_name} on the full dataset and making final predictions...")

    # Get the regressor class again
    _, BestRegressorClass = next((n, cls) for n, cls in regressors if n == best_model_name)

    # Instantiate the best model
    if best_model_name == 'MLPRegressor':
        best_model_final = BestRegressorClass(max_iter=500, random_state=42)
    else:
        best_model_final = BestRegressorClass(random_state=42) if 'random_state' in BestRegressorClass().get_params() else BestRegressorClass()

    # Fit on the entire original training data
    best_model_final.fit(X_full, y_full)

    # Predict on the final test set
    final_predictions = best_model_final.predict(X_test_final)

    # Create the submission file
    submission = pd.DataFrame({'Id': test_df['Id'], 'SalePrice': final_predictions})
    submission_filename = f'submission_{best_model_name}_default.csv'
    submission.to_csv(submission_filename, index=False)

    print(f"Submission file '{submission_filename}' created successfully!")
    print(submission.head())

else:
    print("\nNo models were successfully evaluated.")
    
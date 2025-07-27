import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load the training and test data
train_df = pd.read_csv('train_cleaned.csv')
test_df = pd.read_csv('test_cleaned.csv')

# Prepare the data
# Features are all columns except 'Id' and 'SalePrice'
X_train = train_df.drop(['Id', 'SalePrice'], axis=1)
y_train = train_df['SalePrice']

# The test set has the same columns as the training set, except for SalePrice
X_test = test_df.drop('Id', axis=1)

# Align columns - just in case there are differences
# Get list of columns from training data
train_cols = X_train.columns
test_cols = X_test.columns

# Get the columns that are in the training set but not the test set
missing_in_test = set(train_cols) - set(test_cols)

# Add the missing columns to the test set and fill with 0
for c in missing_in_test:
    X_test[c] = 0

# Get the columns that are in the test set but not the training set
missing_in_train = set(test_cols) - set(train_cols)

# Add the missing columns to the training set and fill with 0
for c in missing_in_train:
    X_train[c] = 0

# Ensure the order of columns in the test set is the same as in the training set
X_test = X_test[train_cols]


# Create and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Create the submission file
# The test IDs start from 1461, as seen in the sample_submission.csv.
start_id = 1461
num_predictions = len(predictions)
test_ids = range(start_id, start_id + num_predictions)

submission = pd.DataFrame({'Id': test_ids, 'SalePrice': predictions})

# Ensure the 'Id' column is of integer type
submission['Id'] = submission['Id'].astype(int)

submission.to_csv('submission.csv', index=False)

print("Submission file created successfully!")
print(submission.head())
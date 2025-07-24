import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

# === Read the data
df_train = pd.read_csv("train_data.csv")
df_test = pd.read_csv("test_data.csv")

df_train['Timestamp'] = pd.to_datetime(df_train['Timestamp'])
df_train['hour'] = df_train['Timestamp'].dt.hour

df_test['Timestamp'] = pd.to_datetime(df_test['Timestamp'])
df_test['hour'] = df_test['Timestamp'].dt.hour

# === Subtask 1
df_test['Answer'] = df_test['hour'].apply(lambda h: 'AM' if h < 12 else 'PM')

task1 = pd.DataFrame({
    'subtaskID': 1,
    'datapointID': df_test.ID,
    'answer': df_test['Answer']
})

# === Subtask 2
features = [
    'Suspicious_Port_Activity', 'Traffic_Volume_Variation',
    'Packet_Length_Anomaly', 'Malware_Score', 'Threat_Level_Index',
    'User_Behavior_Score', 'Geo_Dispersion', 'Payload_Entropy',
    'Login_Attempts', 'Device_Response_Time', 'Session_Duration',
    'Packet_Retry_Rate', 'Anomaly_Tendency'
]

X_train = df_train[features]
y_train = df_train['Attack_Type']

X_test = df_test[features]

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'class_weight': ['balanced', 'balanced_subsample']
}

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state = 42)
random_search = RandomizedSearchCV(model, param_distributions=param_grid, n_iter=10, cv=3, scoring='f1_weighted', random_state = 42)
random_search.fit(X_train, y_train)

best_model = random_search.best_estimator_

y_pred = best_model.predict(X_test)

task2 = pd.DataFrame({
    'subtaskID': 2,
    'datapointID': df_test['ID'],
    'answer': y_pred
})

# === Final dataset
submission_df = pd.concat([task1, task2], ignore_index=True)
submission_df.to_csv("submission2.csv", index=False)
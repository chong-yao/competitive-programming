import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# === Read the data
df_train = pd.read_csv("train_data.csv")
df_test = pd.read_csv("test_data.csv")

# === Subtask 1
df_test['Timestamp'] = pd.to_datetime(df_test['Timestamp'])
df_test['Answer'] = df_test['Timestamp'].dt.hour.apply(lambda h: 'AM' if h < 12 else 'PM')

task1 = pd.DataFrame({
    'subtaskID': 1,
    'datapointID': df_test.ID,
    'answer':  df_test['Answer']
})

# === Subtask 2
y = df_train["Attack_Type"]
features = ["Suspicious_Port_Activity", "Traffic_Volume_Variation", "Packet_Length_Anomaly", "Malware_Score","Threat_Level_Index", "User_Behavior_Score", "Geo_Dispersion", "Payload_Entropy", "Login_Attempts", "Device_Response_Time", "Session_Duration", "Packet_Retry_Rate", "Anomaly_Tendency"]

X = pd.get_dummies(df_train[features])
X_test = pd.get_dummies(df_test[features])

model = RandomForestClassifier(n_estimators=2000, max_depth=50, random_state=5)
model.fit(X, y)
y_pred= model.predict(X_test)

task2 = pd.DataFrame({
    'subtaskID': 2,
    'datapointID': df_test.ID,
    'answer': y_pred
})

# === Final datatset
submission_df = pd.concat([task1, task2], ignore_index=True)
submission_df.to_csv("submission.csv", index=False)
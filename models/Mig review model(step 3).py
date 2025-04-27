import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump

# Load the WoS data
wos_health_df = pd.read_excel('/Users/migueloliveira/Documents/Mig_projects/Synthetic_data_projects/Model HR_NHR/WoS_health_revised_MO.xlsx', skiprows=1)

# Assign correct column names
wos_health_df.columns = ['Authors', 'Title', 'Abstract', 'Year', 'Mig Review', 'GPT4 Review']

# Encode the 'Mig Review' column (assuming similar encoding applies)
# Note: Adjust the lambda function as necessary based on the actual content of 'Mig Review'
wos_health_df['Label'] = wos_health_df['Mig Review'].apply(lambda x: 1 if 'Health related' in x else 0)

# Drop unnecessary columns - now dropping 'Mig Review' after creating 'Label' and 'GPT4 Review' since it's not used
wos_health_df = wos_health_df.drop(['Mig Review', 'GPT4 Review'], axis=1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    wos_health_df['Abstract'], wos_health_df['Label'], test_size=0.1, random_state=42
)

# Create a TF-IDF vectorizer and logistic regression pipeline with class_weight='balanced'
model = make_pipeline(
    TfidfVectorizer(stop_words='english'),
    LogisticRegression(random_state=42, class_weight='balanced')
)

# Train the model
model.fit(X_train, y_train)

# Predict on the test set and evaluate
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))

# Save the model
model_path = "/Users/migueloliveira/Documents/Mig_projects/Synthetic_data_projects/Model HR_NHR/my_trained_model_Mig_review.joblib"
dump(model, model_path)

print(f"Model saved to {model_path}")

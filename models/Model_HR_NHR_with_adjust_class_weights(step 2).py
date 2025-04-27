import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report

# Load the WoS data
wos_health_df = pd.read_excel('/Users/migueloliveira/Documents/Mig_projects/Synthetic_data_projects/Model HR_NHR/WoS_health_revised_MO.xlsx', skiprows=1)  # Skipping the first row now, assuming it's headers

# Assign correct column names
wos_health_df.columns = ['Authors', 'Title', 'Abstract', 'Year', 'Mig Review', 'GPT4 Review']

# Encode the 'GPT4 Review' column (Health related=1, Not health related=0)
wos_health_df['Label'] = wos_health_df['GPT4 Review'].apply(lambda x: 1 if 'Health related' in x else 0)

# Drop unnecessary columns
wos_health_df = wos_health_df.drop(['Mig Review', 'GPT4 Review'], axis=1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    wos_health_df['Abstract'], wos_health_df['Label'], test_size=0.5
    , random_state=42
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

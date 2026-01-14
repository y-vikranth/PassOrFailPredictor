import pandas as pd

pd.options.display.float_format = '{:.2f}'.format

#Load Dataset
df = pd.read_csv('data/student_pass_fail.csv')

#Inspect top 5 rows
print("First 5 rows of dataset:")
print(df.head())

#Check dataset shape
print("\nDataset Shape (r/c):")
print(df.shape)

#Check Info like column names and data types
print("\nDataset Information:")
print(df.info())

#Basic Statistical Summary
print("\nBasic Statistic Summary:")
print(df.describe())


# Separating features and label


X = df[['attendance', 'internal_marks']]
y = df['result']

print("\nFeatures (X) preview:")
print(X.head())

print("\nLabel (y) preview:")
print(y.head())


#Splitting the training data and testing data


from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nTraining set size:")
print(X_train.shape, y_train.shape)

print("\nTesting set size:")
print(X_test.shape, y_test.shape)


#Logistic Regression Model Training


from sklearn.linear_model import LogisticRegression

# Create the Logistic Regression model
model = LogisticRegression()

# Train the model using training data
model.fit(X_train, y_train)

print("\nLogistic Regression model trained successfully.")


#Model Prediction and Evaluation


from sklearn.metrics import accuracy_score

# Predict on the test data
y_pred = model.predict(X_test)

print("\nPredicted values:")
print(y_pred)

print("\nActual values:")
print(y_test.values)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", accuracy)

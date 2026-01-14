Pass / Fail Prediction Using Logistic Regression
1. Introduction

This project implements a supervised machine learning classification model to predict whether a student will pass or fail based on academic indicators. The model is built using Logistic Regression, which is suitable for binary classification problems. Pandas is used for data handling and preprocessing.

2. Problem Statement

To predict a student’s Pass / Fail outcome using attendance percentage and internal marks as input features.

3. Dataset Description

The dataset is a labeled dataset created to simulate realistic academic data.

Features (Input Variables)

attendance: Student attendance percentage

internal_marks: Marks obtained in internal assessments

Label (Output Variable)

result:

1 → Pass

0 → Fail

The dataset is stored as:

data/student_pass_fail.csv

4. Machine Learning Approach Used

Learning Type: Supervised Learning

Problem Type: Binary Classification

Algorithm: Logistic Regression

The dataset is split into:

Training set (80%) – used to train the model

Testing set (20%) – used to evaluate model performance

This split ensures that the model’s generalization ability can be assessed.

5. Model Training

The Logistic Regression model is trained using the training dataset. During training, the model learns the relationship between the input features (attendance and internal marks) and the output label (pass/fail). The objective is to learn parameters that minimize classification error on the training data.

6. Model Evaluation

The trained model is evaluated using accuracy, which measures the proportion of correctly classified samples in the test dataset.

Accuracy
=
Number of Correct Predictions
Total Predictions
Accuracy=
Total Predictions
Number of Correct Predictions
	​


Evaluation is performed on unseen data to ensure proper generalization and to avoid overfitting.

7. Results

The model produces binary predictions (0 or 1) for the test dataset.
The achieved accuracy indicates how effectively the logistic regression model classifies students into pass or fail categories based on the given features.

8. Conclusion

This project demonstrates the application of Logistic Regression for binary classification using a clean and structured machine learning pipeline. By separating training and testing data and evaluating performance using accuracy, the project follows core machine learning principles such as supervised learning, classification, and generalization.

9. Technologies Used

Python

Pandas

NumPy

scikit-learn

# Naive Bayes Classifier for Loan Approval
from sklearn.naive_bayes import GaussianNB

# Training data: [Monthly Income (in thousands), Credit Score]
X = [
    [25, 550],
    [30, 580],
    [35, 600],
    [60, 720],
    [75, 750],
    [90, 800]
]

# Output labels: Rejected or Approved
y = ["Rejected", "Rejected", "Rejected", "Approved", "Approved", "Approved"]

# Training the classifier
model = GaussianNB()
model.fit(X, y)

# User input
income = int(input("Enter monthly income (in thousands, e.g. 50): "))
credit_score = int(input("Enter credit score (300-850): "))

# Prediction
result = model.predict([[income, credit_score]])

print("\nLoan Status:", result[0])

# Student Detail
print("\nStudent Detail")
print("Name: Prasanna Pokharel")
print("Rollno: 24")
print("LAB III-2")
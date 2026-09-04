# Simple Expert System for Disease Diagnosis (COVID-19, Malaria, Food Poisoning)

print("Disease Diagnosis Expert System \n")

fever = input("Do you have fever? y/n ").strip().lower()
loss_of_taste = input("Do you have loss of taste or smell? y/n ").strip().lower()
chills = input("Do you have chills or shivering? y/n ").strip().lower()
vomiting = input("Do you have nausea or vomiting? y/n ").strip().lower()

if fever == "y" and loss_of_taste == "y":
    print("\nDiagnosis: You may have COVID-19.")
elif fever == "y" and chills == "y":
    print("\nDiagnosis: You may have Malaria.")
elif vomiting == "y" and fever == "n":
    print("\nDiagnosis: You may have Food Poisoning.")
else:
    print("\nDiagnosis: Disease not identified. Consult a doctor.")

print("Name: Prasanna Pokharel")
print("Rollno: 24")
print("LAB III-1")
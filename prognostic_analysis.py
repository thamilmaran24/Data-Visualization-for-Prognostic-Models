import matplotlib.pyplot as plt

# Sample patient data
data = {
    'PatientID': [101, 102, 103, 104, 105],
    'Age': [45, 50, 38, 60, 47],
    'RiskScore': [0.8, 0.6, 0.3, 0.9, 0.5],
    'Prognosis': ['Poor', 'Average', 'Good', 'Poor', 'Average']
}


print("\n📋 Patient Data:")
print("PatientID\tAge\tRiskScore\tPrognosis")
for i in range(len(data['PatientID'])):
    print(f"{data['PatientID'][i]}\t\t{data['Age'][i]}\t{data['RiskScore'][i]}\t\t{data['Prognosis'][i]}")


plt.figure(figsize=(10, 5))
plt.bar(data['PatientID'], data['RiskScore'], color='orange')
plt.title('Patient Risk Scores')
plt.xlabel('Patient ID')
plt.ylabel('Risk Score')
plt.ylim(0, 1)
plt.grid(True)
plt.tight_layout()
plt.savefig('risk_scores.png')
plt.show()


prognosis_counts = {}
for p in data['Prognosis']:
    prognosis_counts[p] = prognosis_counts.get(p, 0) + 1


plt.figure(figsize=(6, 4))
plt.pie(prognosis_counts.values(), labels=prognosis_counts.keys(), autopct='%1.1f%%',
        colors=['red', 'yellow', 'green'])
plt.title('Prognosis Outcome Distribution')
plt.tight_layout()
plt.savefig('prognosis_distribution.png')
plt.show()

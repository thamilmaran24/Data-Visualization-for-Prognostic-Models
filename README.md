# 📊 Data Visualization for Prognostic Models

## 🔍 Project Overview

This project implements a Python program to visualize patient data trends and prognosis outcomes. It provides a clear graphical interpretation of risk scores and prognosis categories using **bar charts** and **pie charts**, making it easier to understand patient health insights. The data is simulated to demonstrate how such a visualization system might work in a clinical decision-making environment.

---

## ⚙️ Technologies Used

- **Python** – Core programming language  
- **Matplotlib** – For creating charts and visualizations  
*(No pandas or numpy used in this version)*

---

## 🧠 Features

- Visualizes individual patient **risk scores** in a bar chart
- Shows the distribution of **prognosis outcomes** in a pie chart
- Simulates patient data without needing external files
- Prints patient data table directly in the terminal/command prompt
- Saves both graphs as PNG image files (`risk_scores.png` and `prognosis_distribution.png`)

---

## 🧪 Sample Data Used in Code

```text
PatientID    Age    RiskScore    Prognosis
101          45     0.8          Poor
102          50     0.6          Average
103          38     0.3          Good
104          60     0.9          Poor
105          47     0.5          Average

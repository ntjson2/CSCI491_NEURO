import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('stroke.csv')

# Calculate the bmi mean and standard deviation for patients who have had a stroke and who have not had a stroke
bmi_mean_noStroke = df[df['stroke'] == 0]['bmi'].mean()
bmi_std_noStroke = df[df['stroke'] == 0]['bmi'].std()
bmi_mean_hasStroke = df[df['stroke'] == 1]['bmi'].mean()
bmi_std_hasStroke = df[df['stroke'] == 1]['bmi'].std()

print("bmi Mean NoStroke:", bmi_mean_noStroke)
print("bmi Std NoStroke:", bmi_std_noStroke)
print("bmi Mean HasStroke:", bmi_mean_hasStroke)
print("bmi Std HasStroke:", bmi_std_hasStroke)

# Assess the NA values in the data
na_bmi_noStroke = df[(df['stroke'] == 0) & (df['bmi'].isnull())].shape[0]
na_bmi_hasStroke = df[(df['stroke'] == 1) & (df['bmi'].isnull())].shape[0]

print("NA BMI NoStroke:", na_bmi_noStroke)
print("NA BMI HasStroke:", na_bmi_hasStroke)

# Handle NA values (e.g., drop NA values for simplicity)
df = df.dropna(subset=['bmi'])

# Recalculate the bmi mean and standard deviation after handling NA values
bmi_mean_noStroke = df[df['stroke'] == 0]['bmi'].mean()
bmi_std_noStroke = df[df['stroke'] == 0]['bmi'].std()
bmi_mean_hasStroke = df[df['stroke'] == 1]['bmi'].mean()
bmi_std_hasStroke = df[df['stroke'] == 1]['bmi'].std()

print("Recalculated bmi Mean NoStroke:", bmi_mean_noStroke)
print("Recalculated bmi Std NoStroke:", bmi_std_noStroke)
print("Recalculated bmi Mean HasStroke:", bmi_mean_hasStroke)
print("Recalculated bmi Std HasStroke:", bmi_std_hasStroke)

# Plot the recalculated data as a box plot
fig = plt.figure(figsize=(10, 7))
plt.boxplot([df[df['stroke'] == 0]['bmi'], df[df['stroke'] == 1]['bmi']], labels=['No Stroke', 'Has Stroke'])
plt.title('BMI Distribution for Stroke and No Stroke')
plt.xlabel('Stroke Status')
plt.ylabel('BMI')
plt.show()


fig2 = plt.figure(figsize=(10, 7))
plt.boxplot([df['bmi']], labels=['Raw BMI data'])
plt.title('BMI Distribution for Raw data')
plt.xlabel('Stroke Status')
plt.ylabel('BMI')
plt.show()
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
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

# Fire up the subplots 
fig, axs = plt.subplots(2, 2, figsize=(15, 12))

# Plot the recalculated data as a box plot
axs[0, 0].boxplot([df[df['stroke'] == 0]['bmi'], df[df['stroke'] == 1]['bmi']], labels=['No Stroke', 'Has Stroke'])
axs[0, 0].set_title('BMI Distribution for Stroke and No Stroke')
axs[0, 0].set_xlabel('Stroke Status')
axs[0, 0].set_ylabel('BMI')

# BMI distribution for raw data
axs[0, 1].boxplot([df['bmi']], labels=['Raw BMI data'])
axs[0, 1].set_title('BMI Distribution for Raw data')
axs[0, 1].set_xlabel('Stroke Status')
axs[0, 1].set_ylabel('BMI')


# Plotting age distribution for patients with no stroke
noStrokeAge = df[df['stroke'] == 0]['age']
sns.histplot(noStrokeAge, kde=True, ax=axs[1,0])
axs[1, 0].set_title('Age Distribution for no stroke')
axs[1, 0].set_xlabel('Age')
axs[1, 0].set_ylabel('Frequency')
axs[1, 0].grid(True)

# Plotting age distribution for patients with stroke;
hasStrokeAge = df[df['stroke'] == 1]['age'];
sns.histplot(hasStrokeAge, kde=True, ax=axs[1,1])
axs[1, 1].set_title('Age Distribution for stroke');
axs[1, 1].set_xlabel('Age');
axs[1, 1].set_ylabel('Frequency');
axs[1, 1].grid(True)

# Adjust layout for padding (was looking rough)
plt.tight_layout(pad=6.0, w_pad=4.0, h_pad=4.0)
plt.show()
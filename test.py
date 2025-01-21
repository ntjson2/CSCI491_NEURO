
import pandas as pd

df = pd.read_csv('stroke.csv')
bmi_mean = df['bmi'].mean()

bmi_mean_noStroke = df[df['stroke'] == 0]['bmi'].mean()
bmi_std_noStroke = df[df['stroke'] == 0]['bmi'].std()

#print(&quot;Average for each column:&quot;)
print(f"bmi Mean NoStroke {bmi_mean_noStroke: ^50}")
print("bmi Std NStroke", bmi_std_noStroke)
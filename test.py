
import pandas as pd

df = pd.read_csv('stroke.csv')
bmi_mean = df['bmi'].mean()

#print(&quot;Average for each column:&quot;)
print(bmi_mean)


#print(df.to_string()) 

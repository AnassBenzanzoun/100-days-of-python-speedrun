import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


with open("./2018_Central_Park_Squirrel_Census.csv") as file:
    data = pd.read_csv(file)

# Check for missing values
# print(data.isnull().sum())

# Create a bar plot for Primary Fur Color
sns.countplot(data["Primary Fur Color"])
plt.title("Distribution of Primary Fur Color")
plt.xlabel("Primary Fur Color")
plt.ylabel("Count")
plt.show()

# Filtering out rows with null values in the 'Age' column
data_with_age = data[data["Age"].notnull()]

# Creating a bar plot for squirrel distribution by age
plt.figure(figsize=(10, 6))
sns.countplot(data_with_age["Age"])
plt.title("Squirrel Distribution by Age")
plt.xlabel("Age")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Creating a bar plot to show primary fur color distribution based on age
plt.figure(figsize=(10, 6))
sns.countplot(x="Age", hue="Primary Fur Color", data=data_with_age)
plt.title("Primary Fur Color Distribution by Age")
plt.xlabel("Age")
plt.ylabel("Count")
plt.legend(title="Primary Fur Color")
plt.xticks(rotation=45)
plt.show()

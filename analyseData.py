
import pandas as pd

#create constants/requirements for the program
fileName = 'data.csv'
requiredCols = ['Street', 'Zip', 'City', 'Last Check-In Date', 'Company']

#read in the file
df = pd.read_csv(fileName, sep=',', engine='c', header=0, usecols=['First Name', 'Last Name','Street','Zip', 'City', 'Type','Last Check-In Date', 'Job','Phone', 'Company'], low_memory=False)
print("\n")

#check file for missing required elements
for col in requiredCols:
    missing = df[col].isnull().sum()
    if missing>0:
        print("{} has {} missing value(s)".format(col,missing))

#remove rows that do not meet the required criteria
for req in requiredCols:
    df.dropna(subset = [req], inplace=True)

#convert date type from string to date -- specifying input format
df['Last Check-In Date'] = pd.to_datetime(df['Last Check-In Date'], format='%d/%m/%Y')

#Retrieve the customer with the earliest check in date.
earliestCustomer = df.loc[df['Last Check-In Date'].idxmin(), ['First Name','Last Name']]
print("\nCustomer with earliest check in: ")
print(earliestCustomer)

#Retrieve the customer with the latest check in date.
latestCustomer = df.loc[df['Last Check-In Date'].idxmax(), ['First Name','Last Name']]
print("\nCustomer with latest check in: ")
print(latestCustomer)

#Retrieve a list of customer’s full names ordered alphabetically.
#full name = first name + last name
df['Full Name'] = df['First Name'] + ' ' + df['Last Name']
df = df.iloc[df['Full Name'].str.normalize('NFKD').argsort()]
print("\nCustomer's names ordered alphabetically")
print(df['Full Name'])

#Retrieve a list of the companies user’s jobs ordered alphabetically.
df = df.sort_values(['Job']).drop_duplicates('Job', keep='last')
print("\nJobs ordered alphabetically")
print(df['Job'])

"""
Output: 
Street has 2 missing value(s)
Zip has 2 missing value(s)
City has 1 missing value(s)
Last Check-In Date has 2 missing value(s)
Company has 1 missing value(s)

Customer with earliest check in:
First Name    Anselmo
Last Name      Ortega
Name: 4, dtype: object

Customer with latest check in:
First Name      Bjorn
Last Name     Ostberg
Name: 5, dtype: object

Customer's names ordered alphabetically
3      André Citröen
4     Anselmo Ortega
1      Ángel Ganivet
5      Bjorn Ostberg
0    Federico García
9        Paul Hudson
Name: Full Name, dtype: object

Jobs ordered alphabetically
5        Actor
0      Dentist
4    Policeman
3      Postman
9     Salesman
Name: Job, dtype: object
"""
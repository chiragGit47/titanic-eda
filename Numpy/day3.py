import pandas as pd

# data = {
#     "Name":   ["Rahul", "Priya", "Arjun", "Sneha", "Vikram"],
#     "Age":    [24, 27, 22, 30, 25],
#     "City":   ["Gurugram", "Delhi", "Mumbai", "Gurugram", "Pune"],
#     "Salary": [45000, 62000, 38000, 75000, 51000]
# }

# df = pd.DataFrame(data)

df = pd.read_csv("employees.csv")

# print(df.shape)

# print(df.tail(3))

# print(df.info())

# print(df.describe())

# print(df["City"])

# print(df[["Name", "City" ,"Salary"]])

# print(df.iloc[0])        # first row
# print(df.iloc[0:3])      # first 3 rows
# print(df.iloc[0, 2]) sx

# print(df.loc[0])                        # row with index 0
# print(df.loc[0:2, "Name":"City"])       # rows 0-2, columns Name to City
# print(df.loc[:, "Salary"]) 

# print(df[df["Age"] < 26][["Name", "Age", "Salary"]])

# Add a new column
# df["Salary_LPA"] = df["Salary"] * 12 / 100000
# print(df[["Name", "Salary", "Salary_LPA"]])

# print(df[["Name","Department"]],"\n")



# print(df.iloc[3:5])

# city_g = df[df["City"] == "Gurugram"]
# print(city_g,"\n")

# q4 = df[ (df["Department"]== "Finance") & (df["Salary"] > 65000 )]
# print(q4,"\n")

# df["Senior"] = df["Age"] > 27
# print(df,"\n")

# grouped_dept = df.groupby("Department")["Salary"].sum()

# print(grouped_dept)

# print(df.groupby(["Department", "City"])["Salary"].mean())

# print(df.sort_values(["Department", "Salary"], ascending=[True, False]))

# top3 = df.sort_values("Salary", ascending=False).head(3)
# print(top3[["Name", "Department", "Salary"]])

# df2 = pd.read_csv("employees_messy.csv")
# print(df2)
# print(df2.isnull().count())

# print(df.groupby("Department")["Salary"].agg(["mean","min","max"]))

df2 = pd.read_csv("employees_messy.csv")

df2["Age"] = df2["Age"].fillna(df2["Age"].mean())         
df2["City"] = df2["City"].fillna("Unknown")               
df2["Salary"] = df2["Salary"].fillna(df2["Salary"].median()) 
df2["Department"] = df2["Department"].fillna("Unknown")

print(df2.isnull())

df2.groupby("Department")["Salary"].mean()

print(df2.sort_values("Salary", ascending=False))

print(df2.value_counts("City"))
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df = pd.read_csv("Matplotlib/employees.csv")


# days = [1, 2, 3, 4, 5, 6, 7]
# sales = [120, 145, 98, 172, 160, 188, 210]


# plt.plot(days, sales, color="purple", marker="o", linewidth=2)
# plt.title("Weekly Sales")
# plt.xlabel("Day")
# plt.ylabel("Sales (₹)")
# plt.grid(True)
# plt.show()

# departments = ["Engineering", "Finance", "Marketing"]
# avg_salary = [42000, 74000, 56000]

# plt.bar(departments, avg_salary, color=["#7F77DD", "#1D9E75", "#D85A30"])
# plt.title("Average salary by department")
# plt.ylabel("Salary (₹)")
# plt.show()

# salaries = [38000, 42000, 45000, 51000, 55000, 62000, 68000, 75000, 80000]

# plt.hist(salaries, bins=5, color="#7F77DD", edgecolor="black")
# plt.title("Salary distribution")
# plt.xlabel("Salary (₹)")
# plt.ylabel("Number of employees")
# plt.show()

# age =    [22, 24, 25, 27, 28, 30, 31]
# salary = [38000, 45000, 51000, 62000, 68000, 75000, 80000]

# plt.scatter(age, salary, color="#1D9E75", s=100)
# plt.title("Age vs salary")
# plt.xlabel("Age")
# plt.ylabel("Salary (₹)")
# plt.show()


# df = pd.DataFrame({
#     "Age":    [22, 24, 25, 27, 28, 30, 31],
#     "Salary": [38000, 45000, 51000, 62000, 68000, 75000, 80000],
#     "Score":  [88, 72, 91, 65, 85, 78, 94]
# })

# print(df)
# sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
# plt.title("Correlation heatmap")
# plt.show()

# fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# print("axes", axes[0],axes[1])

# Left plot
# axes[0].bar(departments, avg_salary, color="#7F77DD")
# axes[0].set_title("Salary by department")
# axes[0].set_ylabel("Salary (₹)")

# # Right plot
# axes[1].scatter(age, salary, color="#1D9E75", s=100)
# axes[1].set_title("Age vs salary")
# axes[1].set_xlabel("Age")
# axes[1].set_ylabel("Salary (₹)")



# plt.tight_layout()
# plt.show()

print(df)

# Plot 1 — bar chart

avg_salary_dept = df.groupby("Department")["Salary"].mean()

print(avg_salary_dept)

plt.bar(avg_salary_dept.index,avg_salary_dept.values, color="#7F77DD")
plt.title("Average salary by department")
plt.ylabel("Salary (₹)")
plt.show()

# Plot 2 — histogram (you write this)

salaries = df["Salary"]

plt.hist(salaries, bins=4, color="#7F77DD", edgecolor="white")
plt.title("Salary distribution")
plt.xlabel("Salary (₹)")
plt.ylabel("Number of employees")
plt.show()

# Plot 3 — heatmap (you write this)


df2 = df[["Salary","Age"]]

sns.heatmap(df2.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation heatmap")
plt.show()
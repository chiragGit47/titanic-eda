import numpy as np

# marks = np.array([
#     [72, 85, 90],
#     [60, 55, 70],
#     [88, 92, 95],
#     [45, 60, 55]
# ])

# print("shape of the array",marks.shape)

# print("avg marks of each student ",np.mean(marks ,axis=1))
# print("avg marks of each subject ",np.mean(marks ,axis=0))

# temp = marks.reshape(1,12)
# print("max number in the array",np.max(temp))

# x=np.mean(marks ,axis=1)

# print(marks[x>80])

daily_sales = np.arange(1, 29)  # 28 days of sales data

x = np.reshape(daily_sales ,(4, 7))  # Reshape to 4 weeks (7 days each)

print(x)

print("sum of sales for each week ", np.sum (x ,axis=1))
mean =np.mean(x ,axis=0)
max = np.max(mean)
print("best day of the week ", np.where(x==max))
y=np.max(np.sum (x ,axis=1))
print("highest total ", np.where(x==y))
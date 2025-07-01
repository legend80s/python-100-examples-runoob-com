# > 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

# score = float(input("输入分数："))

score = 91
print("A" if score >= 90 else "B" if score >= 60 else "C")

# 89 属于 B
score = 89
print("A" if score >= 90 else "B" if score >= 60 else "C")

score = 58
print("A" if score >= 90 else "B" if score >= 60 else "C")

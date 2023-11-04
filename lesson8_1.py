from tools import getStudent #從tools的module 只imprt student這個class來用

stu1=getStudent(name="robert",chinese=89,math=92,english=75)
print(stu1.name)
print(stu1.chinese)
print(stu1.english)
print(stu1.math)
print(stu1.sum())
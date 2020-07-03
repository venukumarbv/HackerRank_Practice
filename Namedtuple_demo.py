from collections import namedtuple

Student = namedtuple('Student', 'Name, Age, Specialized')
s1 = Student('Venukumar',27,'Python')
print(s1.Name)
print(s1.Age)
print(s1.Specialized)
print(s1)
# Formatted String in Python

name = "ABC"
course = "Python Course"

s1 = "Welcome %s to the %s"%(name, course)
print(s1)

s2 = "Welcome {0} to the {1}".format(name, course)
print(s2)

s3 = f"Welcome {name} to the {course}"
print(s3)

a = 10
b = 20
print(f"Additon of {a} and {b} is {a+b}")

print(f"Lower case of '{course}' is '{course.lower()}'")
print(f"Upper case of '{course}' is '{course.upper()}'")

с = input("Введіть рядок  слів")
lst = с.replace('.', '').split()
print(min((word for word in lst if word), key=len))
print(max((word for word in lst if word), key=len))

mass = float(input())
height = float(input())

imt = mass / (height * height)
if 18.5 <= imt <= 25:
    print("Оптимальная масса")
if imt < 18.5:
    print("Избыточная масса")
else:
    print("Избыточная масса")

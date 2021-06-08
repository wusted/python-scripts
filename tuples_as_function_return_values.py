def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return (c,a)

radius = [10, 20, 30, 40, 50]
for rad in radius:
    cir_area_tuple =  circleInfo(rad)
    print(f"Circle of Radius {rad} has a Circumference and Area of:", cir_area_tuple)


circ, area = circleInfo(100)
print(circ, area)

def celcius_to_farenhite(celcius):
    farenhite = int((celcius *(9/5)) + (32))
    return farenhite
def farenhite_to_celcius(farenhite):
    celcius = int((farenhite - (32)) * (5/9))
    return celcius
def meter_to_centimeter(meter):
    centimeter = meter * 100
    return centimeter
def centimeter_to_meter(centimeter):
    meter = centimeter/100
    return meter
def meter_to_millimeter(meter):
    millimeter = meter * 1000
    return millimeter
def millimeter_to_meter(millimeter):
    meter = millimeter/1000
    return meter

print(celcius_to_farenhite(50))
print(farenhite_to_celcius(40))
print(meter_to_centimeter(30))
print(centimeter_to_meter(1000))
print(meter_to_millimeter(20))
print(millimeter_to_meter(10000))
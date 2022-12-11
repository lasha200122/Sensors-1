import Error


def Info(MyData, NeaData):
    co = [i.CO for i in MyData]
    no = [i.NO for i in MyData]
    no2 = [i.NO2 for i in MyData]
    o3no2 = [i.O3NO2 for i in MyData]
    temperature = [i.Temperature for i in MyData]
    pressure = [i.Pressure for i in MyData]
    humidity = [i.Humidity for i in MyData]
    Nco = [i.CO for i in NeaData]
    Nno = [i.NO for i in NeaData]
    Nno2 = [i.NO2 for i in NeaData]
    No3no2 = [i.O3NO2 for i in NeaData]
    N_temperature = [i.Temperature for i in NeaData]
    N_pressure = [i.Pressure for i in NeaData]
    N_humidity = [i.Humidity for i in NeaData]

    print()
    print("==== CO ====")
    print("Absolute error in norm 1: ")
    print(Error.AbsoluteNorm1(co, Nco))
    print("Absolute error in norm 2: ")
    print(Error.AbsoluteNorm2(co, Nco))
    print("Absolute error in norm infinity: ")
    print(Error.AbsoluteNormInf(co, Nco))
    print("Relative error in norm 1: ")
    print(Error.RelativeNorm1(co, Nco))
    print("Relative error in norm 2: ")
    print(Error.RelativeNorm2(co, Nco))
    print("Relative error in norm infinity: ")
    print(Error.RelativeNormInf(co, Nco))

    print()
    print("==== NO ====")
    print("Absolute error in norm 1: ")
    print(Error.AbsoluteNorm1(no, Nno))
    print("Absolute error in norm 2: ")
    print(Error.AbsoluteNorm2(no, Nno))
    print("Absolute error in norm infinity: ")
    print(Error.AbsoluteNormInf(no, Nno))
    print("Relative error in norm 1: ")
    print(Error.RelativeNorm1(no, Nno))
    print("Relative error in norm 2: ")
    print(Error.RelativeNorm2(no, Nno))
    print("Relative error in norm infinity: ")
    print(Error.RelativeNormInf(no, Nno))

    print()
    print("==== NO2 ====")
    print("Absolute error in norm 1: ")
    print(Error.AbsoluteNorm1(no2, Nno2))
    print("Absolute error in norm 2: ")
    print(Error.AbsoluteNorm2(no2, Nno2))
    print("Absolute error in norm infinity: ")
    print(Error.AbsoluteNormInf(no2, Nno2))
    print("Relative error in norm 1: ")
    print(Error.RelativeNorm1(no2, Nno2))
    print("Relative error in norm 2: ")
    print(Error.RelativeNorm2(no2, Nno2))
    print("Relative error in norm infinity: ")
    print(Error.RelativeNormInf(no2, Nno2))

    print()
    print("==== O3NO2 ====")
    print("Absolute error in norm 1: ")
    print(Error.AbsoluteNorm1(o3no2, No3no2))
    print("Absolute error in norm 2: ")
    print(Error.AbsoluteNorm2(o3no2, No3no2))
    print("Absolute error in norm infinity: ")
    print(Error.AbsoluteNormInf(o3no2, No3no2))
    print("Relative error in norm 1: ")
    print(Error.RelativeNorm1(o3no2, No3no2))
    print("Relative error in norm 2: ")
    print(Error.RelativeNorm2(o3no2, No3no2))
    print("Relative error in norm infinity: ")
    print(Error.RelativeNormInf(o3no2, No3no2))

    print()
    print("==== Temperature ====")
    print("Absolute error in norm 1: ")
    print(Error.AbsoluteNorm1(temperature, N_temperature))
    print("Absolute error in norm 2: ")
    print(Error.AbsoluteNorm2(temperature, N_temperature))
    print("Absolute error in norm infinity: ")
    print(Error.AbsoluteNormInf(temperature, N_temperature))
    print("Relative error in norm 1: ")
    print(Error.RelativeNorm1(temperature, N_temperature))
    print("Relative error in norm 2: ")
    print(Error.RelativeNorm2(temperature, N_temperature))
    print("Relative error in norm infinity: ")
    print(Error.RelativeNormInf(temperature, N_temperature))

    print()
    print("==== Pressure ====")
    print("Absolute error in norm 1: ")
    print(Error.AbsoluteNorm1(pressure, N_pressure))
    print("Absolute error in norm 2: ")
    print(Error.AbsoluteNorm2(pressure, N_pressure))
    print("Absolute error in norm infinity: ")
    print(Error.AbsoluteNormInf(pressure, N_pressure))
    print("Relative error in norm 1: ")
    print(Error.RelativeNorm1(pressure, N_pressure))
    print("Relative error in norm 2: ")
    print(Error.RelativeNorm2(pressure, N_pressure))
    print("Relative error in norm infinity: ")
    print(Error.RelativeNormInf(pressure, N_pressure))

    print()
    print("==== Humidity ====")
    print("Absolute error in norm 1: ")
    print(Error.AbsoluteNorm1(humidity, N_humidity))
    print("Absolute error in norm 2: ")
    print(Error.AbsoluteNorm2(humidity, N_humidity))
    print("Absolute error in norm infinity: ")
    print(Error.AbsoluteNormInf(humidity, N_humidity))
    print("Relative error in norm 1: ")
    print(Error.RelativeNorm1(humidity, N_humidity))
    print("Relative error in norm 2: ")
    print(Error.RelativeNorm2(humidity, N_humidity))
    print("Relative error in norm infinity: ")
    print(Error.RelativeNormInf(humidity, N_humidity))

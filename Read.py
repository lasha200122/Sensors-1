import pandas as pd
import DataViewModel
import OmegasViewModel
import Paths


def DataList():
    excel = pd.read_excel(Paths.directory)
    result = []
    count = 0
    for date, co, no, no2, o3no2, pressure, temperature, humidity in zip(excel[Paths.Date], excel[Paths.CO],
                                                                         excel[Paths.NO], excel[Paths.NO2],
                                                                         excel[Paths.O3NO2], excel[Paths.Pressure],
                                                                         excel[Paths.Temperature],
                                                                         excel[Paths.Humidity]):
        st = date.split(" ")
        dmy = st[0].split("/")
        hms = st[1].split(":")
        obj = DataViewModel.Data()
        obj.CO = 0. if co == "Zero" else float(co)
        obj.NO = 0. if no == "Zero" else float(no)
        obj.NO2 = 0. if no2 == "Zero" else float(no2)
        obj.O3NO2 = 0. if o3no2 == "Zero" else float(o3no2)
        obj.Pressure = 0. if pressure == "Zero" else float(pressure)
        obj.Temperature = 0. if temperature == "Zero" else float(temperature)
        obj.Humidity = 0. if humidity == "Zero" else float(humidity)
        obj.Date_Time = date
        obj.Year = dmy[2]
        obj.Month = dmy[1]
        obj.Day = dmy[0]
        obj.Hour = hms[0]
        obj.Minute = hms[1]
        obj.Second = hms[2]

        result.append(obj)
        count += 1

    print(str(count) + " elements where found")

    return result


def NeaDataList():
    excel = pd.read_excel(Paths.NeaDirectory)
    result = []
    count = 0
    for date, co, no, no2, o3, pressure, temperature, in zip(excel[Paths.Nea_Date], excel[Paths.Nea_CO],
                                                             excel[Paths.Nea_NO], excel[Paths.Nea_NO2],
                                                             excel[Paths.Nea_O3], excel[Paths.Nea_Pressure],
                                                             excel[Paths.Nea_Temperature]):
        st = str(date).split(" ")
        dmy = st[0].split("-")
        hm = st[1].split(":")
        obj = DataViewModel.Data()
        obj.CO = 0. if co == "Zero" or co == "---" else float(co)
        obj.NO = 0. if no == "Zero" or no == "---" else float(no)
        obj.NO2 = 0. if no2 == "Zero" or no2 == "---" else float(no2)
        obj.O3NO2 = 0. if o3 == "Zero" or no2 == "Zero" or o3 == "---" else float(o3) + float(no2)
        obj.Pressure = 0. if pressure == "Zero" or pressure == "---" else float(pressure)
        obj.Temperature = 0. if temperature == "Zero" or temperature == "---" else float(temperature)
        obj.Humidity = 0.
        obj.Date_Time = date
        obj.Year = dmy[2]
        obj.Month = dmy[1]
        obj.Day = dmy[0]
        obj.Hour = hm[0]
        obj.Minute = hm[1]
        obj.Second = hm[2]

        result.append(obj)
        count += 1

    print(str(count) + " elements where found")

    return result


def ReadingAllMonth():
    dictionary = {}
    nea = []
    for sheet in Paths.sheets:
        print(sheet)
        day = []
        neaExcel = pd.read_excel(Paths.NeaDirectory, sheet_name=sheet)
        for date, co, no, no2, o3, pressure, temperature, in zip(neaExcel[Paths.Nea_Date], neaExcel[Paths.Nea_CO],
                                                                 neaExcel[Paths.Nea_NO], neaExcel[Paths.Nea_NO2],
                                                                 neaExcel[Paths.Nea_O3], neaExcel[Paths.Nea_Pressure],
                                                                 neaExcel[Paths.Nea_Temperature]):
            obj = DataViewModel.Data()
            obj.CO = 0. if not isfloat(co) else float(co)
            obj.NO = 0. if not isfloat(no) else float(no)
            obj.NO2 = 0. if not isfloat(no2) else float(no2)
            obj.O3NO2 = 0. if not isfloat(o3) or not isfloat(no2) else float(o3) + float(no2)
            obj.O3 = 0. if not isfloat(o3) else float(o3)
            obj.Pressure = 0. if not isfloat(pressure) else float(pressure)
            obj.Temperature = 0. if not isfloat(temperature) else float(temperature)
            obj.Humidity = 0.
            obj.Date_Time = date

            day.append(obj)
        nea.append(day)

    for name in Paths.excels:
        ls = name.split("\\")
        number = ls[len(ls) - 1].split(".")[0]
        key = number[len(number) - 2: len(number)]
        if key not in dictionary.keys():
            dictionary[key] = []
        print(key)
        excel = pd.read_excel(name)

        for date, co, no, no2, o3no2, pressure, temperature, humidity, O3 in zip(excel[Paths.Date], excel[Paths.CO],
                                                                                 excel[Paths.NO], excel[Paths.NO2],
                                                                                 excel[Paths.O3NO2],
                                                                                 excel[Paths.Pressure],
                                                                                 excel[Paths.Temperature],
                                                                                 excel[Paths.Humidity],
                                                                                 excel[Paths.O3]):
            obj = DataViewModel.Data()
            obj.CO = 0. if co == "Zero" else float(co)
            obj.NO = 0. if no == "Zero" else float(no)
            obj.NO2 = 0. if no2 == "Zero" else float(no2)
            obj.O3NO2 = 0. if o3no2 == "Zero" else float(o3no2)
            obj.Pressure = 0. if pressure == "Zero" else float(pressure)
            obj.Temperature = 0. if temperature == "Zero" else float(temperature)
            obj.Humidity = 0. if humidity == "Zero" else float(humidity)
            obj.Date_Time = date
            obj.O3 = 0. if O3 == "Zero" else float(O3)
            print(date)
            minute = str(date).split(" ")[1].split(":")[1]
            obj.Minute = minute
            dictionary[key].append(obj)

    keys = dictionary.keys()
    result = []
    for key in keys:
        result.append(dictionary[key])

    return result, nea


def ReadOmegas():
    file = pd.read_excel(Paths.ReadOmega)

    result = OmegasViewModel.Omegas()
    for CO_X, CO_Y, NO_X, NO_Y, NO2_X, NO2_Y, O3NO2_X, O3NO2_Y, O3_X, O3_Y, CO_S1, CO_S2, CO_S3, CO_S4, NO_S1, NO_S2, NO_S3, NO_S4, NO2_S1, NO2_S2, NO2_S3, NO2_S4, \
        O3_S1, O3_S2, O3_S3, O3_S4, O3NO2_S1, O3NO2_S2, O3NO2_S3, O3NO2_S4 in zip(
            file[Paths.CO_X], file[Paths.CO_Y], file[Paths.NO_X], file[Paths.NO_Y],
            file[Paths.NO2_X], file[Paths.NO2_Y], file[Paths.O3NO2_X], file[Paths.O3NO2_Y], file[Paths.O3_X],
            file[Paths.O3_Y], file[Paths.CO_S1], file[Paths.CO_S2], file[Paths.CO_S3], file[Paths.CO_S4], file[Paths.NO_S1], file[Paths.NO_S2], file[Paths.NO_S3], file[Paths.NO_S4],
            file[Paths.NO2_S1], file[Paths.NO2_S2], file[Paths.NO2_S3], file[Paths.NO2_S4],
            file[Paths.O3_S1], file[Paths.O3_S2], file[Paths.O3_S3], file[Paths.O3_S4], file[Paths.O3NO2_S1], file[Paths.O3_S2], file[Paths.O3NO2_S3], file[Paths.O3_S4]):
        result.CO_X.append(CO_X)
        result.CO_Y.append(CO_Y)
        result.NO_X.append(NO_X)
        result.NO_Y.append(NO_Y)
        result.NO2_X.append(NO2_X)
        result.NO2_Y.append(NO2_Y)
        result.O3NO2_X.append(O3NO2_X)
        result.O3NO2_Y.append(O3NO2_Y)
        result.O3_X.append(O3_X)
        result.O3_Y.append(O3_Y)
        result.CO_S.append((CO_S1, CO_S2, CO_S3, CO_S4))
        result.NO_S.append((NO_S1, NO_S2, NO_S3, NO_S4))
        result.NO2_S.append((NO2_S1, NO2_S2, NO2_S3, NO2_S4))
        result.O3_S.append((O3_S1, O3_S2, O3_S3, O3_S4))
        result.O3NO2_S.append((O3NO2_S1, O3NO2_S2, O3NO2_S3, O3NO2_S4))

    return result


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

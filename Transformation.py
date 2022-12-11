import Read
import DataViewModel


def SecondsToMinutes():
    data = Read.DataList()
    index = 0
    on = True
    result = []
    while on:
        counter = 0
        pos = index
        minute = data[pos].Minute
        CO = 0
        NO = 0
        NO2 = 0
        O3NO2 = 0
        Pressure = 0
        Temperature = 0
        Humidity = 0
        Day = ""
        Month = ""
        Year = ""
        Minute = ""
        Hour = ""
        Date_Time = ""
        for i in range(pos, len(data)):
            if data[i].Minute == minute:
                CO += data[i].CO
                NO += data[i].NO
                NO2 += data[i].NO2
                O3NO2 += data[i].O3NO2
                Pressure += data[i].Pressure
                Temperature += data[i].Temperature
                Humidity += data[i].Humidity
                Day = data[i].Day
                Month = data[i].Month
                Year = data[i].Year
                Minute = data[i].Minute
                Hour = data[i].Hour
                Date_Time = Day + "/" + Month + "/" + Year + " " + Hour + ":" + Minute + ":00"
                counter += 1
            else:
                index = i
                break

            if i == len(data) - 1:
                on = False
                break

        obj = DataViewModel.Data()
        obj.CO = CO / counter
        obj.NO = NO / counter
        obj.NO2 = NO2 / counter
        obj.O3NO2 = O3NO2 / counter
        obj.Pressure = Pressure / counter
        obj.Temperature = Temperature / counter
        obj.Humidity = Humidity / counter
        obj.Day = Day
        obj.Month = Month
        obj.Year = Year
        obj.Minute = Minute
        obj.Hour = Hour
        obj.Date_Time = Date_Time
        obj.Count = counter

        result.append(obj)

    return result


def GetSecondsFromMinute(data):
    index = 0
    on = True
    result = []

    while on:
        seconds = []
        pos = index
        minute = data[pos].Minute
        for i in range(pos, len(data)):
            if data[i].Minute == minute:
                seconds.append(data[i])
            else:
                index = i
                break

            if i == len(data) - 1:
                on = False
                break

        result.append(seconds)
    print(len(result), len(result[0]))
    return result



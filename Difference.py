import Error
import DifferenceViewModel


def Difference(MyData, NeaData):
    result = DifferenceViewModel.DifferenceModel()

    for m, n in zip(MyData, NeaData):
        result.RelCO.append(Error.Relative(m.CO, n.CO))
        result.RelNO.append(Error.Relative(m.NO, n.NO))
        result.RelNO2.append(Error.Relative(m.NO2, n.NO2))
        result.RelO3NO2.append(Error.Relative(m.O3NO2, n.O3NO2))
        result.RelTemperature.append(Error.Relative(m.Temperature, n.Temperature))
        result.RelHumidity.append(Error.Relative(m.Humidity, n.Humidity))
        result.RelPressure.append(Error.Relative(m.Pressure, n.Pressure))

        result.AbsCO.append(Error.Absolute(m.CO, n.CO))
        result.AbsNO.append(Error.Absolute(m.NO, n.NO))
        result.AbsNO2.append(Error.Absolute(m.NO2, n.NO2))
        result.AbsO3NO2.append(Error.Absolute(m.O3NO2, n.O3NO2))
        result.AbsTemperature.append(Error.Absolute(m.Temperature, n.Temperature))
        result.AbsHumidity.append(Error.Absolute(m.Humidity, n.Humidity))
        result.AbsPressure.append(Error.Absolute(m.Pressure, n.Pressure))

        result.Date_Time.append(m.Date_Time)

    return result

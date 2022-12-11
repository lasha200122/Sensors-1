import DataViewModel
import Transformation
import OmegasViewModel
import numpy as np
import ConditionVIewModel


def Omegas(myData, neaData):
    seconds = Transformation.GetSecondsFromMinute(myData)
    omegas = []
    for index, interval in enumerate(seconds):
        length = len(interval)
        start = 0
        middle = length // 2
        step = 0
        ls = []
        omegaPerMin = []

        while middle < length:
            ls.append(interval[start])
            ls.append(interval[middle])
            step += 1
            start += 1
            middle += 1

            if middle >= length and step != 2:
                ls.append(interval[start - 1])
                ls.append(interval[middle - 1])
                ls.append(neaData[index])
                omega = SolveLinearEquations(ls)
                omegaPerMin.append(omega)
                ls = []

            if step == 2:
                ls.append(neaData[index])
                omega = SolveLinearEquations(ls)
                omegaPerMin.append(omega)
                ls = []
                step = 0

        omegas.append((omegaPerMin, interval[0], interval[length // 2], neaData[index]))

    return omegas


def SolveLinearEquations(ls):
    x0 = ls[0]
    x1 = ls[1]
    x2 = ls[2]
    x3 = ls[3]
    x4 = ls[4]
    obj = DataViewModel.Data()

    CO2 = (x2.CO * x3.CO - x4.CO * x0.CO) / (x1.CO * x2.CO + x0.CO * x3.CO)
    CO1 = (x4.CO - x1.CO * CO2) / x0.CO
    obj.CO = CO1, CO2

    NO2 = (x2.NO * x3.NO - x4.NO * x0.NO) / (x1.NO * x2.NO + x0.NO * x3.NO)
    NO1 = (x4.NO - x1.NO * NO2) / x0.NO
    obj.NO = NO1, NO2

    NO22 = (x2.NO2 * x3.NO2 - x4.NO2 * x0.NO2) / (x1.NO2 * x2.NO2 + x0.NO2 * x3.NO2)
    NO21 = (x4.NO2 - x1.NO2 * NO22) / x0.NO2
    obj.NO2 = NO21, NO22

    O3NO22 = (x2.O3NO2 * x3.O3NO2 - x4.O3NO2 * x0.O3NO2) / (x1.O3NO2 * x2.O3NO2 + x0.O3NO2 * x3.O3NO2)
    O3NO21 = (x4.O3NO2 - x1.O3NO2 * O3NO22) / x0.O3NO2
    obj.O3NO2 = O3NO21, O3NO22

    Temperature2 = (x2.Temperature * x3.Temperature - x4.Temperature * x0.Temperature) / \
                   (x1.Temperature * x2.Temperature + x0.Temperature * x3.Temperature)
    Temperature1 = (x4.Temperature - x1.Temperature * Temperature2) / x0.Temperature
    obj.Temperature = Temperature1, Temperature2

    Pressure2 = (x2.Pressure * x3.Pressure - x4.Pressure * x0.Pressure) / (x1.Pressure * x2.Pressure +
                                                                           x0.Pressure * x3.Pressure)
    Pressure1 = (x4.Pressure - x1.Pressure * Pressure2) / x0.Pressure
    obj.Pressure = Pressure1, Pressure2

    Humidity2 = (x2.Humidity * x3.Humidity - x4.Humidity * x0.Humidity) / (x1.Humidity * x2.Humidity +
                                                                           x0.Humidity * x3.Humidity)
    Humidity1 = (x4.Humidity - x1.Humidity * Humidity2) / x0.Humidity
    obj.Humidity = Humidity1, Humidity2

    return obj


def LinearRegression(omegas):
    result = []
    for interval in omegas:
        interval = interval[0]
        n = len(interval)
        COx = sum([i.CO[0] for i in interval])
        COy = sum([i.CO[1] for i in interval])
        COxy = sum([i.CO[0] * i.CO[1] for i in interval])
        COx2 = sum([i.CO[0] * i.CO[0] for i in interval])

        COm = (n * COxy - COx * COy) / (n * COx2 - COx * COx)
        COb = (COy - COm * COx) / n

        NOx = sum([i.NO[0] for i in interval])
        NOy = sum([i.NO[1] for i in interval])
        NOxy = sum([i.NO[0] * i.NO[1] for i in interval])
        NOx2 = sum([i.NO[0] * i.NO[0] for i in interval])

        NOm = (n * NOxy - NOx * NOy) / (n * NOx2 - NOx * NOx)
        NOb = (NOy - NOm * NOx) / n

        NO2x = sum([i.NO2[0] for i in interval])
        NO2y = sum([i.NO2[1] for i in interval])
        NO2xy = sum([i.NO2[0] * i.NO2[1] for i in interval])
        NO2x2 = sum([i.NO2[0] * i.NO2[0] for i in interval])

        NO2m = (n * NO2xy - NO2x * NO2y) / (n * NO2x2 - NO2x * NO2x)
        NO2b = (NO2y - NO2m * NO2x) / n

        O3NO2x = sum([i.O3NO2[0] for i in interval])
        O3NO2y = sum([i.O3NO2[1] for i in interval])
        O3NO2xy = sum([i.O3NO2[0] * i.O3NO2[1] for i in interval])
        O3NO2x2 = sum([i.O3NO2[0] * i.O3NO2[0] for i in interval])

        O3NO2m = (n * O3NO2xy - O3NO2x * O3NO2y) / (n * O3NO2x2 - O3NO2x * O3NO2x)
        O3NO2b = (O3NO2y - O3NO2m * O3NO2x) / n

        obj = DataViewModel.Data()
        obj.CO = COm, COb
        obj.NO = NOm, NOb
        obj.NO2 = NO2m, NO2b
        obj.O3NO2 = O3NO2m, O3NO2b

        result.append(obj)
    return result


def GetRealValues(omegas, equations):
    result = []
    for index, omega in enumerate(omegas):
        omega1 = (omega[3].CO - omega[2].CO * equations[index].CO[1]) / (omega[1].CO + omega[2].CO *
                                                                         equations[index].CO[0])
        omega2 = omega1 * equations[index].CO[0] + equations[index].CO[1]
        result.append((omega1, omega2))
    return result


def SubInterval_4(myData, neaData):  # my data list of intervals [[obj1, obj....], ...] every second per day
    result = OmegasViewModel.Omegas()
    matrices = []
    for interval in myData:
        S1 = []
        S2 = []
        S3 = []
        S4 = []
        index = 0
        length = len(interval)
        while index < length:  # 4
            if index < length:
                S1.append(interval[index])
            if index + 1 < length:
                S2.append(interval[index + 1])
            if index + 2 < length:
                S3.append(interval[index + 2])
            if index + 3 < length:
                S4.append(interval[index + 3])
            index += 4
        coeff1 = DataViewModel.Data()
        coeff2 = DataViewModel.Data()
        coeff3 = DataViewModel.Data()
        coeff4 = DataViewModel.Data()
        coeff1.CO = 0
        coeff1.NO = 0
        coeff1.NO2 = 0
        coeff1.O3NO2 = 0
        coeff1.Pressure = 0
        coeff1.Temperature = 0
        coeff1.Humidity = 0
        coeff1.O3 = 0

        coeff2.CO = 0
        coeff2.NO = 0
        coeff2.NO2 = 0
        coeff2.O3NO2 = 0
        coeff2.Pressure = 0
        coeff2.Temperature = 0
        coeff2.Humidity = 0
        coeff2.O3 = 0

        coeff3.CO = 0
        coeff3.NO = 0
        coeff3.NO2 = 0
        coeff3.O3NO2 = 0
        coeff3.Pressure = 0
        coeff3.Temperature = 0
        coeff3.Humidity = 0
        coeff3.O3 = 0

        coeff4.CO = 0
        coeff4.NO = 0
        coeff4.NO2 = 0
        coeff4.O3NO2 = 0
        coeff4.Pressure = 0
        coeff4.Temperature = 0
        coeff4.Humidity = 0
        coeff4.O3 = 0


        for obj in S1:  # [obj1, obj2]
            coeff1.CO += obj.CO
            coeff1.NO += obj.NO
            coeff1.NO2 += obj.NO2
            coeff1.O3NO2 += obj.O3NO2
            coeff1.Pressure += obj.Pressure
            coeff1.Temperature += obj.Temperature
            coeff1.Humidity += obj.Humidity
            coeff1.O3 += obj.O3
        if (len(S1) != 0):
            coeff1.CO /= len(S1)
            coeff1.NO /= len(S1)
            coeff1.NO2 /= len(S1)
            coeff1.O3NO2 /= len(S1)
            coeff1.Pressure /= len(S1)
            coeff1.Temperature /= len(S1)
            coeff1.Humidity /= len(S1)
            coeff1.O3 /= len(S1)

        for obj in S2:
            coeff2.CO += obj.CO
            coeff2.NO += obj.NO
            coeff2.NO2 += obj.NO2
            coeff2.O3NO2 += obj.O3NO2
            coeff2.Pressure += obj.Pressure
            coeff2.Temperature += obj.Temperature
            coeff2.Humidity += obj.Humidity
            coeff2.O3 += obj.O3

        if (len(S2) != 0):
            coeff2.CO /= len(S2)
            coeff2.NO /= len(S2)
            coeff2.NO2 /= len(S2)
            coeff2.O3NO2 /= len(S2)
            coeff2.Pressure /= len(S2)
            coeff2.Temperature /= len(S2)
            coeff2.Humidity /= len(S2)
            coeff2.O3 /= len(S2)

        for obj in S3:
            coeff3.CO += obj.CO
            coeff3.NO += obj.NO
            coeff3.NO2 += obj.NO2
            coeff3.O3NO2 += obj.O3NO2
            coeff3.Pressure += obj.Pressure
            coeff3.Temperature += obj.Temperature
            coeff3.Humidity += obj.Humidity
            coeff3.O3 += obj.O3

        if (len(S3) != 0):
            coeff3.CO /= len(S3)
            coeff3.NO /= len(S3)
            coeff3.NO2 /= len(S3)
            coeff3.O3NO2 /= len(S3)
            coeff3.Pressure /= len(S3)
            coeff3.Temperature /= len(S3)
            coeff3.Humidity /= len(S3)
            coeff3.O3 /= len(S3)

        for obj in S4:
            coeff4.CO += obj.CO
            coeff4.NO += obj.NO
            coeff4.NO2 += obj.NO2
            coeff4.O3NO2 += obj.O3NO2
            coeff4.Pressure += obj.Pressure
            coeff4.Temperature += obj.Temperature
            coeff4.Humidity += obj.Humidity
            coeff4.O3 += obj.O3

        if (len(S4) != 0):
            coeff4.CO /= len(S4)
            coeff4.NO /= len(S4)
            coeff4.NO2 /= len(S4)
            coeff4.O3NO2 /= len(S4)
            coeff4.Pressure /= len(S4)
            coeff4.Temperature /= len(S4)
            coeff4.Humidity /= len(S4)
            coeff4.O3 /= len(S4)
        matrices.append([coeff1, coeff2, coeff3, coeff4, interval])
    print("Matrix length: " + str(len(matrices)))
    for index, equation in enumerate(matrices):
        CO_X, CO_Y = Solver(equation[0].CO, equation[1].CO, equation[2].CO, equation[3].CO, neaData[index].CO)
        NO_X, NO_Y = Solver(equation[0].NO, equation[1].NO, equation[2].NO, equation[3].NO, neaData[index].NO)
        NO2_X, NO2_Y = Solver(equation[0].NO2, equation[1].NO2, equation[2].NO2, equation[3].NO2, neaData[index].NO2)
        O3NO2_X, O3NO2_Y = Solver(equation[0].O3NO2, equation[1].O3NO2, equation[2].O3NO2, equation[3].O3NO2,
                                  neaData[index].O3NO2)
        Temperature_X, Temperature_Y = Solver(equation[0].Temperature, equation[1].Temperature, equation[2].Temperature,
                                              equation[3].Temperature, neaData[index].Temperature)
        Pressure_X, Pressure_Y = Solver(equation[0].Pressure, equation[1].Pressure, equation[2].Pressure,
                                        equation[3].Pressure, neaData[index].Pressure)
        Humidity_X, Humidity_Y = Solver(equation[0].Humidity, equation[1].Humidity, equation[2].Humidity,
                                        equation[3].Humidity, neaData[index].Humidity)
        O3_X, O3_Y = Solver(equation[0].O3, equation[1].O3, equation[2].O3, equation[3].O3, neaData[index].O3)

        #  Calculating S
        # CO_S1 = (equation[0].CO + equation[1].CO) / 2
        # CO_S2 = (equation[2].CO + equation[3].CO) / 2
        # NO_S1 = (equation[0].NO + equation[1].NO) / 2
        # NO_S2 = (equation[2].NO + equation[3].NO) / 2
        # NO2_S1 = (equation[0].NO2 + equation[1].NO2) / 2
        # NO2_S2 = (equation[2].NO2 + equation[3].NO2) / 2
        # O3_S1 = (equation[0].O3 + equation[1].O3) / 2
        # O3_S2 = (equation[2].O3 + equation[3].O3) / 2
        # O3NO2_S1 = (equation[0].O3NO2 + equation[1].O3NO2) / 2
        # O3NO2_S2 = (equation[2].O3NO2 + equation[3].O3NO2) / 2

        result.CO_X.append(CO_X)
        result.CO_Y.append(CO_Y)
        result.NO_X.append(NO_X)
        result.NO_Y.append(NO_Y)
        result.NO2_X.append(NO2_X)
        result.NO2_Y.append(NO2_Y)
        result.O3NO2_X.append(O3NO2_X)
        result.O3NO2_Y.append(O3NO2_Y)
        result.Temperature_X.append(Temperature_X)
        result.Temperature_Y.append(Temperature_Y)
        result.Humidity_X.append(Humidity_X)
        result.Humidity_Y.append(Humidity_Y)
        result.Pressure_X.append(Pressure_X)
        result.Pressure_Y.append(Pressure_Y)
        result.O3_X.append(O3_X)
        result.O3_Y.append(O3_Y)
        result.CO_S.append((equation[0].CO, equation[1].CO, equation[2].CO, equation[3].CO))
        result.NO_S.append((equation[0].NO, equation[1].NO, equation[2].NO, equation[3].NO))
        result.NO2_S.append((equation[0].NO2, equation[1].NO2, equation[2].NO2, equation[3].NO2))
        result.O3NO2_S.append((equation[0].O3NO2, equation[1].O3NO2, equation[2].O3NO2, equation[3].O3NO2))
        result.O3_S.append((equation[0].O3, equation[1].O3, equation[2].O3, equation[3].O3))
        result.Intervals.append(equation[4])

    print("length of CO_X" + str(len(result.CO_X)))
    return result


def Solver(c1, c2, c3, c4, b):
    matrix = np.array([[c1, c2], [c3, c4]])
    if np.linalg.det(matrix) == 0:
        return 0, 0
    B = np.array([[b], [b]])
    result = np.linalg.solve(matrix, B)  # [w1, w2]
    return result[0], result[1]


def distance(a, b):
    return np.sqrt(np.power(a, 2) + np.power(b, 2))


def ConditionNumbers(myData, n):
    conditions = ConditionVIewModel.Conditions()
    for interval in myData:
        S1 = []
        S2 = []
        S3 = []
        S4 = []
        index = 0
        length = len(interval)
        while index < length - 4:
            if index < length:
                S1.append(interval[index])
            if index + 1 < length:
                S2.append(interval[index + 1])
            if index + 2 < length:
                S3.append(interval[index + 2])
            if index + 3 < length:
                S4.append(interval[index + 3])
            index += 4
        coeff1 = DataViewModel.Data()
        coeff2 = DataViewModel.Data()
        coeff3 = DataViewModel.Data()
        coeff4 = DataViewModel.Data()
        coeff1.CO = 0
        coeff1.NO = 0
        coeff1.NO2 = 0
        coeff1.O3NO2 = 0
        coeff1.Pressure = 0
        coeff1.Temperature = 0
        coeff1.Humidity = 0
        coeff1.O3 = 0

        coeff2.CO = 0
        coeff2.NO = 0
        coeff2.NO2 = 0
        coeff2.O3NO2 = 0
        coeff2.Pressure = 0
        coeff2.Temperature = 0
        coeff2.Humidity = 0
        coeff2.O3 = 0

        coeff3.CO = 0
        coeff3.NO = 0
        coeff3.NO2 = 0
        coeff3.O3NO2 = 0
        coeff3.Pressure = 0
        coeff3.Temperature = 0
        coeff3.Humidity = 0
        coeff3.O3 = 0

        coeff4.CO = 0
        coeff4.NO = 0
        coeff4.NO2 = 0
        coeff4.O3NO2 = 0
        coeff4.Pressure = 0
        coeff4.Temperature = 0
        coeff4.Humidity = 0
        coeff4.O3 = 0

        for obj in S1:
            coeff1.CO += obj.CO
            coeff1.NO += obj.NO
            coeff1.NO2 += obj.NO2
            coeff1.O3NO2 += obj.O3NO2
            coeff1.Pressure += obj.Pressure
            coeff1.Temperature += obj.Temperature
            coeff1.Humidity += obj.Humidity
            coeff1.O3 += obj.O3
        coeff1.CO /= len(S1)
        coeff1.NO /= len(S1)
        coeff1.NO2 /= len(S1)
        coeff1.O3NO2 /= len(S1)
        coeff1.Pressure /= len(S1)
        coeff1.Temperature /= len(S1)
        coeff1.Humidity /= len(S1)
        coeff1.O3 /= len(S1)

        for obj in S2:
            coeff2.CO += obj.CO
            coeff2.NO += obj.NO
            coeff2.NO2 += obj.NO2
            coeff2.O3NO2 += obj.O3NO2
            coeff2.Pressure += obj.Pressure
            coeff2.Temperature += obj.Temperature
            coeff2.Humidity += obj.Humidity
            coeff2.O3 += obj.O3
        coeff2.CO /= len(S2)
        coeff2.NO /= len(S2)
        coeff2.NO2 /= len(S2)
        coeff2.O3NO2 /= len(S2)
        coeff2.Pressure /= len(S2)
        coeff2.Temperature /= len(S2)
        coeff2.Humidity /= len(S2)
        coeff2.O3 /= len(S2)

        for obj in S3:
            coeff3.CO += obj.CO
            coeff3.NO += obj.NO
            coeff3.NO2 += obj.NO2
            coeff3.O3NO2 += obj.O3NO2
            coeff3.Pressure += obj.Pressure
            coeff3.Temperature += obj.Temperature
            coeff3.Humidity += obj.Humidity
            coeff3.O3 += obj.O3
        coeff3.CO /= len(S3)
        coeff3.NO /= len(S3)
        coeff3.NO2 /= len(S3)
        coeff3.O3NO2 /= len(S3)
        coeff3.Pressure /= len(S3)
        coeff3.Temperature /= len(S3)
        coeff3.Humidity /= len(S3)
        coeff3.O3 /= len(S3)

        for obj in S4:
            coeff4.CO += obj.CO
            coeff4.NO += obj.NO
            coeff4.NO2 += obj.NO2
            coeff4.O3NO2 += obj.O3NO2
            coeff4.Pressure += obj.Pressure
            coeff4.Temperature += obj.Temperature
            coeff4.Humidity += obj.Humidity
            coeff4.O3 += obj.O3
        coeff4.CO /= len(S4)
        coeff4.NO /= len(S4)
        coeff4.NO2 /= len(S4)
        coeff4.O3NO2 /= len(S4)
        coeff4.Pressure /= len(S4)
        coeff4.Temperature /= len(S4)
        coeff4.Humidity /= len(S4)
        coeff4.O3 /= len(S4)
        COM = np.array([[coeff1.CO, coeff2.CO], [coeff3.CO, coeff4.CO]])
        NOM = np.array([[coeff1.NO, coeff2.NO], [coeff3.NO, coeff4.NO]])
        NO2M = np.array([[coeff1.NO2, coeff2.NO2], [coeff3.NO2, coeff4.NO2]])
        O3M = np.array([[coeff1.O3, coeff2.O3], [coeff3.O3, coeff4.O3]])
        O3NO2M = np.array([[coeff1.O3NO2, coeff2.O3NO2], [coeff3.O3NO2, coeff4.O3NO2]])
        conditions.CO.append(np.linalg.norm(COM, ord=n) * np.linalg.norm(np.linalg.inv(COM), ord=n))
        conditions.NO.append(np.linalg.norm(NOM, ord=n) * np.linalg.norm(np.linalg.inv(NOM), ord=n))
        conditions.NO2.append(np.linalg.norm(NO2M, ord=n) * np.linalg.norm(np.linalg.inv(NO2M), ord=n))
        conditions.O3.append(np.linalg.norm(O3M, ord=n) * np.linalg.norm(np.linalg.inv(O3M), ord=n))
        conditions.O3NO2.append(np.linalg.norm(O3NO2M, ord=n) * np.linalg.norm(np.linalg.inv(O3NO2M), ord=n))

    return conditions


def UpperBound(myData, nea, epsilon, n):
    nea = [item for sublist in nea for item in sublist]
    bounds = ConditionVIewModel.Conditions()
    for i, interval in enumerate(myData):
        S1 = []
        S2 = []
        S3 = []
        S4 = []
        index = 0
        length = len(interval)
        while index < length:
            if index < length:
                S1.append(interval[index])
            if index + 1 < length:
                S2.append(interval[index + 1])
            if index + 2 < length:
                S3.append(interval[index + 2])
            if index + 3 < length:
                S4.append(interval[index + 3])
            index += 4
        coeff1 = DataViewModel.Data()
        coeff2 = DataViewModel.Data()
        coeff3 = DataViewModel.Data()
        coeff4 = DataViewModel.Data()
        coeff1.CO = 0
        coeff1.NO = 0
        coeff1.NO2 = 0
        coeff1.O3NO2 = 0
        coeff1.Pressure = 0
        coeff1.Temperature = 0
        coeff1.Humidity = 0
        coeff1.O3 = 0

        coeff2.CO = 0
        coeff2.NO = 0
        coeff2.NO2 = 0
        coeff2.O3NO2 = 0
        coeff2.Pressure = 0
        coeff2.Temperature = 0
        coeff2.Humidity = 0
        coeff2.O3 = 0

        coeff3.CO = 0
        coeff3.NO = 0
        coeff3.NO2 = 0
        coeff3.O3NO2 = 0
        coeff3.Pressure = 0
        coeff3.Temperature = 0
        coeff3.Humidity = 0
        coeff3.O3 = 0

        coeff4.CO = 0
        coeff4.NO = 0
        coeff4.NO2 = 0
        coeff4.O3NO2 = 0
        coeff4.Pressure = 0
        coeff4.Temperature = 0
        coeff4.Humidity = 0
        coeff4.O3 = 0

        for obj in S1:
            coeff1.CO += obj.CO
            coeff1.NO += obj.NO
            coeff1.NO2 += obj.NO2
            coeff1.O3NO2 += obj.O3NO2
            coeff1.Pressure += obj.Pressure
            coeff1.Temperature += obj.Temperature
            coeff1.Humidity += obj.Humidity
            coeff1.O3 += obj.O3
        coeff1.CO /= len(S1)
        coeff1.NO /= len(S1)
        coeff1.NO2 /= len(S1)
        coeff1.O3NO2 /= len(S1)
        coeff1.Pressure /= len(S1)
        coeff1.Temperature /= len(S1)
        coeff1.Humidity /= len(S1)
        coeff1.O3 /= len(S1)

        for obj in S2:
            coeff2.CO += obj.CO
            coeff2.NO += obj.NO
            coeff2.NO2 += obj.NO2
            coeff2.O3NO2 += obj.O3NO2
            coeff2.Pressure += obj.Pressure
            coeff2.Temperature += obj.Temperature
            coeff2.Humidity += obj.Humidity
            coeff2.O3 += obj.O3
        coeff2.CO /= len(S2)
        coeff2.NO /= len(S2)
        coeff2.NO2 /= len(S2)
        coeff2.O3NO2 /= len(S2)
        coeff2.Pressure /= len(S2)
        coeff2.Temperature /= len(S2)
        coeff2.Humidity /= len(S2)
        coeff2.O3 /= len(S2)

        for obj in S3:
            coeff3.CO += obj.CO
            coeff3.NO += obj.NO
            coeff3.NO2 += obj.NO2
            coeff3.O3NO2 += obj.O3NO2
            coeff3.Pressure += obj.Pressure
            coeff3.Temperature += obj.Temperature
            coeff3.Humidity += obj.Humidity
            coeff3.O3 += obj.O3
        coeff3.CO /= len(S3)
        coeff3.NO /= len(S3)
        coeff3.NO2 /= len(S3)
        coeff3.O3NO2 /= len(S3)
        coeff3.Pressure /= len(S3)
        coeff3.Temperature /= len(S3)
        coeff3.Humidity /= len(S3)
        coeff3.O3 /= len(S3)

        for obj in S4:
            coeff4.CO += obj.CO
            coeff4.NO += obj.NO
            coeff4.NO2 += obj.NO2
            coeff4.O3NO2 += obj.O3NO2
            coeff4.Pressure += obj.Pressure
            coeff4.Temperature += obj.Temperature
            coeff4.Humidity += obj.Humidity
            coeff4.O3 += obj.O3
        coeff4.CO /= len(S4)
        coeff4.NO /= len(S4)
        coeff4.NO2 /= len(S4)
        coeff4.O3NO2 /= len(S4)
        coeff4.Pressure /= len(S4)
        coeff4.Temperature /= len(S4)
        coeff4.Humidity /= len(S4)
        coeff4.O3 /= len(S4)



        # COM = np.linalg.inv(np.array([[coeff1.CO, coeff2.CO], [coeff3.CO, coeff4.CO]]))
        # NOM = np.linalg.inv(np.array([[coeff1.NO, coeff2.NO], [coeff3.NO, coeff4.NO]]))
        # NO2M = np.linalg.inv(np.array([[coeff1.NO2, coeff2.NO2], [coeff3.NO2, coeff4.NO2]]))
        # O3M = np.linalg.inv(np.array([[coeff1.O3, coeff2.O3], [coeff3.O3, coeff4.O3]]))
        # O3NO2M = np.linalg.inv(np.array([[coeff1.O3NO2, coeff2.O3NO2], [coeff3.O3NO2, coeff4.O3NO2]]))
        #
        # COb = nea[i].CO
        # NOb = nea[i].NO
        # NO2b = nea[i].NO2
        # O3b = nea[i].O3
        # O3NO2b = nea[i].O3NO2
        #
        # rCO = np.array(COb) - np.matmul(COM, np.array(epsilon))
        # rNO = np.array(NOb) - np.matmul(NOM, np.array(epsilon))
        # rNO2 = np.array(NO2b) - np.matmul(NO2M, np.array(epsilon))
        # rO3 = np.array(O3b) - np.matmul(O3M, np.array(epsilon))
        # rO3NO2 = np.array(O3NO2b) - np.matmul(O3NO2M, np.array(epsilon))
        #
        # CObound = np.linalg.norm(COM, ord=n) * np.linalg.norm(rCO, ord=n)
        # NObound = np.linalg.norm(NOM, ord=n) * np.linalg.norm(rNO, ord=n)
        # NO2bound = np.linalg.norm(NO2M, ord=n) * np.linalg.norm(rNO2, ord=n)
        # O3bound = np.linalg.norm(O3M, ord=n) * np.linalg.norm(rO3, ord=n)
        # O3NO2bound = np.linalg.norm(O3NO2M, ord=n) * np.linalg.norm(rO3NO2, ord=n)
        #
        # bounds.CO.append(CObound)
        # bounds.NO.append(NObound)
        # bounds.NO2.append(NO2bound)
        # bounds.O3.append(O3bound)
        # bounds.O3NO2.append(O3NO2bound)

    return bounds


def LR(X, Y):
    n = len(X)
    xx = sum([i*i for i in X])
    sx = sum([i for i in X])
    sx2 = sx * sx
    xy = sum(X[i] * Y[i] for i in range(n))
    xpy = sum([i for i in X]) * sum([i for i in Y])
    x = sum([i for i in X])
    y = sum([i for i in Y])
    m = (n * xy - xpy) / (n * xx - sx2)
    b = (y - m * x) / n
    return m, b


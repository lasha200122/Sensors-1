import Transformation
import Paths
import xlsxwriter


def SaveSecondsToMinutes():
    data = Transformation.SecondsToMinutes()

    ls = Paths.directory.split("\\")
    fileName = ls[len(ls) - 1]
    fullPath = Paths.SaveTo + fileName

    workbook = xlsxwriter.Workbook(fullPath)
    worksheet = workbook.add_worksheet()

    worksheet.write("A1", Paths.Date)
    worksheet.write("B1", Paths.CO)
    worksheet.write("C1", Paths.NO)
    worksheet.write("D1", Paths.NO2)
    worksheet.write("E1", Paths.O3NO2)
    worksheet.write("F1", Paths.Pressure)
    worksheet.write("G1", Paths.Temperature)
    worksheet.write("H1", Paths.Humidity)
    worksheet.write("I1", Paths.Count)

    row = 2

    for obj in data:
        worksheet.write("A" + str(row), obj.Date_Time)
        worksheet.write("B" + str(row), obj.CO)
        worksheet.write("C" + str(row), obj.NO)
        worksheet.write("D" + str(row), obj.NO2)
        worksheet.write("E" + str(row), obj.O3NO2)
        worksheet.write("F" + str(row), obj.Pressure)
        worksheet.write("G" + str(row), obj.Temperature)
        worksheet.write("H" + str(row), obj.Humidity)
        worksheet.write("I" + str(row), obj.Count)

        row += 1

    workbook.close()


def SaveOmegas(data):
    fullPath = Paths.OmegaPath + "Omegas.xlsx"

    workbook = xlsxwriter.Workbook(fullPath)
    worksheet = workbook.add_worksheet()

    worksheet.write("A1", Paths.CO_X)
    worksheet.write("B1", Paths.CO_Y)
    worksheet.write("C1", Paths.NO_X)
    worksheet.write("D1", Paths.NO_Y)
    worksheet.write("E1", Paths.NO2_X)
    worksheet.write("F1", Paths.NO2_Y)
    worksheet.write("G1", Paths.O3NO2_X)
    worksheet.write("H1", Paths.O3NO2_Y)
    worksheet.write("I1", Paths.O3_X)
    worksheet.write("J1", Paths.O3_Y)
    worksheet.write("K1", Paths.CO_S1)
    worksheet.write("L1", Paths.CO_S2)
    worksheet.write("M1", Paths.CO_S3)
    worksheet.write("N1", Paths.CO_S4)
    worksheet.write("O1", Paths.NO_S1)
    worksheet.write("P1", Paths.NO_S2)
    worksheet.write("Q1", Paths.NO_S3)
    worksheet.write("R1", Paths.NO_S4)
    worksheet.write("S1", Paths.NO2_S1)
    worksheet.write("T1", Paths.NO2_S2)
    worksheet.write("U1", Paths.NO2_S3)
    worksheet.write("V1", Paths.NO2_S4)
    worksheet.write("W1", Paths.O3_S1)
    worksheet.write("X1", Paths.O3_S2)
    worksheet.write("Y1", Paths.O3_S3)
    worksheet.write("Z1", Paths.O3_S4)
    worksheet.write("AB1", Paths.O3NO2_S1)
    worksheet.write("AC1", Paths.O3NO2_S2)
    worksheet.write("AD1", Paths.O3NO2_S3)
    worksheet.write("AE1", Paths.O3NO2_S4)

    worksheet.write("AF1", Paths.CO_S)
    worksheet.write("AG1", Paths.NO_S)
    worksheet.write("AH1", Paths.NO2_S)
    worksheet.write("AI1", Paths.O3_S)
    worksheet.write("AJ1", Paths.O3NO2_S)

    row = 2
    print()
    print(len(data.CO_X))
    print(len(data.NO_X))
    print(len(data.NO2_X))
    print(len(data.O3_X))
    print(len(data.O3NO2_X))
    print(len(data.Intervals))

    for CO_X, CO_Y, NO_X, NO_Y, NO2_X, NO2_Y, O3NO2_X, O3NO2_Y, O3_X, O3_Y, CO_S, NO_S, NO2_S, O3_S, O3NO2_S, obj in zip(
            data.CO_X, data.CO_Y, data.NO_X, data.NO_Y, data.NO2_X, data.NO2_Y, data.O3NO2_X, data.O3NO2_Y, data.O3_X,
            data.O3_Y, data.CO_S, data.NO_S, data.NO2_S, data.O3_S, data.O3NO2_S, data.Intervals):

        worksheet.write("A" + str(row), CO_X)
        worksheet.write("B" + str(row), CO_Y)
        worksheet.write("C" + str(row), NO_X)
        worksheet.write("D" + str(row), NO_Y)
        worksheet.write("E" + str(row), NO2_X)
        worksheet.write("F" + str(row), NO2_Y)
        worksheet.write("G" + str(row), O3NO2_X)
        worksheet.write("H" + str(row), O3NO2_Y)
        worksheet.write("I" + str(row), O3_X)
        worksheet.write("J" + str(row), O3_Y)
        worksheet.write("K" + str(row), CO_S[0])
        worksheet.write("L" + str(row), CO_S[1])
        worksheet.write("M" + str(row), CO_S[2])
        worksheet.write("N" + str(row), CO_S[3])
        worksheet.write("O" + str(row), NO_S[0])
        worksheet.write("P" + str(row), NO_S[1])
        worksheet.write("Q" + str(row), NO_S[2])
        worksheet.write("R" + str(row), NO_S[3])
        worksheet.write("S" + str(row), NO2_S[0])
        worksheet.write("T" + str(row), NO2_S[1])
        worksheet.write("U" + str(row), NO2_S[2])
        worksheet.write("V" + str(row), NO2_S[3])
        worksheet.write("W" + str(row), O3_S[0])
        worksheet.write("X" + str(row), O3_S[1])
        worksheet.write("Y" + str(row), O3_S[2])
        worksheet.write("Z" + str(row), O3_S[3])
        worksheet.write("AB" + str(row), O3NO2_S[0])
        worksheet.write("AC" + str(row), O3NO2_S[1])
        worksheet.write("AD" + str(row), O3NO2_S[2])
        worksheet.write("AE" + str(row), O3NO2_S[3])
        worksheet.write("AF" + str(row), ",".join([str(i.CO) for i in obj]))
        worksheet.write("AG" + str(row), ",".join([str(i.NO) for i in obj]))
        worksheet.write("AH" + str(row), ",".join([str(i.NO2) for i in obj]))
        worksheet.write("AI" + str(row), ",".join([str(i.O3) for i in obj]))
        worksheet.write("AJ" + str(row), ",".join([str(i.O3NO2) for i in obj]))
        row += 1
        print(row)

    workbook.close()


def SaveConditions(data):
    fullPath = Paths.Condition

    workbook = xlsxwriter.Workbook(fullPath)
    worksheet = workbook.add_worksheet()

    worksheet.write("A1", Paths.CO)
    worksheet.write("B1", Paths.NO)
    worksheet.write("C1", Paths.NO2)
    worksheet.write("D1", Paths.O3)
    worksheet.write("E1", Paths.O3NO2)

    row = 2

    for CO, NO, NO2, O3, O3NO2 in zip(
            data.CO, data.NO, data.NO2, data.O3, data.O3NO2):

        worksheet.write("A" + str(row), CO)
        worksheet.write("B" + str(row), NO)
        worksheet.write("C" + str(row), NO2)
        worksheet.write("D" + str(row), O3)
        worksheet.write("E" + str(row), O3NO2)

        row += 1

    workbook.close()


def SaveBounds(data):
    fullPath = Paths.Bounds

    workbook = xlsxwriter.Workbook(fullPath)
    worksheet = workbook.add_worksheet()

    worksheet.write("A1", Paths.CO)
    worksheet.write("B1", Paths.NO)
    worksheet.write("C1", Paths.NO2)
    worksheet.write("D1", Paths.O3)
    worksheet.write("E1", Paths.O3NO2)

    row = 2

    for CO, NO, NO2, O3, O3NO2 in zip(
            data.CO, data.NO, data.NO2, data.O3, data.O3NO2):

        worksheet.write("A" + str(row), CO)
        worksheet.write("B" + str(row), NO)
        worksheet.write("C" + str(row), NO2)
        worksheet.write("D" + str(row), O3)
        worksheet.write("E" + str(row), O3NO2)

        row += 1

    workbook.close()

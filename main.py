import random

import ConditionVIewModel
import Norm
import OmegasViewModel
import Read
import Difference
import Print
import Plot
import Paths
import Logic
import Save
import Transformation
import KMean
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

def line(x, k, h):
    return k * x + h

if __name__ == '__main__':
    # //////////////// From 24 December to 6 January //////////////////
    # allData, nea = Read.ReadingAllMonth()
    # print(len(allData), len(nea))
    # print(len(allData[0]))

    # result = ConditionVIewModel.Conditions()
    # Condition Numbers
    # for index, d in enumerate(allData):
    #     data = Transformation.GetSecondsFromMinute(d)
    #     coefficients = Logic.UpperBound(data, nea, [[1], [1]], 2)
    #     result.CO += coefficients.CO
    #     result.NO += coefficients.NO
    #     result.NO2 += coefficients.NO2
    #     result.O3 += coefficients.O3
    #     result.O3NO2 += coefficients.O3NO2
    #
    # plt.title("CO Error upper bound norm_2")
    # plt.scatter([i for i in range(len(result.CO))], result.CO, s=0.3)
    # plt.show()
    #
    # plt.title("NO Error upper bound norm_2")
    # plt.scatter([i for i in range(len(result.NO))], result.NO, s=0.3)
    # plt.show()
    #
    # plt.title("NO2 Error upper bound norm_2")
    # plt.scatter([i for i in range(len(result.NO2))], result.NO2, s=0.3)
    # plt.show()
    #
    # plt.title("O3 Error upper bound norm_2")
    # plt.scatter([i for i in range(len(result.O3))], result.O3, s=0.3)
    # plt.show()
    #
    # plt.title("O3NO2 Error upper bound norm_2")
    # plt.scatter([i for i in range(len(result.O3NO2))], result.O3NO2, s=0.3)
    # plt.show()
    #
    # Save.SaveBounds(result)
    # MyData = Read.DataList()
    # NeaData = Read.NeaDataList()
    # omegas = Logic.Omegas(MyData, NeaData)
    # LinearEquations = Logic.LinearRegression(omegas)

    # realValues = Logic.GetRealValues(omegas, LinearEquations)
    #
    #
    # result = OmegasViewModel.Omegas()
    # for index, d in enumerate(allData):
    #     secondsInterval = Transformation.GetSecondsFromMinute(d)
    #     coefficients = Logic.SubInterval_4(secondsInterval, nea[index])
    #
    # Save.SaveOmegas(result)

    # for index, interval in enumerate(seconds):
    #     start = 0
    #     middle = len(interval) // 2
    #     while middle < len(interval):
    #         value = realValues[index][0] * interval[start].CO + realValues[index][1] * interval[middle].CO
    #         middle += 1
    #         start += 1
    #         print(value)
    #     print("-----------------------------------------")
    #     print()

    # errorModel = Difference.Difference(MyData, NeaData)
    #
    # Plot.Visualize(errorModel.AbsCO, Paths.CO_ABS)

    # Print.Info(MyData, NeaData)

    # To Transform Seconds in to minutes and save as xlsx file remove comment tags from "import Save" and code below
    # Save.SaveSecondsToMinutes()



    # ------ K Means Part
    omegas = Read.ReadOmegas()
    #

    x = np.array(omegas.CO_X).reshape((-1, 1))
    y = np.array(omegas.CO_Y)

    model = LinearRegression().fit(x, y)
    newy = model.predict(x)
    plt.plot([i for i in range(len(newy))], abs(newy - y), color='red')
    plt.title("CO error")
    plt.show()

    x = np.array(omegas.NO_X).reshape((-1, 1))
    y = np.array(omegas.NO_Y)

    model = LinearRegression().fit(x, y)
    newy = model.predict(x)
    plt.plot([i for i in range(len(newy))], abs(newy - y), color='red')
    plt.title("NO error")
    plt.show()

    x = np.array(omegas.NO2_X).reshape((-1, 1))
    y = np.array(omegas.NO2_Y)

    model = LinearRegression().fit(x, y)
    newy = model.predict(x)
    plt.plot([i for i in range(len(newy))], abs(newy - y), color='red')
    plt.title("NO2 error")
    plt.show()


    x = np.array(omegas.O3_X).reshape((-1, 1))
    y = np.array(omegas.O3_Y)

    model = LinearRegression().fit(x, y)
    newy = model.predict(x)
    plt.plot([i for i in range(len(newy))], abs(newy - y), color='red')
    plt.title("O3 error")
    plt.show()


    x = np.array(omegas.O3NO2_X).reshape((-1, 1))
    y = np.array(omegas.O3NO2_Y)

    model = LinearRegression().fit(x, y)
    newy = model.predict(x)
    plt.plot([i for i in range(len(newy))], abs(newy - y), color='red')
    plt.title("O3NO2 error")
    plt.show()
    # #  Linear Regression
    #
    # m, b = Logic.LR(omegas.CO_X, omegas.CO_Y)
    # newY = line(np.array(omegas.CO_X), m, b)
    # error_n1 = Norm.NormP(np.array(omegas.CO_Y) - newY, 1)
    # error_n2 = Norm.NormP(np.array(omegas.CO_Y) - newY, 2)
    # error_n3 = Norm.NormP(np.array(omegas.CO_Y) - newY, "inf")
    # difference = abs(newY - omegas.CO_Y)
    # plt.title("CO error")
    # plt.plot([i for i in range(len(omegas.CO_X))], difference, color='red')
    # plt.show()
    # print("Norm 1: " + str(error_n1))
    # print("Norm 2: " + str(error_n2))
    # print("Norm inf: " + str(error_n3))
    # plt.title("CO compare")
    # plt.plot(omegas.CO_X, omegas.CO_Y)
    # plt.plot(omegas.CO_X, newY)
    # plt.show()
    #
    # m, b = Logic.LR(omegas.NO_X, omegas.NO_Y)
    # newY = line(np.array(omegas.NO_X), m, b)
    # error_n1 = Norm.NormP(np.array(omegas.NO_Y) - newY, 1)
    # error_n2 = Norm.NormP(np.array(omegas.NO_Y) - newY, 2)
    # error_n3 = Norm.NormP(np.array(omegas.NO_Y) - newY, "inf")
    # difference = abs(newY - omegas.NO_Y)
    # plt.title("NO error")
    # plt.plot([i for i in range(len(omegas.NO_X))], difference, color='red')
    # plt.show()
    # print("Norm 1: " + str(error_n1))
    # print("Norm 2: " + str(error_n2))
    # print("Norm inf: " + str(error_n3))
    # plt.title("NO compare")
    # plt.plot(omegas.NO_X, omegas.NO_Y)
    # plt.plot(omegas.NO_X, newY)
    # plt.show()
    #
    # m, b = Logic.LR(omegas.NO2_X, omegas.NO2_Y)
    # newY = line(np.array(omegas.NO2_X), m, b)
    # error_n1 = Norm.NormP(np.array(omegas.NO2_Y) - newY, 1)
    # error_n2 = Norm.NormP(np.array(omegas.NO2_Y) - newY, 2)
    # error_n3 = Norm.NormP(np.array(omegas.NO2_Y) - newY, "inf")
    # difference = abs(newY - omegas.NO2_Y)
    # plt.title("NO2 error")
    # plt.plot([i for i in range(len(omegas.NO2_X))], difference, color='red')
    # plt.show()
    # print("Norm 1: " + str(error_n1))
    # print("Norm 2: " + str(error_n2))
    # print("Norm inf: " + str(error_n3))
    # plt.title("NO2 compare")
    # plt.plot(omegas.NO2_X, omegas.NO2_Y)
    # plt.plot(omegas.NO2_X, newY)
    # plt.show()
    #
    # m, b = Logic.LR(omegas.O3_X, omegas.O3_Y)
    # newY = line(np.array(omegas.O3_X), m, b)
    # error_n1 = Norm.NormP(np.array(omegas.O3_Y) - newY, 1)
    # error_n2 = Norm.NormP(np.array(omegas.O3_Y) - newY, 2)
    # error_n3 = Norm.NormP(np.array(omegas.O3_Y) - newY, "inf")
    # difference = abs(newY - omegas.O3_Y)
    # plt.title("O3 error")
    # plt.plot([i for i in range(len(omegas.O3_X))], difference, color='red')
    # plt.show()
    # print("Norm 1: " + str(error_n1))
    # print("Norm 2: " + str(error_n2))
    # print("Norm inf: " + str(error_n3))
    # plt.title("O3 compare")
    # plt.plot(omegas.O3_X, omegas.O3_Y)
    # plt.plot(omegas.O3_X, newY)
    # plt.show()
    #
    # m, b = Logic.LR(omegas.O3NO2_X, omegas.O3NO2_Y)
    # newY = line(np.array(omegas.O3NO2_X), m, b)
    # error_n1 = Norm.NormP(np.array(omegas.O3NO2_Y) - newY, 1)
    # error_n2 = Norm.NormP(np.array(omegas.O3NO2_Y) - newY, 2)
    # error_n3 = Norm.NormP(np.array(omegas.O3NO2_Y) - newY, "inf")
    # difference = abs(newY - omegas.O3NO2_Y)
    # plt.title("O3NO2 error")
    # plt.plot([i for i in range(len(omegas.O3NO2_X))], difference, color='red')
    # plt.show()
    # print("Norm 1: " + str(error_n1))
    # print("Norm 2: " + str(error_n2))
    # print("Norm inf: " + str(error_n3))
    # plt.title("O3NO2 compare")
    # plt.plot(omegas.O3NO2_X, omegas.O3NO2_Y)
    # plt.plot(omegas.O3NO2_X, newY)
    # plt.show()


    #===
    # plt.title("CO omegas")
    # plt.plot(omegas.CO_X, omegas.CO_Y)
    # plt.scatter(omegas.CO_X, omegas.CO_Y)
    # plt.show()
    #
    # plt.title("NO omegas")
    # plt.plot(omegas.NO_X, omegas.NO_Y)
    # plt.scatter(omegas.NO_X, omegas.NO_Y)
    # plt.show()
    #
    # plt.title("NO2 omegas")
    # plt.plot(omegas.NO2_X, omegas.NO2_Y)
    # plt.scatter(omegas.NO2_X, omegas.NO2_Y)
    # plt.show()
    #
    # plt.title("O3 omegas")
    # plt.plot(omegas.O3_X, omegas.O3_Y)
    # plt.scatter(omegas.O3_X, omegas.O3_Y)
    # plt.show()
    #
    # plt.title("O3NO2 omegas")
    # plt.plot(omegas.O3NO2_X, omegas.O3NO2_Y)
    # plt.scatter(omegas.O3NO2_X, omegas.O3NO2_Y)
    # plt.show()

    # # #
    # p = 1
    # clusters, dictionary, indexes = KMean.Clustering(omegas.CO_X, omegas.CO_Y, 14, 2, omegas.CO_S)
    # clusters = KMean.UniqueClustering(omegas.O3NO2_X, omegas.O3NO2_Y, 14, 2, omegas.O3NO2_S)
    # UniqueClusters = KMean.ClusterIntersections(clusters, 2, 2)
    # lastStep = KMean.ShrinkClusters(UniqueClusters, 2, 2)
    # result = KMean.Clean(clusters)
    # for key in result.keys():
    #     x = [i[0] for i in result[key]]
    #     y = [i[1] for i in result[key]]
    #     distances = [Logic.distance(i[0] - key[0], i[1] - key[1]) for i in result[key]]
    #     radius = max(distances, default=0)
    #     color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    #     plt.scatter(x, y, color=color)
    #     plt.scatter([key[0]], [key[1]], marker="+", color=color)
    #     circle = plt.Circle((key[0], key[1]), radius, color=color, fill=False)
    #     plt.gca().add_patch(circle)
    #     print("Centroid: " + str((key[0], key[1])) + "| Number of clusters: " + str(
    #         len(result[key])) + "| Radius: " + str(radius))
    # plt.title("O3NO2 norm 2")
    # plt.autoscale()
    # plt.show()
    #
    # clusters = KMean.UniqueClustering(omegas.NO_X, omegas.NO_Y, 14, 2, omegas.NO_S)
    # UniqueClusters = KMean.ClusterIntersections(clusters, 2, 2)
    # lastStep = KMean.ShrinkClusters(UniqueClusters, 2, 2)
    # result = KMean.Clean(lastStep)
    # for key in result.keys():
    #     x = [i[0] for i in result[key]]
    #     y = [i[1] for i in result[key]]
    #     distances = [Logic.distance(i[0] - key[0], i[1] - key[1]) for i in result[key]]
    #     radius = max(distances, default=0)
    #     color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    #     plt.scatter(x, y, color=color)
    #     plt.scatter([key[0]], [key[1]], marker="+", color=color)
    #     circle = plt.Circle((key[0], key[1]), radius, color=color, fill=False)
    #     plt.gca().add_patch(circle)
    #     print("Centroid: " + str((key[0], key[1])) + "| Number of clusters: " + str(
    #         len(result[key])) + "| Radius: " + str(radius))
    # plt.title("NO norm 2")
    # plt.autoscale()
    # plt.show()
    #
    # clusters = KMean.UniqueClustering(omegas.NO2_X, omegas.NO2_Y, 14, 2, omegas.NO2_S)
    # UniqueClusters = KMean.ClusterIntersections(clusters, 2, 2)
    # lastStep = KMean.ShrinkClusters(UniqueClusters, 2, 2)
    # result = KMean.Clean(lastStep)
    # for key in result.keys():
    #     x = [i[0] for i in result[key]]
    #     y = [i[1] for i in result[key]]
    #     distances = [Logic.distance(i[0] - key[0], i[1] - key[1]) for i in result[key]]
    #     radius = max(distances, default=0)
    #     color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    #     plt.scatter(x, y, color=color)
    #     plt.scatter([key[0]], [key[1]], marker="+", color=color)
    #     circle = plt.Circle((key[0], key[1]), radius, color=color, fill=False)
    #     plt.gca().add_patch(circle)
    #     print("Centroid: " + str((key[0], key[1])) + "| Number of clusters: " + str(
    #         len(result[key])) + "| Radius: " + str(radius))
    # plt.title("NO2 norm 2")
    # plt.autoscale()
    # plt.show()
    #
    # clusters = KMean.UniqueClustering(omegas.O3_X, omegas.O3_Y, 14, 2, omegas.O3_S)
    # UniqueClusters = KMean.ClusterIntersections(clusters, 2, 2)
    # lastStep = KMean.ShrinkClusters(UniqueClusters, 2, 2)
    # result = KMean.Clean(lastStep)
    # for key in result.keys():
    #     x = [i[0] for i in result[key]]
    #     y = [i[1] for i in result[key]]
    #     distances = [Logic.distance(i[0] - key[0], i[1] - key[1]) for i in result[key]]
    #     radius = max(distances, default=0)
    #     color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    #     plt.scatter(x, y, color=color)
    #     plt.scatter([key[0]], [key[1]], marker="+", color=color)
    #     circle = plt.Circle((key[0], key[1]), radius, color=color, fill=False)
    #     plt.gca().add_patch(circle)
    #     print("Centroid: " + str((key[0], key[1])) + "| Number of clusters: " + str(
    #         len(result[key])) + "| Radius: " + str(radius))
    # plt.title("O3 norm 2")
    # plt.autoscale()
    # plt.show()
    #
    # clusters = KMean.UniqueClustering(omegas.O3NO2_X, omegas.O3NO2_Y, 14, 2, omegas.O3NO2_S)
    # UniqueClusters = KMean.ClusterIntersections(clusters, 2, 2)
    # lastStep = KMean.ShrinkClusters(UniqueClusters, 2, 2)
    # result = KMean.Clean(lastStep)
    # for key in result.keys():
    #     x = [i[0] for i in result[key]]
    #     y = [i[1] for i in result[key]]
    #     distances = [Logic.distance(i[0] - key[0], i[1] - key[1]) for i in result[key]]
    #     radius = max(distances, default=0)
    #     color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    #     plt.scatter(x, y, color=color)
    #     plt.scatter([key[0]], [key[1]], marker="+", color=color)
    #     circle = plt.Circle((key[0], key[1]), radius, color=color, fill=False)
    #     plt.gca().add_patch(circle)
    #     print("Centroid: " + str((key[0], key[1])) + "| Number of clusters: " + str(
    #         len(result[key])) + "| Radius: " + str(radius))
    # plt.title("O3NO2 norm 2")
    # plt.autoscale()
    # plt.show()
#==================================================
    # for key in dictionary.keys():

    # for key, centroid in enumerate(clusters):
    #     k = omegas.CO_S[indexes[key]]
    #     S = np.array([k[0], k[1], k[2], k[3]])
    #     Sm = np.array([0, 0, 0, 0])
    #     for cluster in dictionary[key]:
    #         km = cluster[2]
    #         Sm = np.add(Sm, np.array([km[0], km[1], km[2], km[3]]))
    #
    #     if len(dictionary[key]) != 0:
    #         Sm = Sm / len(dictionary[key])
    #         point = (0, 0)
    #         radius = 0
    #         for cluster in dictionary[key]:
    #             pk = cluster[2]
    #             vector = np.array([pk[0], pk[1], pk[2], pk[3]]) - Sm
    #             distance = Norm.NormP(vector, p)
    #             if distance > radius:
    #                 radius = distance
    #                 point = (cluster[0], cluster[1])
    #
    #         color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    #         plt.scatter([centroid[0], point[0]], [centroid[1], point[1]], marker='+', color=color)
    #         plt.scatter([point[0]], [point[1]], color=color)
    #
    #         distances = [Logic.distance(i[0] - centroid[0], i[1] - centroid[1]) for i in dictionary[key]]
    #         m = max(distances, default=0)
    #         circle = plt.Circle((centroid[0], centroid[1]), m, color=color, fill=False)
    #         plt.gca().add_patch(circle)
    #         print("Centroid: " + str(centroid) + "| Number of Clusters: " + str(len(dictionary[key])) + "| radius: " + str(m) + "| Radius of S: " + str(radius))
    # plt.title("CO norm: " + str(p))
    # plt.autoscale()
    # plt.show()
    #
    # clusters, dictionary, indexes = KMean.Clustering(omegas.NO_X, omegas.NO_Y, 14, 2, omegas.NO_S)
    # for key, centroid in enumerate(clusters):
    #     k = omegas.NO_S[indexes[key]]
    #     S = np.array([k[0], k[1], k[2], k[3]])
    #     Sm = np.array([0, 0, 0, 0])
    #     for cluster in dictionary[key]:
    #         km = cluster[2]
    #         Sm = np.add(Sm, np.array([km[0], km[1], km[2], km[3]]))
    #
    #     if len(dictionary[key]) != 0:
    #         Sm = Sm / len(dictionary[key])
    #         point = (0, 0)
    #         radius = 0
    #         for cluster in dictionary[key]:
    #             pk = cluster[2]
    #             vector = np.array([pk[0], pk[1], pk[2], pk[3]]) - Sm
    #             distance = Norm.NormP(vector, p)
    #             if distance > radius:
    #                 radius = distance
    #                 point = (cluster[0], cluster[1])
    #
    #         color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    #         plt.scatter([centroid[0], point[0]], [centroid[1], point[1]], marker='+', color=color)
    #         plt.scatter([point[0]], [point[1]], color=color)
    #
    #         distances = [Logic.distance(i[0] - centroid[0], i[1] - centroid[1]) for i in dictionary[key]]
    #         m = max(distances, default=0)
    #         circle = plt.Circle((centroid[0], centroid[1]), m, color=color, fill=False)
    #         plt.gca().add_patch(circle)
    #         print("Centroid: " + str(centroid) + "| Number of Clusters: " + str(len(dictionary[key])) + "| radius: " + str(m) + "| Radius of S: " + str(radius))
    # plt.title("NO norm: " + str(p))
    # plt.autoscale()
    # plt.show()
    #
    # clusters, dictionary, indexes = KMean.Clustering(omegas.NO2_X, omegas.NO2_Y, 14, 2, omegas.NO2_S)
    # for key, centroid in enumerate(clusters):
    #     k = omegas.NO2_S[indexes[key]]
    #     S = np.array([k[0], k[1], k[2], k[3]])
    #     Sm = np.array([0, 0, 0, 0])
    #     for cluster in dictionary[key]:
    #         km = cluster[2]
    #         Sm = np.add(Sm, np.array([km[0], km[1], km[2], km[3]]))
    #
    #     if len(dictionary[key]) != 0:
    #         Sm = Sm / len(dictionary[key])
    #         point = (0, 0)
    #         radius = 0
    #         for cluster in dictionary[key]:
    #             pk = cluster[2]
    #             vector = np.array([pk[0], pk[1], pk[2], pk[3]]) - Sm
    #             distance = Norm.NormP(vector, p)
    #             if distance > radius:
    #                 radius = distance
    #                 point = (cluster[0], cluster[1])
    #
    #         color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    #         plt.scatter([centroid[0], point[0]], [centroid[1], point[1]], marker='+', color=color)
    #         plt.scatter([point[0]], [point[1]], color=color)
    #
    #         distances = [Logic.distance(i[0] - centroid[0], i[1] - centroid[1]) for i in dictionary[key]]
    #         m = max(distances, default=0)
    #         circle = plt.Circle((centroid[0], centroid[1]), m, color=color, fill=False)
    #         plt.gca().add_patch(circle)
    #         print("Centroid: " + str(centroid) + "| Number of Clusters: " + str(len(dictionary[key])) + "| radius: " + str(m) + "| Radius of S: " + str(radius))
    # plt.title("NO2 norm: " + str(p))
    # plt.autoscale()
    # plt.show()
    #
    # clusters, dictionary, indexes = KMean.Clustering(omegas.O3_X, omegas.O3_Y, 14, 2, omegas.O3_S)
    # for key, centroid in enumerate(clusters):
    #     k = omegas.O3_S[indexes[key]]
    #     S = np.array([k[0], k[1], k[2], k[3]])
    #     Sm = np.array([0, 0, 0, 0])
    #     for cluster in dictionary[key]:
    #         km = cluster[2]
    #         Sm = np.add(Sm, np.array([km[0], km[1], km[2], km[3]]))
    #
    #     if len(dictionary[key]) != 0:
    #         Sm = Sm / len(dictionary[key])
    #         point = (0, 0)
    #         radius = 0
    #         for cluster in dictionary[key]:
    #             pk = cluster[2]
    #             vector = np.array([pk[0], pk[1], pk[2], pk[3]]) - Sm
    #             distance = Norm.NormP(vector, p)
    #             if distance > radius:
    #                 radius = distance
    #                 point = (cluster[0], cluster[1])
    #
    #         color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    #         plt.scatter([centroid[0], point[0]], [centroid[1], point[1]], marker='+', color=color)
    #         plt.scatter([point[0]], [point[1]], color=color)
    #
    #         distances = [Logic.distance(i[0] - centroid[0], i[1] - centroid[1]) for i in dictionary[key]]
    #         m = max(distances, default=0)
    #         circle = plt.Circle((centroid[0], centroid[1]), m, color=color, fill=False)
    #         plt.gca().add_patch(circle)
    #         print("Centroid: " + str(centroid) + "| Number of Clusters: " + str(len(dictionary[key])) + "| radius w: " + str(m) + "| Radius of S: " + str(radius))
    # plt.title("O3 norm: " + str(p))
    # plt.autoscale()
    # plt.show()
    #
    # clusters, dictionary, indexes = KMean.Clustering(omegas.O3NO2_X, omegas.O3NO2_Y, 14, 2, omegas.O3NO2_S)
    # for key, centroid in enumerate(clusters):
    #     k = omegas.O3NO2_S[indexes[key]]
    #     S = np.array([k[0], k[1], k[2], k[3]])
    #     Sm = np.array([0, 0, 0, 0])
    #     for cluster in dictionary[key]:
    #         km = cluster[2]
    #         Sm = np.add(Sm, np.array([km[0], km[1], km[2], km[3]]))
    #
    #     if len(dictionary[key]) != 0:
    #         Sm = Sm / len(dictionary[key])
    #         point = (0, 0)
    #         radius = 0
    #         for cluster in dictionary[key]:
    #             pk = cluster[2]
    #             vector = np.array([pk[0], pk[1], pk[2], pk[3]]) - Sm
    #             distance = Norm.NormP(vector, p)
    #             if distance > radius:
    #                 radius = distance
    #                 point = (cluster[0], cluster[1])
    #
    #         color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    #         plt.scatter([centroid[0], point[0]], [centroid[1], point[1]], marker='+', color=color)
    #         plt.scatter([point[0]], [point[1]], color=color)
    #
    #         distances = [Logic.distance(i[0] - centroid[0], i[1] - centroid[1]) for i in dictionary[key]]
    #         m = max(distances, default=0)
    #         circle = plt.Circle((centroid[0], centroid[1]), m, color=color, fill=False)
    #         plt.gca().add_patch(circle)
    #         print("Centroid: " + str(centroid) + "| Number of Clusters: " + str(len(dictionary[key])) + "| radius w: " + str(m) + "| Radius of S: " + str(radius))
    # plt.title("O3NO2 norm: " + str(p))
    # plt.autoscale()
    # plt.show()

    # for key, centroid in enumerate(clusters):
    #     S = omegas.CO_S[indexes[key]]
    #     print("Centroid: " + str(centroid) + "| " + "S: " + str(S))
    #     norm = 0
    #     point = (0, 0)
    #     s = (0, 0)
    #     for t in dictionary[key]:
    #         x = t[2][0] - S[0]
    #         y = t[2][1] - S[1]
    #         d = Norm.NormP([x, y], p)
    #         if d >= norm:
    #             point = (t[0], t[1])
    #             norm = d
    #             s = (t[2][0], t[2][1])
    #     print("Cluster: " + str(point) + "| " + "S: " + str(s))
    #     print("Distance: " + str(norm))
    #     print()
    #     plt.plot([centroid[0], point[0]],[centroid[1], point[1]])
    #     plt.scatter([centroid[0], point[0]], [centroid[1], point[1]])
    # plt.show()
    #
    # clusters, dictionary, indexes = KMean.Clustering(omegas.NO_X, omegas.NO_Y, 14, 2, omegas.NO_S)
    # for key, centroid in enumerate(clusters):
    #     S = omegas.NO_S[indexes[key]]
    #     print("Centroid S: " + str(S))
    #     norm = 0
    #     point = (0, 0)
    #     s = (0, 0)
    #     for t in dictionary[key]:
    #         x = t[2][0] - S[0]
    #         y = t[2][1] - S[1]
    #         d = Norm.NormP([x, y], p)
    #         if d >= norm:
    #             point = (t[0], t[1])
    #             norm = d
    #             s = (t[2][0], t[2][1])
    #     print("Cluster: " + str(point) + "| " + "S: " + str(s))
    #     print("Distance: " + str(norm))
    #     print()
    #     plt.plot([centroid[0], point[0]],[centroid[1], point[1]])
    #     plt.scatter([centroid[0], point[0]], [centroid[1], point[1]])
    # plt.show()
    #
    # clusters, dictionary, indexes = KMean.Clustering(omegas.NO2_X, omegas.NO2_Y, 14, 2, omegas.NO2_S)
    # for key, centroid in enumerate(clusters):
    #     S = omegas.NO2_S[indexes[key]]
    #     print("Centroid S: " + str(S))
    #     norm = 0
    #     point = (0, 0)
    #     s = (0, 0)
    #     for t in dictionary[key]:
    #         x = t[2][0] - S[0]
    #         y = t[2][1] - S[1]
    #         d = Norm.NormP([x, y], p)
    #         if d >= norm:
    #             point = (t[0], t[1])
    #             norm = d
    #             s = (t[2][0], t[2][1])
    #     print("Cluster: " + str(point) + "| " + "S: " + str(s))
    #     print("Distance: " + str(norm))
    #     print()
    #     plt.plot([centroid[0], point[0]],[centroid[1], point[1]])
    #     plt.scatter([centroid[0], point[0]], [centroid[1], point[1]])
    # plt.show()
    #
    # clusters, dictionary, indexes = KMean.Clustering(omegas.O3_X, omegas.O3_Y, 14, 2, omegas.O3_S)
    # for key, centroid in enumerate(clusters):
    #     S = omegas.O3_S[indexes[key]]
    #     print("Centroid S: " + str(S))
    #     norm = 0
    #     point = (0, 0)
    #     s = (0, 0)
    #     for t in dictionary[key]:
    #         x = t[2][0] - S[0]
    #         y = t[2][1] - S[1]
    #         d = Norm.NormP([x, y], p)
    #         if d >= norm:
    #             point = (t[0], t[1])
    #             norm = d
    #             s = (t[2][0], t[2][1])
    #     print("Cluster: " + str(point) + "| " + "S: " + str(s))
    #     print("Distance: " + str(norm))
    #     print()
    #     plt.plot([centroid[0], point[0]],[centroid[1], point[1]])
    #     plt.scatter([centroid[0], point[0]], [centroid[1], point[1]])
    # plt.show()
    #
    # clusters, dictionary, indexes = KMean.Clustering(omegas.O3NO2_X, omegas.O3NO2_Y, 14, 2, omegas.O3NO2_S)
    # for key, centroid in enumerate(clusters):
    #     S = omegas.O3NO2_S[indexes[key]]
    #     print("Centroid S: " + str(S))
    #     norm = 0
    #     point = (0, 0)
    #     s = (0, 0)
    #     for t in dictionary[key]:
    #         x = t[2][0] - S[0]
    #         y = t[2][1] - S[1]
    #         d = Norm.NormP([x, y], p)
    #         if d >= norm:
    #             point = (t[0], t[1])
    #             norm = d
    #             s = (t[2][0], t[2][1])
    #     print("Cluster: " + str(point) + "| " + "S: " + str(s))
    #     print("Distance: " + str(norm))
    #     print()
    #     plt.plot([centroid[0], point[0]],[centroid[1], point[1]])
    #     plt.scatter([centroid[0], point[0]], [centroid[1], point[1]])
    # plt.show()

    # # Plot.PlotClusters(dictionary, clusters, "CO Clusters")
    # Plot.PlotCentroidsWithCircles(dictionary, clusters, "CO Centroids")
    #
    # clusters, dictionary = KMean.Clustering(omegas.NO_X, omegas.NO_Y, 14, 2)
    # # Plot.PlotClusters(dictionary, clusters, "NO Clusters")
    # Plot.PlotCentroidsWithCircles(dictionary, clusters, "NO Centroids")
    #
    # clusters, dictionary = KMean.Clustering(omegas.NO2_X, omegas.NO2_Y, 14, 2)
    # # Plot.PlotClusters(dictionary, clusters, "NO2 Clusters")
    # Plot.PlotCentroidsWithCircles(dictionary, clusters, "NO2 Centroids")
    #
    # clusters, dictionary = KMean.Clustering(omegas.O3_X, omegas.O3_Y, 14, 2)
    # # Plot.PlotClusters(dictionary, clusters, "O3 Clusters")
    # Plot.PlotCentroidsWithCircles(dictionary, clusters, "O3 Centroids")
    #
    # clusters, dictionary = KMean.Clustering(omegas.O3NO2_X, omegas.O3NO2_Y, 14, 2)
    # # Plot.PlotClusters(dictionary, clusters, "O3NO2 Clusters")
    # Plot.PlotCentroidsWithCircles(dictionary, clusters, "O3NO2 Centroids")

"""
1) w ეების კლასტერიზაცია სადაც რადიუსი არადამაკმაყოფილებელია მარტო მაგათ განვიხილავ  და მაგათ კიდევ ვაკლასტერებ
სანამ რადიუსს კარგს არ მივიღებ  მიახლოება გავაკეთო 10^-6

და ნახაზები მოვაწესრიგო ლეგენდა გავუკეთო და რადიუსები მანდ ჩავწერო 
S - ები დავხაზო გასაშუალებული 
"""

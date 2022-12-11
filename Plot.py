import matplotlib.pyplot as plt
import random
import Logic


def Visualize(vector, title):
    plt.title(title)
    plt.plot([i for i in range(len(vector))], vector, color='red')
    return plt.show()


def Plots(x, y, title):
    plt.title(title)
    plt.plot(x, y)
    return plt.show()


def Scatter(x, y, title):
    plt.title(title)
    plt.scatter(x, y)
    return plt.show()


def PlotWithDots(x, y, title):
    plt.title(title)
    plt.scatter(x, y, color='red')
    plt.plot(x, y)

    plt.xlim([min(x) - 10, max(x) + 10])
    plt.ylim([min(y) - 10, max(y) + 10])
    return plt.show()


def PlotClusters(dictionary, clusters, title):
    plt.title(title)
    for key in dictionary.keys():
        color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
        x = [i[0] for i in dictionary[key]]
        y = [i[1] for i in dictionary[key]]
        plt.title("O3NO2 clusters")
        plt.scatter(x, y, color=color)
        plt.scatter([clusters[key][0]], [clusters[key][1]], marker="X", color=color)
    plt.autoscale()
    return plt.show()


def PlotCentroidsWithCircles(dictionary, centroids, title):
    plt.title(title)

    for key, centroid in enumerate(centroids):
        points = dictionary[key]
        distances = [Logic.distance(i[0] - centroid[0], i[1] - centroid[1]) for i in points]
        radius = max(distances, default=0)
        color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
        plt.scatter([centroid[0]], [centroid[1]], color=color)
        circle = plt.Circle((centroid[0], centroid[1]), radius, color=color, fill=False)
        plt.gca().add_patch(circle)
        print("Centroid Coordinates: " + str(centroid) + " Number of Clusters: " + str(len(dictionary[key])) +
              " Radius: " + str(radius))
    plt.autoscale()
    return plt.show()

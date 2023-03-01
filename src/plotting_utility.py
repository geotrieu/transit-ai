import matplotlib.pyplot as plt
import seaborn as sns

def plotGridPoints2D(gridPoints, color=None):
    fig = plt.figure()
    ax = fig.add_subplot()
    fig.set_figheight(10)
    fig.set_figwidth(10)
    ax.scatter(gridPoints["lat"], gridPoints["long"], c=color)
    return ax

def plotGridPoints3D(gridPoints, color=None):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    fig.set_figheight(10)
    fig.set_figwidth(10)
    ax.scatter(gridPoints["lat"], gridPoints["long"], gridPoints["score"], c=color)
    return ax

def plotGridPoints3DWithLine(gridPoints, line):
    ax = plotGridPoints3D(gridPoints)
    ax.plot([line[0], line[1]], [line[2], line[3]], [0, 0], color='red', linewidth=3)
    return ax

def plotGridPoints3DWithPoints(gridPoints, points):
    ax = plotGridPoints3D(gridPoints)
    x = points[0]
    y = points[1]
    ax.scatter(x, y, 0)
    return ax

def plotHeatmap(gridPoints, line, density):
    y_begin = line[2]
    y_end = line[3]
    fig = plt.figure()
    ax = sns.heatmap(gridPoints.pivot("long", "lat", "score"))
    y_begin_hm = int((y_begin - gridPoints["long"].iloc[0]) / (gridPoints["long"].iloc[-1] - gridPoints["long"].iloc[0]) * density)
    y_end_hm = int((y_end - gridPoints["long"].iloc[0]) / (gridPoints["long"].iloc[-1] - gridPoints["long"].iloc[0]) * density)
    ax.plot([0, density], [y_begin_hm, y_end_hm], linewidth=3, color='r')
    return ax

def plotHeatmapPolynomial(gridPoints, curves, density):
    fig = plt.figure()
    ax = sns.heatmap(gridPoints.pivot("long", "lat", "score"))
    for curve in curves:
        x = curve[0]
        y = curve[1]
        x_hm = [int(a) for a in ((x - gridPoints["lat"].iloc[0]) / (gridPoints["lat"].iloc[-1] - gridPoints["lat"].iloc[0]) * density)]
        y_hm = [int(a) for a in ((y - gridPoints["long"].iloc[0]) / (gridPoints["long"].iloc[-1] - gridPoints["long"].iloc[0]) * density)]
        ax.scatter(x_hm, y_hm, linewidth=1)
    return ax
import random
import plotly
import plotly.graph_objs as go
import numpy as np

P = 3 * 10**(-9)
Pmin = P - (P * 0.15)
Pmax = P + (P * 0.15)
E = 109
L = 3.5 * 10**(-3)
w = 1.6 * 10**(-3)
t = 0.4 * 10**(-3)
I = w * t**3 / 12

Nexp = 1000
i = 0
xList = []
yList = []
while i < Nexp:
    Prand = random.uniform(Pmin, Pmax)
    dL = -(Prand*(L**3))/(3*E*I)
    xList.append(i)
    yList.append(dL * 10**3)
    i += 1

graphData = [go.Scatter(
    x = xList,
    y = yList,
    mode = 'markers'
)]
plotly.offline.plot(graphData, filename='graph.html')

N = 1 + 3.222 * np.log10(Nexp)
N = int(round(N))

histogramData = [go.Histogram(
    x = yList,
    nbinsx = N
)]
plotly.offline.plot(histogramData, filename='histogram.html')
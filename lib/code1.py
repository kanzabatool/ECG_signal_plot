import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')


def load_data():
    ecg = "../data/data-eeg.csv"
    myfile = pd.read_csv(ecg, header=None).values
    data = myfile.tolist()
    return data


def plot_signal(data):
    yaxis = []
    xaxis = data

    for k in range(1, 192001, 1):
        y = k / 320
        yaxis.append(y)

    # Normalise the data
    df = pd.DataFrame(xaxis)
    normalized_df = (df - df.mean()) / df.std()
    df = normalized_df
    xaxis = df.values.tolist()

    # Plot the signal
    plt.plot(yaxis, xaxis)
    plt.xlabel("time/s")
    plt.show()

    return xaxis, yaxis


def slider(yaxis, xaxis):
    # Setting Plot and Axis variables as subplots()
    # function returns tuple(fig, ax)
    Plot, Axis = plt.subplots()

    # Adjust the bottom size according to the
    # requirement of the user
    plt.subplots_adjust(bottom=0.25)

    # plot the x and y using plot function
    l = plt.plot(yaxis, xaxis)

    # Choose the Slider color
    slider_color = 'White'

    # Set the axis and slider position in the plot
    axis_position = plt.axes([0.2, 0.1, 0.65, 0.03],
                             facecolor=slider_color)
    slider_position = Slider(axis_position,
                             'Pos', 0.1, 90.0)

    def update(val):
        pos = slider_position.val
        Axis.axis([pos, pos + 10, -1, 1])
        Plot.canvas.draw_idle()

    # update function called using on_changed() function
    slider_position.on_changed(update)

    # Display the plot
    plt.xlabel("time/s")
    plt.show()


def clean_signal(yaxis, xaxis):

    df = pd.DataFrame(xaxis)
    normalized_df = (df - df.mean()) / df.std()
    df = normalized_df
    df[(df < -1) | (df > 1)] = 0
    xaxis = df.values.tolist()

    plt.ylim(-10, 30)
    plt.plot(yaxis, xaxis)
    plt.xlabel("time/s")
    plt.show()


data = load_data()
xaxis, yaxis = plot_signal(data)
slider(yaxis, xaxis)
clean_signal(yaxis, xaxis)



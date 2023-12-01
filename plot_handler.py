# plot_handler.py
import pandas as pd
import matplotlib.pyplot as plt

def plot_line_chart(df, x_label, y_label):
    plt.figure()
    plt.plot(df[x_label], df[y_label])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title('Line Plot')
    plt.show()

def plot_bar_chart(df, x_label, y_label):
    plt.figure()
    plt.bar(df[x_label], df[y_label])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title('Bar Plot')
    plt.show()

def plot_scatter_chart(df, x_label, y_label):
    plt.figure()
    plt.scatter(df[x_label], df[y_label])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title('Scatter Plot')
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt
# import libraries
import seaborn as sns
import numpy as np

#path where the reading are stored
PATH = "EvalReadings.xlsx"
bft_modes = ["Byz-0B", "Byz-100B", "Byz-1KB", "Byz-4KB"]
bft_cft_modes = ["Byz-0B", "Byz-100B", "Byz-1KB", "Byz-4KB","Cft-0B", "Cft-100B", "Cft-1KB", "Cft-4KB" ]
cft_modes = ["Cft-0B", "Cft-100B", "Cft-1KB", "Cft-4KB"]
clients = ["10 clients", "20 clients","30 clients"]

#def to make use to plot the results from Experiment 1,2,3
def throughputLatencyPlot():

    for i in [2,9,10]:
        df1 = pd.read_excel(PATH , sheet_name=i)
        x = df1['Operations']
        y = df1['Throughput']
        # uncomment if Latency numbers need to be plotted
        # y = df1['Latency']
        if i==2:
            plt.plot(x, y, label= clients[0])
        elif i==9:
            plt.plot(x, y, label= clients[1])
        else:
            plt.plot(x, y, label=clients[2])
    plt.xlabel('# Operations (Kops)')
    plt.ylabel('Throughput (ops per sec)')
    #uncomment if Latency numbers need to be plotted
    # plt.ylabel('Latency (milli sec)')
    plt.title(' ')
    plt.grid()
    plt.legend()
    plt.show()  # To display the plot

def faultScalabilityPlot():
    import matplotlib.pyplot as plt

    df = pd.read_excel(PATH, sheet_name=8)
    print(df)
    f = df["f"][0:3]
    throughput0 = {
        'bft': df["Throughput BFT"][:3],
        'cft' : df['Throughput CFT'][:3]
    }
    x = np.arange(len(f))
    width = 0.25
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')
    for attribute, measurement in throughput0.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Throughput (ops per sec)')
    ax.set_xlabel('Number of faults')
    ax.set_title('')
    ax.set_xticks(x + width, f)
    ax.legend(loc='upper right', ncols=3)

    # ax.set_ylim(0, 250)

    plt.show()
    # print(f)

throughputLatencyPlot()
faultScalabilityPlot()

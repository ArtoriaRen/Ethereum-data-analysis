import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def main():
        # Data to plot
        stats = pd.read_csv('data/ether_2018_july.csv')
        labels = [x.decode('string_escape') for x in stats['pool_name']]
        print(labels[0])
        sizes = stats['count']
        # colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'tomato', 'grey', 'hotpink', \
        #     'royalblue', 'violet', 'limegreen', 'peru', 'cyan']

        colors = ['royalblue', 'orange', 'green', 'red', 'lightskyblue', 'brown', 'green', \
                  'grey', 'orange', 'cyan', 'violet', 'red']
        # Plot
        plt.pie(sizes, labels=labels,
                autopct='%1.1f%%', shadow=False, startangle=0, colors=colors)

        plt.axis('equal')
        plt.savefig('../figures/eth_pie_chart.eps')
        plt.close()

if __name__ == '__main__':
        main()
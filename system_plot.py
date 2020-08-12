import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def build_df(filename="nsp_data_clean.csv"):
    return pd.read_csv(filename)

def show_plot(system_df):
    sns.set_style("whitegrid", {'axes.grid': False})
    fig = plt.figure(figsize=(7,7))
    ax = Axes3D(fig)
    ax.scatter(system_df['X'], system_df['Y'], system_df['Z'], marker='o')
    plt.show()


def main():
    system_df = build_df()
    show_plot(system_df)
    
if __name__ == "__main__":
    main()

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url="https://raw.githubusercontent.com/sci2pro/code-fastfoundations/refs/heads/main/day3/FAOSTAT_data_7-23-2022.csv"
df=pd.read_csv(url)
print(df.head())
df_small=df[["Year","Area","Item","Element","Value"]]
print(df_small.head())
df_pivot=df_small.pivot_table(
    index=["Year","Area","Item"],
    columns="Element",
    values="Value",
    aggfunc="first"
     ).reset_index()
df_pivot = df_pivot.rename(columns={
    "Area harvested": "Area Harvested",
    "Yield": "Yield",
    "Production": "Production"
})
print(df_pivot.head(10))

cocoa = df_pivot[df_pivot["Item"] == "Cocoa, beans"]
cocoa = cocoa[cocoa["Area"].isin(["Ghana", "Côte d'Ivoire"])]

def plot_cocoa_scatter():
    plt.figure(figsize=(10,10))

    for country in["Ghana","Côte d'Ivoire"]:
        subset=cocoa[cocoa["Area"]==country]
        plt.scatter(subset["Area Harvested"], subset["Yield"], label=country)
        plt.title("Ghana and Ivory Coast cocoa production Comparison")
        plt.xlabel("Area harvested(Hectares)")
        plt.ylabel("Yield(Hg/Ha)")
        plt.legend()
        plt.grid(True)
        plt.show()

def plot_cocoa_bar():
    plt.figure(figsize=(12,6))
    for country in["Ghana","Côte d'Ivoire"]:
        subset=cocoa[cocoa["Area"]==country]
        plt.bar(
            subset["Year"],
            subset["Production"],
            alpnewha=0.6,
            label=f"{country}Production"
        )
        plt.plot(
            subset["Year"],
            subset["Production"],
            marker="o",
            linestyle="--",
            label=f"{country}Yield"
        )
    plt.title("Ghana and Ivory Coast cocoa production Comparison")
    plt.xlabel("Year")
    plt.ylabel("Production")
    plt.legend()
    plt.grid(True)
    plt.show()
def main():
    plot_cocoa_scatter()
    plot_cocoa_bar()
    return 0
if __name__ == '__main__':
    sys.exit(main())
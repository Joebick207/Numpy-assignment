import sys
import matplotlib.pyplot as plt
import numpy as np
def plot_lines():
    x=np.linspace(0,2*np.pi,200)
    print(f"{x=}")
    y=np.sin(x)
    fig, ax = plt.subplots()
    print(f"{type(fig)=};{type(ax)=}")
    ax.plot(x,y)
    plt.show()
def main():
    plot_lines()
    return 0
if __name__ == '__main__':
    sys.exit(main())
from matplotlib import pyplot as plt

def plot_prices(times,prices):
    
    fig, ax = plt.subplots()
    ax.set_title('Prices')
    ax.set_xlabel('times in days')
    ax.set_ylabel('prices in dollars')
    ax.plot(times,prices)

    return fig, ax
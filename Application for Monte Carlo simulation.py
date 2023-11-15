import yfinance as yf 
import numpy as np 
import matplotlib.pyplot as plt
import datetime
def montecarlo(stock="TSLA", reps=250):
    list_prices = []
    start = datetime.datetime.now() - datetime.timedelta(days=30) # not gonna use in this case
    df = yf.download("TSLA", interval="1d")
    returns = np.log(1 + df['Adj Close'].pct_change())
    mu, sigma = returns.mean(), returns.std()
    initial = df['Adj Close'].iloc[-1]
    for i in range(reps):
        sim_reps = np.random.normal(mu, sigma, 252) # for the next 252 days we're predicting
        sim_prices = initial * (sim_reps + 1).cumprod()
        plt.axhline(initial, c="k")
        plt.plot(sim_prices)
        list_prices.append(sim_prices[-1])
    return stock, np.array(list_prices).mean()
def main():
    stock, a = montecarlo()
    print(f"stock price for {stock} a year later:{a}")
if __name__ == "__main__":
    main()

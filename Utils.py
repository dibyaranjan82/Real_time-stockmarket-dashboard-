

def calculate_moving_average(data, window=10):
    return data['Close'].rolling(window=window).mean()



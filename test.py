import pandas as pd

def create_df():
    df = pd.DataFrame({ 'length': [1.5, 0.5, 1.2, 0.9, 3],
                        'width': [0.7, 0.2, 0.15, 0.2, 1.1]
                        }, index= ['pig', 'rabbit', 'duck', 'chicken', 'horse']
                      )
    return df

def plot_pandas_df(df):
    hist = df.hist(bins=3)
    return hist

## This is the function that transform
## the time series to X(t-1), X(t-2), X(t-3),... -> Y(t)

## I modified it from Jason Brownlee's blog here: 
## https://machinelearningmastery.com/convert-time-series-supervised-learning-problem-python/

import pandas as pd


def series_to_supervised(data, n_in=1, n_out=1, dropna=True):
    """
    Frame a time series as a supervised learning dataset.
    Arguments:
         data: Sequence of observations as a list or Numpy array or a pandas dataframe.
         n_in: Number of lag observations as input (X). it refers to the number in units of time
         n_out: Number of observations as output (y).
         dropnan: Bollean whether or not to drop rows with NaN values.
    Returns:
         Pandas DataFrame of series framed for supervised learning.
    """
    if data.shape[1]:
        n_vars = data.shape[1]
    else:
        n_vars = 1
        
    df = pd.DataFrame(data)
    
    cols, col_names = [], []
    ## build the input sequence (t-n, ..., t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        col_list = [(col + '(t-%d)'%(i)) for col in df.columns]
        col_names.extend(col_list)
        
    ## forecast sequence (t, t+1, ..., t+n)
    for i in range(0, n_out):
        cols.append(df.shift(i))
        if i == 0:
            col_list = [(col + '(t)') for col in df.columns]
            col_names.extend(col_list)
        else:
            col_list = [(col + '(t+%d)'%(i)) for col in df.columns]
            col_names.extend(col_list)
            
    ## put everything together
    agg = pd.concat(cols, axis = 1)
    agg.columns = col_names
    ## drop the Nan values
    if dropna:
        agg.dropna(inplace = True)
    return agg

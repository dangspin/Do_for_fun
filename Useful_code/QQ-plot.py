import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import *

def qqplot(x_array, qpoints = 100):

    ## Standarlize the dataset
    x_array_norm = (x_array - np.mean(x_array))/np.std(x_array)
    
    ## Here only consider 99 points. So that we will consider 1%, 2%,...,99%
    x_leng = len(x_array)
    quantiles = [(1.0 * i/100) for i in range(1, qpoints)]
    
    ## initialization the placeholders for the normal distribution and customized data
    normal = np.empty(qpoints - 1)
    result = np.empty(qpoints - 1)
    
    for k in range(0, qpoints - 1):
        q = quantiles[k]
        
        ## This is the way to calculate the qth quantile, both value and position.
        i = q *(x_leng + 1) - 1
        j = int(np.floor(i))        
        res = x_array_norm[j] + (x_array_norm[j + 1]-x_array_norm[j])*(i - j)
        
        result[k] = res
        normal[k] = norm.ppf(q)
        
    return result, normal
    
    
    if __name__ == "__main__":
        data_points = sorted(np.random.normal(0, 1, 100))
        result, normal = qqplot(data_points)
        
        plt.plot(np.linspace(-2,2,100), np.linspace(-2,2,100), '-')
        plt.plot(result, normal, '.')

        plt.show()

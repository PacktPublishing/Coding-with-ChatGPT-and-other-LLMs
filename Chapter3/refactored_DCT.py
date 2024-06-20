# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:50:12 2024

@author: Vince Hall  ABT NEWS LTD. and Claude 3 Sonnet.
"""
import numpy as np
from scipy.fft import dct, idct

def compute_dct(data):
    """
    Compute the Discrete Cosine Transform (DCT) of the input data.
    """
    return dct(data, norm='ortho')

def truncate_coefficients(coefficients, num_coefficients):
    """
    Truncate the DCT coefficients to keep only the specified number of coefficients.
    """
    return coefficients[:num_coefficients]

def compress_timeseries(data, num_coefficients):
    """
    Compress the time series data using DCT and return the truncated coefficients.
    """
    half_len = len(data) // 2
    dct1 = compute_dct(data[:half_len])
    dct2 = compute_dct(data[half_len:])
    # coefficients = np.concatenate((truncate_coefficients(dct1, num_coefficients),
    #                                truncate_coefficients(dct2, num_coefficients)))


    # change from Gemini 1 Pro    
    coefficients = [truncate_coefficients(dct1, num_coefficients),
                truncate_coefficients(dct2, num_coefficients)]


    return coefficients

# Example usage
data = [0.15, 9.347, -5.136, 8.764, 4.17, 12.056, 2.45, 9.03, 16.125]
compressed_data = compress_timeseries(data, 3)
print(compressed_data)

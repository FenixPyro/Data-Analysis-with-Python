"""Module defining the calculate function"""
import numpy as np

def calculate(lst):
    """Function that makes a dict with all the relevant data from a list"""
    if len(lst) == 9:
        array = np.array(
            [lst[:3],
            lst[3:6],
            lst[6:]
        ])
        mean_1 = np.mean(array, axis=0).tolist()
        mean_2 = np.mean(array, axis=1).tolist()
        mean_3 = np.mean(array)
        var_1 = np.var(array, axis=0).tolist()
        var_2 = np.var(array, axis=1).tolist()
        var_3 = np.var(array)
        std_1 = np.std(array, axis=0).tolist()
        std_2 = np.std(array, axis=1).tolist()
        std_3 = np.std(array)
        max_1 = np.max(array, axis=0).tolist()
        max_2 = np.max(array, axis=1).tolist()
        max_3 = np.max(array)
        min_1 = np.min(array, axis=0).tolist()
        min_2 = np.min(array, axis=1).tolist()
        min_3 = np.min(array)
        sum_1 = np.sum(array, axis=0).tolist()
        sum_2 = np.sum(array, axis=1).tolist()
        sum_3 = np.sum(array)
        all_mean = [mean_1, mean_2, mean_3]
        all_var = [var_1, var_2, var_3]
        all_std = [std_1, std_2, std_3]
        all_max = [max_1, max_2, max_3]
        all_min = [min_1, min_2, min_3]
        all_sum = [sum_1, sum_2, sum_3]
        calculations = {
            'mean' : all_mean,
            'variance' : all_var,
            'standard deviation' : all_std,
            'max' : all_max,
            'min' : all_min,
            'sum' : all_sum
        }
        return calculations
    else:
        raise ValueError("List must contain nine numbers.")

import numpy as np


def calculate(list):

    # Test lengh of the list
    try:
        numbers = np.array(list).reshape([3, 3])
    except ValueError:
        raise ValueError("List must contain nine numbers.")

    # Variables declaration
    mean = []
    var = []
    sd = []
    max = []
    min = []
    sum = []

    # Order Column, Row and Total
    # Axis 0 - Column
    mean.append(numbers.mean(axis=0).tolist())
    var.append(numbers.var(axis=0).tolist())
    sd.append(numbers.std(axis=0).tolist())
    max.append(numbers.max(axis=0).tolist())
    min.append(numbers.min(axis=0).tolist())
    sum.append(numbers.sum(axis=0).tolist())

    # Axis 1 - Row
    mean.append(numbers.mean(axis=1).tolist())
    var.append(numbers.var(axis=1).tolist())
    sd.append(numbers.std(axis=1).tolist())
    max.append(numbers.max(axis=1).tolist())
    min.append(numbers.min(axis=1).tolist())
    sum.append(numbers.sum(axis=1).tolist())

    # Total
    mean.append(numbers.mean().tolist())
    var.append(numbers.var().tolist())
    sd.append(numbers.std().tolist())
    max.append(numbers.max().tolist())
    min.append(numbers.min().tolist())
    sum.append(numbers.sum().tolist())

    # Mount the dict with de values obtained before
    calculations = {
        'mean': mean,
        'variance': var,
        'standard deviation': sd,
        'max': max,
        'min': min,
        'sum': sum
    }

    return calculations

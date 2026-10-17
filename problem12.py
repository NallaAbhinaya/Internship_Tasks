
def average(array):
    unique_heights = set(array)
    return sum(unique_heights) / len(unique_heights)

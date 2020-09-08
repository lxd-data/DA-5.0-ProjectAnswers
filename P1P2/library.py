# TASK 1: Write your code below this comment:
def calculate_mean(data):
    """
    calculate the mean from the provided data.

    Parameters
    ----------
    data: (list)
        a list of integers
    
    Returns
    ----------
    the mean of the data.
    """
    return sum(data)/len(data)

# TASK 2: Write your code below this comment:
def calculate_median(data):
    """
    calulate the median from the provided data.

    Parameters
    ----------
    data: (list)
        a list of integers

    Returns
    ----------
    the median of the data.
    """
    length = len(data)
    sorted_data = sorted(data)
    median = sorted_data[length//2]

    if length % 2 == 0: 
        median = (median + sorted_data[length//2 - 1])/2
    return median

# TASK 3: Write your code below this comment:
def calculate_stddev(data):
  """
  calculates the standard deviation from the provided data.

  Parameters
  ----------
  data: (list)
    a list of integers

  Returns
  ----------
  the standard deviation of the data.
  """
  mean = calculate_mean(data)
  squared_list = [(x-mean)**2 for x in data]
  squared_mean = calculate_mean(squared_list)
  return round(squared_mean**0.5, 2)

# TASK 4: Create a reporting function that returns the result of the given operation

def report(operation, data):
    """
    Return a report for whichever descriptive statistic a coworker requests.
    
    Parameters
    ----------
    operation: (str)
        the operation to run. Accepted operations are
        mean, median, std dev, or all.
    data: (list)
        a list of integers.

    Returns
    ----------
    a report including info on the specified operation.
    """
    dispatch_table = {
            "mean": calculate_mean(data), 
            "median": calculate_median(data), 
            "std dev": calculate_stddev(data) 
            }
    if operation in dispatch_table:
        result = dispatch_table[operation]
        return f"The {operation} is {result}."
    else:
        return dispatch_table

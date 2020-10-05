import pandas as pd
import os
# EXAMPLE CSV SO THINGS RUN CORRECTLY
CSV_PATH = os.path.join(os.path.dirname(__file__).replace("Labs", ""), "my_file.csv")
df = pd.read_csv(CSV_PATH)

# My actual answers
df.head()
df.tail()
df.shape
df.info()
df.describe()
# .value_counts on a dataframe is throwing an error for me here but not in the jupyter notebook
# This makes me think we shouldn't encourage them to use .value_counts() on an entire df.
# df.value_counts()
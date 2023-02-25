# import pandas as pd
# import numpy as np
from main import summarize_dataframe, np, pd
#Example testing
df = pd.read_csv('test_dataset.csv', sep = ',', names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

if __name__ == '__main__':
    print(summarize_dataframe(df, input('Choose output type (markdown, html or xlsx):')))

import pandas as pd
import numpy as np
import tabulate

def summarize_dataframe(df, output_type):
    summary = pd.DataFrame(columns=[
        'column_name',
        'data_type',
        'min',
        'max',
        'mean',
        'median',
        'mode',
        'percent_zero', 'variance', 'standard_deviation', 'interquartile_range', 'coefficient_of_variation', 'num_distinct_values'])

    for col in df.columns:
        col_data = df[col]
        data_type = str(col_data.dtype)
        num_distinct_values = len(col_data.unique())

        if col_data.dtype == np.float64 or col_data.dtype == np.int64:
            summary.loc[len(summary)] = [col, data_type, col_data.min(), col_data.max(), col_data.mean(), col_data.median(), col_data.mode().values[0], (col_data == 0).sum()/len(col_data)*100, col_data.var(), col_data.std(), col_data.quantile(0.75) - col_data.quantile(0.25), col_data.std()/col_data.mean(), num_distinct_values]
        elif col_data.dtype == bool:
            summary.loc[len(summary)] = [col, data_type, None, None, None, None, col_data.mode().values[0], (col_data == 0).sum()/len(col_data)*100, None, None, None, None, num_distinct_values]
        elif col_data.dtype == 'datetime64[ns]':
            summary.loc[len(summary)] = [col, data_type, col_data.min(), col_data.max(), None, None, col_data.mode().values[0], (col_data == 0).sum()/len(col_data)*100, None, None, None, None, num_distinct_values]
        else:
            summary.loc[len(summary)] = [col, data_type, None, None, None, None, col_data.mode().values[0], (col_data == 0).sum()/len(col_data)*100, None, None, None, None, num_distinct_values]

        output_type = output_type.lower()
        if output_type == 'html':
            with open('output_file.html', 'w') as file:
                summary.to_html(file)
        elif output_type == 'xlsx' or output_type == 'excel':
            with open('output_file.xslx', 'w') as file:
                summary.to_html(file)
        elif output_type == 'markdown' or output_type == 'md':
            with open('output_file.md', 'w') as file:
                summary.to_markdown(file)
    
    return summary 

print(summarize_dataframe(pd.read_csv('test_dataset.csv'), 'xlsx'))
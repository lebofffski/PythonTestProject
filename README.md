# Data summarizer

Data summarizer is a Python program that provides descriptive analysis of each column of a dataframe. The algorithm takes dataframe and output type as an input and outputs a file with analyzed data.
Repository contains test_file.py with example of usage. It demonstrates perfomance with dataset uploaded with test_dataset.csv file.

## Usage
Create a directory and set as working; clone this repository; install the requested dependencies with pip from `requirements.txt`; run `test_file.py` for testing on a sample dataset or `main.py` to get a summary of target data.

```python
import main
#or 
from main import summarize_dataframe 

# function returns dataframe with descriptive summary for each column 
# and creates an output file with summarize data 
# with output format of choice (html, excel or markdown)

col_sum = summarize_dataframe(df, 'output_type')
print(col_sum)

```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
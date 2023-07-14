# Onion Data Type

The Onion data type is a hierarchical structure that allows for nesting subsets and performing statistical operations on the elements within those subsets. It provides flexibility in managing and analyzing data with various levels of granularity.

## Features

- Supports subsets of different data types, including DataFrames.
- Addition and removal of subsets.
- Statistical operations on the elements within subsets.

## Installation

To use the Onion data type, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/as-bestinclass/onionDatatype
   ```

2. Install the required dependencies:
   ```
   pip install pandas
   ```

3. Import the Onion class into your project:
   ```python
   from onion import Onion
   ```

## Usage

Create an Onion object by providing an initial list of subsets. Each subset can be of any data type, including DataFrames.

```python
import pandas as pd
from onion import Onion

# Create DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'X': [7, 8, 9], 'Y': [10, 11, 12]})

# Create an instance of Onion with initial subsets, including DataFrames
my_onion = Onion([df1, df2])
```

Perform operations on the Onion object, such as adding a new subset, removing a subset, or performing statistical operations on the elements within subsets.

```python
# Add a new DataFrame subset
df3 = pd.DataFrame({'C': [13, 14, 15], 'D': [16, 17, 18]})
my_onion.add_subset(df3)

# Remove a subset by index
my_onion.remove_subset(1)

# Perform a statistical operation on the Onion data (e.g., mean)
my_onion.perform_operation('mean')
```

Please refer to the class documentation in `onion.py` for more details on available methods and their parameters.

## Contributions

Contributions to the Onion data type are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

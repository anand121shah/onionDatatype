import pandas as pd

class Onion:
    def __init__(self, subsets):
        self.subsets = subsets
    
    def add_subset(self, subset):
        self.subsets.append(subset)
    
    def remove_subset(self, index):
        del self.subsets[index]
    
    def perform_operation(self, operation):
        # Implement statistical operations based on the provided 'operation' parameter
        # Perform the operations on the elements within the subsets
        # If a subset is a DataFrame, you can use pandas methods for statistical operations
        
        if operation == 'mean':
            for subset in self.subsets:
                if isinstance(subset, pd.DataFrame):
                    subset_mean = subset.mean()
                    print(f"Mean of DataFrame subset: {subset_mean}")
                else:
                    print("Subset is not a DataFrame. Skipping...")
        
    # Add additional methods as needed

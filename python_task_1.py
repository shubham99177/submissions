import pandas as pd


# def generate_car_matrix(df)->pd.DataFrame:
#     """
#     Creates a DataFrame  for id combinations.

#     Args:
#         df (pandas.DataFrame)

#     Returns:
#         pandas.DataFrame: Matrix generated with 'car' values, 
#                           where 'id_1' and 'id_2' are used as indices and columns respectively.
#     """
#     # Write your logic here

#     return df




def get_type_count(file_path):
    # Read the CSV file into a DataFrame
    dataframe = pd.read_csv(file_path)

    # Use cut within value_counts to create the 'car_type' column and count occurrences
    type_counts = dataframe['car'].pipe(lambda x: pd.cut(x, bins=[float('-inf'), 15, 25, float('inf')], labels=['low', 'medium', 'high'], right=False)).value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    dict = dict(sorted(type_counts.items()))

    return dict


file_path = 'dataset-1.csv'
result = get_type_count(file_path)
print(result)




def get_bus_indexes(file_path):
    # Read the CSV file into a DataFrame
    dataframe = pd.read_csv(file_path)

    # Calculate the mean value of the 'bus' column
    bus_mean = dataframe['bus'].mean()

    # Identify indices where 'bus' values are greater than twice the mean
    bus_indexes = dataframe[dataframe['bus'] > 2 * bus_mean].index.tolist()

    # Sort the indices in ascending order
    sorted_bus_indexes = sorted(bus_indexes)

    return sorted_bus_indexes
file_path = 'dataset-1.csv'
result = get_bus_indexes(file_path)
print(result)


def filter_routes(file_path):
    # Read the CSV file into a DataFrame
    dataframe = pd.read_csv(file_path)

    # Calculate the average value of the 'truck' column for each 'route'
    route_avg_truck = dataframe.groupby('route')['truck'].mean()

    # Filter routes where the average 'truck' value is greater than 7
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    # Sort the list of selected routes
    sorted_selected_routes = sorted(selected_routes)
    return sorted_selected_routes

file_path = 'dataset-1.csv'
result = filter_routes(file_path)
print(result)



def filter_routes(file_path):
    # Read the CSV file into a DataFrame
    dataframe = pd.read_csv(file_path)

    # Calculate the average value of the 'truck' column for each 'route'
    route_avg_truck = dataframe.groupby('route')['truck'].mean()

    # Filter routes where the average 'truck' value is greater than 7
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    # Sort the list of selected routes
    sorted_selected_routes = sorted(selected_routes)
    return sorted_selected_routes

file_path = 'dataset-1.csv'
result = filter_routes(file_path)
print(result)



# def time_check(df)->pd.Series:
#     """
#     Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

#     Args:
#         df (pandas.DataFrame)

#     Returns:
#         pd.Series: return a boolean series
#     """
#     # Write your logic here

#     return pd.Series()

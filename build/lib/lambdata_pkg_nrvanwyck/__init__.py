import pandas as pd
import seaborn as sns
from sklearn.utils.multiclass import unique_labels
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

def null_checker(df):
    """
    null_checker takes a pandas DataFrame and returns the number of nulls in each column.
    """
    assert isinstance(df, pd.DataFrame), 'argument must be a pandas DataFrame.'
    return df.isnull().sum(), sns.heatmap(df.isnull(), cbar=False)

def plot_confusion_matrix(y_true, y_pred):
    """
    plot_confusion_matrix takes actual target values and predicted target values and returns a labelled confusion matrix.
    """
    labels = unique_labels(y_true)
    columns = [f'Predicted {label}' for label in labels]
    index = [f'Actual {label}' for label in labels]
    table = pd.DataFrame(confusion_matrix(y_true, y_pred), 
                         columns=columns, index=index)
    fig = plt.figure(figsize=(10,6))
    plt.title('Confusion Matrix')
    return sns.heatmap(table, annot=True, fmt='d', cmap='viridis')
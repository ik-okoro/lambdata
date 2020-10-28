'''
nofan - a collection of useful Data science modules and functions
wrangler - a module to aid wrangling data
'''

# Access libraries through pipenv
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency as ch

class DfTweaker():
    """
    Dataframe class for some wrangling methods
    """
    
    def __init__(self):
        pass

    def date_converter(self, df, column, drop = False):
        """
        Takes a dataframe pandas datetime column and returns columns for day, month, and year
        Pass in column name as a string
        Set default parameter, drop as True to drop original date column before returning
        """
        df = df.copy()
        # Removed the raise error in case the column is not pandas datetime
        # Next lines require datetime so pandas would raise the error
        df["Day"] = df[column].dt.day
        df["Month"] = df[column].dt.month
        df["Year"] = df[column].dt.year
        
        # Return appropriate dataframe
        if drop:
            df.drop(column, axis = 1, inplace = True)
            return df
        else:
            return df


    def outliers(self, df, colName):
        """
        Takes a dataframe and name of a numerical column
        Removes outliers based on 1.5 * interquartile range rule
        Reports new dataframe shape and returns new dataframe
        Pass in column name as a string
        """
        df = df.copy()
        desc = df[colName].describe()

        # Calculate IQR from quarteriles
        iqr = desc.loc["75%"] - desc.loc["25%"]
        iqr = int(iqr)

        # Drop outliers
        df = df[(df[colName] < 1.5*iqr) | (df[colName] > 1.5*iqr)]
        print(f"Resulting shape of dataframe after removing outliers is {df.shape}")
        return df
    

    def chi_report(self, column1, column2, table = False):
        """
        Takes two features of a dataframe and returns a chi2 report of independence
        Set default parameter table as True to return normalized contingency table as well
        Pass columns as dataframe series as df[column1] or df.column1
        """
        chi_table = pd.crosstab(column1, column2, normalize = "index")*100

        # Compute chi2
        stat, p, dof, expected = ch(pd.crosstab(column1, column2))

        # Turn into report
        report = pd.Series([stat, p, dof, expected], index= ["Chi^2 Test Statistic", "p-value", "Degrees of Freedom", "Expected Frequencies"], name = "Chi^2 Report")

        if table:
            return report, chi_table
        else:
            return report




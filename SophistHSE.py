#Imports
import pandas as pd

#Class
class SophistHSE:
    def __init__(self):
        self.url = 'http://sophist.hse.ru/hse/1/tables/'
    
    #Transform str index to datetime index
    def __time_to_datetime__(self, df):
        current_year = df.index[0].split()[0]
        new_index = []
        for index, row in df.iterrows():
            lst = index.split()
            if len(lst) == 2:
                current_year = lst[0]
                new_index.append(pd.to_datetime(index))
            else:
                new_index.append(pd.to_datetime(current_year + ' ' + lst[0]))
   
        df.index = new_index
        return df
    
    #Parse Table
    def get_table(self, table):
        df = pd.read_html(self.url + table + '.htm', index_col = 0, decimal = ',', thousands = None,  na_values = '&nbsp')[0]
        df.rename(columns = df.iloc[0], inplace=True)
        df = df[df.index.notna()]
        df = df.drop(index = ['T'])
        df = self.__time_to_datetime__(df).astype(float)
        return df
# sophist.hse.ru Python Parser
A simple python module for parse statistical data from sophist.hse.ru

Inspired by https://github.com/bdemeshev/sophisthse (Package for R program language)

**Not tested on all datasets**

 
# How to use
1. Download sophiistHSE.py and and put it in the same directory with your working python file/notebook
2. Choose dataset on http://sophist.hse.ru/hse/nindex.shtml
3. Write in your python file:
```python
import pandas as pd
from SophistHSE import SophistHSE


HSE = SophistHSE()
table = 'CPI_M_CHI' #Put here name of dataset
df = HSE.get_table(table)
```

If you need plot, use the column name:
```python
import matplotlib.pyplot as plt
plt.plot(df['CPI_M_CHI'])
```

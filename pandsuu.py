# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 19:17:06 2022

@author: home
"""

import pandas as pd

# DataFrame Creation
sales_record = pd.DataFrame({'Products_ID': {0: 101, 1: 102, 2: 103,
                                 3: 104, 4: 105, 5: 106,
                                 6: 107, 7: 108, 8: 109},
                          'Product_Names': {0: 'Mosuse', 1: 'Keyboard',
                                   2: 'Headphones', 3: 'CPU',
                                   4: 'Flash Drives', 5: 'Tablets',
                                   6: 'Android Box', 7: 'LCD',
                                   8: 'OTG Cables' },
                          'Product_Prices': {0: 700, 1: 800, 2: 200, 3: 2000,
                                    4: 100, 5: 1500, 6: 1800, 7: 1300,
                                    8: 90},
                          'Product_Sales': {0: 5, 1: 13, 2: 50, 3: 4,
                                    4: 100, 5: 50, 6: 6, 7: 1,
                                    8: 50}})
  
# Specify the name of the excel file
file_name = 'ProductSales_sheet.xlsx'
  
# saving the excelsheet
sales_record.to_excel(file_name)
print('Sales record successfully exported into Excel File')
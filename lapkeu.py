# Melakukan import pandas dan upload file
import pandas as pd
lapkeu = pd.read_excel("Laporan Keuangan Index LQ45 Kuartal II 2023.csv")

# Cek missing value
lapkeu.isna().sum()

# Cek duplicated data
lapkeu.duplicated().sum()

# Cek type data
lapkeu.info()

# Menambahkan metric ke dalam dataset
lapkeu['Market Cap'] = lapkeu['Share'] * lapkeu['Price']
lapkeu['NPM'] = lapkeu['Net Profit'] / lapkeu['Revenue']
lapkeu['EPS'] = lapkeu['Net Profit'] / lapkeu['Share']
lapkeu['DY'] = lapkeu['Dividen Per Share'] / lapkeu['Price']
lapkeu['ROA'] = lapkeu['Net Profit'] / lapkeu['Aset']
lapkeu['ROE'] = lapkeu['Net Profit'] / lapkeu['Equity']
lapkeu['Book Value'] = lapkeu['Equity'] /lapkeu['Share']
lapkeu['PBV'] = lapkeu['Price'] / lapkeu['Book Value']
lapkeu['PER'] = lapkeu['Price'] / lapkeu['EPS']
lapkeu['DER'] = lapkeu['Liabilities'] / lapkeu['Equity']

# Menyimpan dataset baru dalam bentuk csv
lapkeu_new = lapkeu.to_csv("Laporan Keuangan New.csv")

# Menyimpan dataset baru dalam bentuk excel
lapkeu_new = lapkeu.to_excel("Laporan Keuangan New.xlsx")

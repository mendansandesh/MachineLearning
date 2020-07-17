import pandas as pd
import os
# inputDf = pd.read_csv('/home/inct-sandeshmendan/sandesh/ML/automation datasets/concat columns/supermarket-sales/supermarket_sales.csv')
# #pd.set_option('display.max_columns', None)
# df = inputDf.head(10)
# df['purchase keywords'] = 'Bought / Purchased a product: '  + df['Product line'] + ', through Payment mode: ' + df['Payment'].astype(str)
# #+ ', Unit price: ' + df['Unit price'] +', Quantity: ' + df['Quantity'] \
# df.to_csv(r'/home/inct-sandeshmendan/sandesh/ML/automation datasets/concat columns/supermarket-sales/sales.txt', header=None, index=None, sep=' ', mode='a', columns=['purchase keywords'])

#inputDf = pd.read_csv('/home/inct-sandeshmendan/sandesh/ML/automation datasets/concat columns/ecommerce-events-history-in-cosmetics-shop/2019-Dec.csv')

inputfolderpath = os.path.abspath(os.getcwd()) + '/'
inputFileName = inputfolderpath + 'mergeInput.csv' #modify
outputFile = inputfolderpath + 'purchase_keywords.txt'
print('Script is running at pwd: ' + inputfolderpath)
print('Processing..........')
inputDf = pd.read_csv(inputFileName)
df = inputDf.head(10) #comment this
print(df)
print('--------')
# modify below column names and sentence accordingly
col1= 'product'
col2 = 'payment'
df['purchase keywords'] = 'Bought / Purchased a product: '  + df[col1] + ', through Payment mode: ' + df[col2]
#df1 = df.dropna(thresh=1)
dfNew = df['purchase keywords']
# df.drop_duplicates()
dfNew.dropna().drop_duplicates().to_csv(outputFile, header=None, index=None, sep=' ', mode='a', columns=['purchase keywords'])
# print(df)
# df.applymap(str)
# print(df.dtypes) k

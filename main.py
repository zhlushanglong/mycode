import pandas_datareader.data as web
import datetime as dt
start = dt.datetime(2021,1,1)#获取数据的时间段-起始时间
#end = dt.datetime(2021,6,10)#获取数据的时间段-结束时间
end = dt.date.today()#结束时间为当前时间
stockData = web.DataReader("603927.SS", "yahoo", start, end)#股票为中科软，数据源为雅虎
stockData.to_csv('StockData/603927.csv')

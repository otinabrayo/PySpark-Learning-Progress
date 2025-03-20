import spark

df = spark.\
    read.\
    format('csv').\
    option('inferSchema',True).\
    option('header',True).\
    load('/BigMart Sales.csv')
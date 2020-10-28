from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext
sc = SparkContext(appName="NetworkWordCount")
ssc = StreamingContext(sc, 2)
ssc.checkpoint("./tmp/checkspark")
lines = ssc.socketTextStream("localhost",9999)
# lines = ssc.textFileStream('./Data/')
words = lines.flatMap(lambda line: line.split(" "))
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)
# wordCounts = pairs.reduceByKeyAndWindow(lambda x,y:x+y,lambda x,y: x-y, 6,2)
wordCounts.pprint(100)
ssc.start() 
ssc.awaitTermination()

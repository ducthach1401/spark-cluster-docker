from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark
sc = SparkContext(appName="NetworkWordCount",master="spark://36a53dfcbce2:7077")
ssc = StreamingContext(sc, 3)
lines = ssc.textFileStream('./Data/')
words = lines.flatMap(lambda line: line.split(" "))
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)

wordCounts.pprint(100)
ssc.start() 
ssc.awaitTermination()
from pyspark import SparkContext
from pyspark.files import SparkFiles
from pyspark.streaming import StreamingContext
import os
import sys
sc = SparkContext(appName="NetworkWordCount")
ssc = StreamingContext(sc, 2)
lines = ssc.textFileStream('./Data/')
words = lines.flatMap(lambda line: line.split(" "))
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)
wordCounts.pprint()
ssc.start() 
ssc.awaitTermination()
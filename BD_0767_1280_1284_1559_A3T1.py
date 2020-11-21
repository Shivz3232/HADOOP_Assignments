#!/usr/bin/python3

import sys
from pyspark.sql import SparkSession

word = sys.argv[1]
f1 = sys.argv[2]
f2 = sys.argv[3]

spark = SparkSession.builder.appName("Task1").getOrCreate()

lines = spark.read.format("csv").option("header", "true").load(f2)

lines = lines.select("word", "recognized", "Total_Strokes")
lines = lines.filter(lines["word"] == word).select("recognized", "Total_Strokes")

recognized = [int(row[0]) for row in lines.filter((lines["recognized"] == "True")).select("Total_Strokes").collect()]
unrecognized = [int(row[0]) for row in lines.filter((lines["recognized"] == "False")).select("Total_Strokes").collect()]

if len(recognized) == 0:
    print(0.00000)
else:
    print("%.5f" % (float(sum(recognized)) / float(len(recognized))))

if len(unrecognized) == 0:
    print(0.00000)
else:
    print("%.5f" % (float(sum(unrecognized)) / float(len(unrecognized))))

spark.stop()

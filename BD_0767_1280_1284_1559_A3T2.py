#!/usr/bin/python3

import sys
from pyspark.sql import SparkSession

word = sys.argv[1]
strokes = int(sys.argv[2])
f1 = sys.argv[3]
f2 = sys.argv[4]

spark = SparkSession.builder.appName("Task2").getOrCreate()

lines1 = spark.read.format("csv").option("header", "true").load(f1)
lines2 = spark.read.format("csv").option("header", "true").load(f2)

lines1 = lines1.filter((lines1["word"] == word))
lines2 = lines2.filter((lines2["word"] == word) & (lines2["recognized"] == "False") & (lines2["Total_Strokes"] < strokes))

res = lines2.join(lines1, "key_id", "left").select("countrycode").groupBy("countrycode").count().sort("countrycode").collect()

if len(res) == 0:
	print(0)
else:
	for i in res:
		print(i[0],i[1], sep=",")

spark.stop()

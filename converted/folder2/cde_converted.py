import pyspark

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

print("I am second folder")
from pyspark.sql import SparkSession
import time

spark = SparkSession.builder.getOrCreate()

start_time = time.time()

print("Hello")

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time)
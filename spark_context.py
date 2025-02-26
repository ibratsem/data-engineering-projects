from pyspark.sql import SparkSession

# Attempt to stop any existing Spark session if active
try:
    spark.stop()
except Exception as e:
    print("No active Spark session to stop:", e)

# Create a new Spark session to ensure the LiveListenerBus is active
spark = SparkSession.builder \
    .appName("SparkFixApp") \
    .enableHiveSupport() \
    .getOrCreate()

print("Spark session started successfully.")

# Build Spark context from Spark session
sc = spark.sparkContext
print("Spark context built:", sc)

# Test the new Spark session
spark.sql("select 1").show(10, False)

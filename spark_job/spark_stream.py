import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, expr
from pyspark.sql.types import StructType, IntegerType, DoubleType, StringType
from pyspark.ml import PipelineModel
from pyspark.ml.feature import VectorAssembler
from pyspark.ml import PipelineModel

# Define schema to match Kafka JSON
schema = StructType() \
    .add("user_id", IntegerType()) \
    .add("amount", DoubleType()) \
    .add("timestamp", StringType())

# Start Spark session
spark = SparkSession.builder \
    .appName("KafkaFraudDetection") \
    .master("local[*]") \
    .config("spark.hadoop.hadoop.native.lib", "false") \
    .getOrCreate()

spark.sparkContext._jsc.hadoopConfiguration().set("hadoop.native.lib", "false")

# Read stream from Kafka
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "transactions") \
    .option("startingOffsets", "latest") \
    .load()

# Convert value to JSON and parse schema
parsed_df = kafka_df.selectExpr("CAST(value AS STRING) as json_str") \
    .select(from_json(col("json_str"), schema).alias("data")) \
    .select("data.*")

# Simulate rolling average as a proxy (in real case, you'd compute over a window)
parsed_df = parsed_df.withColumn("avg_amount", expr("amount * 0.7"))
parsed_df = parsed_df.withColumn("deviation", col("amount") - col("avg_amount"))

# Assemble features for MLlib model
#vec_assembler = VectorAssembler(inputCols=["amount", "avg_amount", "deviation"], outputCol="features")
#featured_df = vec_assembler.transform(parsed_df)



# Load pre-trained MLlib model
model = PipelineModel.load("file:///home/ashish2511/fraud_project/fraud_model")

predictions = model.transform(parsed_df) \
    .select("user_id", "amount", "avg_amount", "deviation", "prediction")

# Predict using the model
# predictions = model.transform(featured_df) \
#     .select("user_id", "amount", "avg_amount", "deviation", "prediction")

# Output predictions to console
query = predictions.writeStream \
    .format("console") \
    .option("truncate", False) \
    .outputMode("append") \
    .start()

query.awaitTermination()

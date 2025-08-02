import os
os.environ["PYSPARK_PYTHON"] = r"C:\Users\User\AppData\Local\Programs\Python\Python310\python.exe"
from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.ml import Pipeline

# Start Spark
spark = SparkSession.builder.appName("ModelTrainer").getOrCreate()

# Fake historical data: user_id, amount, avg_amount, label
data = [
    (1, 100.0, 80.0, 0),
    (2, 1500.0, 200.0, 1),
    (3, 300.0, 290.0, 0),
    (4, 1800.0, 100.0, 1),
    (5, 250.0, 260.0, 0)
]

columns = ["user_id", "amount", "avg_amount", "label"]
df = spark.createDataFrame(data, columns)

# Create features
df = df.withColumn("deviation", df.amount - df.avg_amount)
vec_assembler = VectorAssembler(inputCols=["amount", "avg_amount", "deviation"], outputCol="features")

# Train model
lr = LogisticRegression(featuresCol="features", labelCol="label")
pipeline = Pipeline(stages=[vec_assembler, lr])
model = pipeline.fit(df)

# Save model
model.write().overwrite().save("fraud_model")
print("✅ Model saved as 'fraud_model'")

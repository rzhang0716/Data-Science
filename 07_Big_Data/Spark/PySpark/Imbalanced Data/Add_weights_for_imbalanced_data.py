# Check imbalance and compute weights
import pandas as pd
counts = df.groupBy('label').count().toPandas()
print(counts)

# Counts
count_ture = 26051 # number of less class count
count_total = 1465535 # total Counts

# Weights
c = 2 # number of classes for prediction
weight_true = count_total / (c * count_ture)
weight_false = count_total / (c * (count_total - count_ture))

# Append weights to the dataset
from pyspark.sql.functions import col
from pyspark.sql.functions import when

df = df.withColumn("weight", when(col("label") ==1, weight_true).otherwise(weight_false))

# Check everything seems ok
df.select('label', 'weight').where(col('label')==1).show(3)


# Split the dataset into train and test subsets
train, test = df.randomSplit([.8, .2], seed = 42)
print(f"""There are {train.count()} rows in the train set, and {test.count()} in the test set""")


ref: https://www.datatrigger.org/post/spark_3_weighted_random_forest/

# Bankruptcy Prediction with LightGBM Classifier
from pyspark.sql import SparkSession

# Bootstrap Spark Session
spark = SparkSession.builder.getOrCreate()

from synapse.ml.core.platform import running_on_synapse

if running_on_synapse():
    from notebookutils.visualization import display



df = (
    spark.read.format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .load(
        "wasbs://publicwasb@mmlspark.blob.core.windows.net/company_bankruptcy_prediction_data.csv"
    )
)
# print dataset size
print("records read: " + str(df.count()))
print("Schema: ")
df.printSchema()

# Train test split
train, test = df.randomSplit([0.85, 0.15], seed=1)

# Assemble the feature
from pyspark.ml.feature import VectorAssembler

feature_cols = df.columns[1:]
featurizer = VectorAssembler(inputCols=feature_cols, outputCol="features")
train_data = featurizer.transform(train)["Bankrupt?", "features"]
test_data = featurizer.transform(test)["Bankrupt?", "features"]

# Check the data is balanced or not
display(train_data.groupBy("Bankrupt?").count())

# Train the model
from synapse.ml.lightgbm import LightGBMClassifier

model = LightGBMClassifier(
    objective="binary", featuresCol="features", labelCol="Bankrupt?", isUnbalance=True
)

model = model.fit(train_data)

# Feature Importance Visualization
import pandas as pd
import matplotlib.pyplot as plt

feature_importances = model.getFeatureImportances()
fi = pd.Series(feature_importances, index=feature_cols)
fi = fi.sort_values(ascending=True)
f_index = fi.index
f_values = fi.values

# print feature importances
print("f_index:", f_index)
print("f_values:", f_values)

# plot
x_index = list(range(len(fi)))
x_index = [x / len(fi) for x in x_index]
plt.rcParams["figure.figsize"] = (20, 20)
plt.barh(
    x_index, f_values, height=0.028, align="center", color="tan", tick_label=f_index
)
plt.xlabel("importances")
plt.ylabel("features")
plt.show()

# Model Prediction
predictions = model.transform(test_data)
from synapse.ml.train import ComputeModelStatistics

metrics = ComputeModelStatistics(
    evaluationMetric="classification",
    labelCol="Bankrupt?",
    scoredLabelsCol="prediction",
).transform(predictions)
display(metrics)

###############################
# Quantile Regression for Drug Discovery with LightGBMRegressor
triazines = spark.read.format("libsvm").load(
    "wasbs://publicwasb@mmlspark.blob.core.windows.net/triazines.scale.svmlight"
)

train, test = triazines.randomSplit([0.85, 0.15], seed=1)

from synapse.ml.lightgbm import LightGBMRegressor

model = LightGBMRegressor(
    objective="quantile", alpha=0.2, learningRate=0.3, numLeaves=31
).fit(train)


print(model.getFeatureImportances())

scoredData = model.transform(test)
display(scoredData)

from synapse.ml.train import ComputeModelStatistics

metrics = ComputeModelStatistics(
    evaluationMetric="regression", labelCol="label", scoresCol="prediction"
).transform(scoredData)
display(metrics)

###############################
# LightGBM Ranker
df = spark.read.format("parquet").load(
    "wasbs://publicwasb@mmlspark.blob.core.windows.net/lightGBMRanker_train.parquet"
)
# print some basic info
print("records read: " + str(df.count()))
print("Schema: ")
df.printSchema()
display(df.limit(10))

from synapse.ml.lightgbm import LightGBMRanker

features_col = "features"
query_col = "query"
label_col = "labels"
lgbm_ranker = LightGBMRanker(
    labelCol=label_col,
    featuresCol=features_col,
    groupCol=query_col,
    predictionCol="preds",
    leafPredictionCol="leafPreds",
    featuresShapCol="importances",
    repartitionByGroupingColumn=True,
    numLeaves=32,
    numIterations=200,
    evalAt=[1, 3, 5],
    metric="ndcg",
)

lgbm_ranker_model = lgbm_ranker.fit(df)

dt = spark.read.format("parquet").load(
    "wasbs://publicwasb@mmlspark.blob.core.windows.net/lightGBMRanker_test.parquet"
)
predictions = lgbm_ranker_model.transform(dt)
predictions.limit(10).toPandas()


# Reference:
# 1. https://tamaracucumides.medium.com/learning-to-rank-with-lightgbm-code-example-in-python-843bd7b44574

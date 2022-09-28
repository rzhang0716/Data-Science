from pyspark.ml.feature import StringIndexer, IndexToString, OneHotEncoder, VectorAssembler
import pandas as pd
import numpy as np
from pyspark.ml import Pipeline
from pyspark.ml.tuning import CrossValidator
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

# one hot encoding and assembling
encoding_var = [i[0] for i in train.dtypes if (i[1]=='string') & (i[0]!='label') & (i[0]!='weight')]
num_var = [i[0] for i in train.dtypes if ((i[1]=='int') | (i[1]=='double')) & (i[0]!='label') & (i[0]!='weight')]

string_indexes = [StringIndexer(inputCol = c, outputCol = 'IDX_' + c, handleInvalid = 'keep') for c in encoding_var]
onehot_indexes = [OneHotEncoder(inputCols = ['IDX_' + c], outputCols = ['OHE_' + c]) for c in encoding_var]
label_indexes = StringIndexer(inputCol = 'label', outputCol = 'label_index', handleInvalid = 'keep')
assembler = VectorAssembler(inputCols = num_var + ['OHE_' + c for c in encoding_var], outputCol = "features")
lr = LogisticRegression(labelCol="label_index", featuresCol="features",weightCol='weight', maxIter=30)

pipe = Pipeline(stages = string_indexes + onehot_indexes + [assembler, label_indexes, lr])


evaluator = BinaryClassificationEvaluator()
paramGrid = ParamGridBuilder().addGrid(lr.regParam, [.01, .1, 1, 10]).addGrid(lr.elasticNetParam, [0, .5, 1]).build()

cv = CrossValidator(estimator=pipe, estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=5)
cv_mod = pipe.fit(train) # used for feature importance

prediction = cv_mod.transform(test)


from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Evaluation
evaluator = BinaryClassificationEvaluator()
# print("Test Area Under ROC: " + str(evaluator.evaluate(prediction, {evaluator.metricName: "areaUnderROC"})))

# Calculate the elements of the confusion matrix
TN = prediction.filter('prediction = 0 AND label_index = prediction').count() #216172
TP = prediction.filter('prediction = 1 AND label_index = prediction').count() #3127
FN = prediction.filter('prediction = 0 AND label_index <> prediction').count() #2012
FP = prediction.filter('prediction = 1 AND label_index <> prediction').count() #71353
# show confusion matrix
prediction.groupBy('label_index', 'prediction').count().show()
# calculate metrics by the confusion matrix
accuracy = (TN + TP) / (TN + TP + FN + FP)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
F =  2 * (precision*recall) / (precision + recall)
# calculate auc
evaluator = BinaryClassificationEvaluator()
auc = BinaryClassificationEvaluator(labelCol="label_index", rawPredictionCol="prediction")
auc = auc.evaluate(prediction)
print('n precision: %0.3f' % precision)
print('n recall: %0.3f' % recall)
print('n accuracy: %0.3f' % accuracy)
print('n F1 score: %0.3f' % F)
print('AUC: %0.3f' % auc)

# MulticlassClassificationEvaluation
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.evaluation import BinaryClassificationEvaluator

eval_accuracy = MulticlassClassificationEvaluator(labelCol="label_index", predictionCol="prediction", metricName="accuracy")
eval_precision = MulticlassClassificationEvaluator(labelCol="label_index", predictionCol="prediction", metricName="precisionByLabel")
eval_recall = MulticlassClassificationEvaluator(labelCol="label_index", predictionCol="prediction", metricName="recallByLabel")
eval_f1 = MulticlassClassificationEvaluator(labelCol="label_index", predictionCol="prediction", metricName="f1")

eval_auc = BinaryClassificationEvaluator(labelCol="label_index", rawPredictionCol="prediction")

accuracy = eval_accuracy.evaluate(lrPredictions)
precision = eval_precision.evaluate(lrPredictions)
recall = eval_recall.evaluate(lrPredictions)
f1score = eval_f1.evaluate(lrPredictions)

auc = eval_accuracy.evaluate(lrPredictions)

print('n precision: %0.3f' % precision)
print('n recall: %0.3f' % recall)
print('n accuracy: %0.3f' % accuracy)
print('n F1 score: %0.3f' % f1score)
print('AUC: %0.3f' % auc)

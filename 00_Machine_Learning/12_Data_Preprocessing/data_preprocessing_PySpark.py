train, test = stratified_split_train, stratified_split_test
from pyspark.ml.feature import StringIndexer, IndexToString, OneHotEncoder, VectorAssembler
import pandas as pd
import numpy as np
from pyspark.ml import Pipeline
from pyspark.ml.tuning import CrossValidator
from pyspark.ml.classification import GBTClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

# one hot encoding and assembling
encoding_var = [i[0] for i in train.dtypes if (i[1]=='string') & (i[0]!='label') & (i[0]!='weight')]
num_var = [i[0] for i in train.dtypes if ((i[1]=='int') | (i[1]=='double')) & (i[0]!='label') & (i[0]!='weight')]

string_indexes = [StringIndexer(inputCol = c, outputCol = 'IDX_' + c, handleInvalid = 'keep') for c in encoding_var]
onehot_indexes = [OneHotEncoder(inputCols = ['IDX_' + c], outputCols = ['OHE_' + c]) for c in encoding_var]
label_indexes = StringIndexer(inputCol = 'label', outputCol = 'label_index', handleInvalid = 'keep')
assembler = VectorAssembler(inputCols = num_var + ['OHE_' + c for c in encoding_var], outputCol = "features")
gbt = GBTClassifier(labelCol="label_index", featuresCol="features", weightCol='weight',seed = 42)

pipe = Pipeline(stages = string_indexes + onehot_indexes + [assembler, label_indexes, gbt])


evaluator = BinaryClassificationEvaluator()
# maxIter represents number of trees
# maxBins is used to reduce the number of values for continuous input features, to discretization or binning values into a fixed number of buckets.
# This can reduce the number of unique values for each feature from tens of thousands down to a few hundred.
paramGrid = ParamGridBuilder().addGrid(gbt.maxDepth, [4, 8, 16, 32, 64]).addGrid(gbt.maxBins, [128, 256, 512]).addGrid(gbt.maxIter, [100, 200, 500]).build()

cv = CrossValidator(estimator=pipe, estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=5)

cv_mod = pipe.fit(train)

prediction = cv_mod.transform(test)

auc = evaluator.evaluate(prediction, {evaluator.metricName: 'areaUnderROC'})
print('AUC: %0.3f' % auc)

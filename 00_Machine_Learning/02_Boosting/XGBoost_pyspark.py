train, test = df.randomSplit([0.8, 0.2], seed = 42)
from pyspark.ml.feature import StringIndexer, IndexToString, OneHotEncoder, VectorAssembler
import pandas as pd
import numpy as np
from pyspark.ml import Pipeline
from pyspark.ml.tuning import CrossValidator
from pyspark.ml.classification import GBTClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from sparkdl.xgboost import XgboostClassifier

# one hot encoding and assembling
encoding_var = [i[0] for i in train.dtypes if (i[1]=='string') & (i[0]!='label')]
num_var = [i[0] for i in train.dtypes if ((i[1]=='int') | (i[1]=='double')) & (i[0]!='label')]

string_indexes = [StringIndexer(inputCol = c, outputCol = 'IDX_' + c, handleInvalid = 'keep') for c in encoding_var]
onehot_indexes = [OneHotEncoder(inputCols = ['IDX_' + c], outputCols = ['OHE_' + c]) for c in encoding_var]
label_indexes = StringIndexer(inputCol = 'label', outputCol = 'label_index', handleInvalid = 'keep')
assembler = VectorAssembler(inputCols = num_var + ['OHE_' + c for c in encoding_var], outputCol = "features")
xgb = XgboostClassifier(num_workers=3, labelCol="label_index", missing=0.0)

pipe = Pipeline(stages = string_indexes + onehot_indexes + [assembler, label_indexes, gbt])


evaluator = BinaryClassificationEvaluator()
paramGrid = ParamGridBuilder().addGrid(xgb.maxDepth, [2, 5, 10]).addGrid(xgb.n_estimators, [50,100]).build() 

cv = CrossValidator(estimator=pipe, estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=5)

cv_mod = pipe.fit(train) # used for feature importance

prediction = cv_mod.transform(test)

auc = evaluator.evaluate(prediction, {evaluator.metricName: 'areaUnderROC'})
print('AUC: %0.3f' % auc)

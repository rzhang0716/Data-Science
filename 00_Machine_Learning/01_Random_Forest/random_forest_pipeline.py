train, test = df.randomSplit([0.8, 0.2], seed = 42)
from pyspark.ml.feature import StringIndexer, IndexToString, OneHotEncoder, VectorAssembler
from pyspark.ml import Pipeline
from pyspark.ml.tuning import CrossValidator
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

# one hot encoding and assembling
encoding_var = [i[0] for i in train.dtypes if (i[1]=='string') & (i[0]!='label')]
num_var = [i[0] for i in train.dtypes if ((i[1]=='int') | (i[1]=='double')) & (i[0]!='label')]

string_indexes = [StringIndexer(inputCol = c, outputCol = 'IDX_' + c, handleInvalid = 'keep') for c in encoding_var]
onehot_indexes = [OneHotEncoder(inputCols = ['IDX_' + c], outputCols = ['OHE_' + c]) for c in encoding_var]
label_indexes = StringIndexer(inputCol = 'label', outputCol = 'label_index', handleInvalid = 'keep')
assembler = VectorAssembler(inputCols = num_var + ['OHE_' + c for c in encoding_var], outputCol = "features")
rf = RandomForestClassifier(labelCol="label_index", featuresCol="features", seed = 42, numTrees=30, maxDepth=30)

# Create Pipeline for assembling and random forest
pipe = Pipeline(stages = string_indexes + onehot_indexes + [assembler, label_indexes, rf])


evaluator = BinaryClassificationEvaluator()
paramGrid = ParamGridBuilder().addGrid(rf.numTrees, [50, 100]).addGrid(rf.maxDepth, [10, 20, 30]).build()

# Cross Validation
cv = CrossValidator(estimator=pipe, estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=5)

cv_mod = pipe.fit(train) # used for feature importance

# Feature Importance
print(cv_mod.stages[-1].featureImportances)

prediction = cv_mod.transform(test)

# Read feature importance with varaible name
feature_importance_COVID_associated_hospitalization = ExtractFeatureImp(cv_mod.stages[-1].featureImportances, prediction, "features")
print(feature_importance_COVID_associated_hospitalization)

# Evaluate the model
auc = evaluator.evaluate(prediction, {evaluator.metricName: 'areaUnderROC'})
print('AUC: %0.3f' % auc)


# Function defined for reading feature importance with the model
def ExtractFeatureImp(featureImp, dataset, featuresCol):
   list_extract = []
   for i in dataset.schema[featuresCol].metadata["ml_attr"]["attrs"]:
       list_extract = list_extract + dataset.schema[featuresCol].metadata["ml_attr"]["attrs"][i]
   varlist = pd.DataFrame(list_extract)
   varlist['score'] = varlist['idx'].apply(lambda x: featureImp[x])
   return(varlist.sort_values('score', ascending = False))

from pyspark.ml.evaluation import BinaryClassificationEvaluator
evaluator = BinaryClassificationEvaluator()
print("Test Area Under ROC: " + str(evaluator.evaluate(prediction, {evaluator.metricName: "areaUnderROC"})))

# Calculate the elements of the confusion matrix
TN = prediction.filter('prediction = 0 AND label_index = prediction').count()
TP = prediction.filter('prediction = 1 AND label_index = prediction').count()
FN = prediction.filter('prediction = 0 AND label_index <> prediction').count()
FP = prediction.filter('prediction = 1 AND label_index <> prediction').count()
# show confusion matrix
prediction.groupBy('label_index', 'prediction').count().show()
# calculate metrics by the confusion matrix
accuracy = (TN + TP) / (TN + TP + FN + FP)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
F =  2 * (precision*recall) / (precision + recall)
# calculate auc
evaluator = BinaryClassificationEvaluator()
auc = evaluator.evaluate(prediction, {evaluator.metricName: 'areaUnderROC'})
print('n precision: %0.3f' % precision)
print('n recall: %0.3f' % recall)
print('n accuracy: %0.3f' % accuracy)
print('n F1 score: %0.3f' % F)
print('AUC: %0.3f' % auc)
        

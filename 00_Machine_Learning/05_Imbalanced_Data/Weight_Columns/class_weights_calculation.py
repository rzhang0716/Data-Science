from sklearn.utils import class_weight
y_train = df["label"]
class_weights = class_weight.compute_class_weight(class_weight = 'balanced',classes = np.unique(y_train),y = y_train)
print(class_weights)

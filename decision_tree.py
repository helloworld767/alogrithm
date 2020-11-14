import pandas as pd
import numpy as np
import collections
import heapq

data = {'色泽': ['青绿', '乌黑', '乌黑', '青绿', '浅白', '青绿', '乌黑', '乌黑', '乌黑', '青绿', '浅白', '浅白', '青绿', '浅白', '乌黑', '浅白', '青绿'],
        '根蒂': ['卷缩', '卷缩', '卷缩', '卷缩', '卷缩', '稍卷', '稍卷', '稍卷', '稍卷', '硬挺', '硬挺', '卷缩', '稍卷', '稍卷', '稍卷', '卷缩', '卷缩'],
        '敲声': ['浊响', '沉闷', '浊响', '沉闷', '浊响', '浊响', '浊响', '浊响', '沉闷', '清脆', '清脆', '浊响', '浊响', '沉闷', '浊响', '浊响', '沉闷'],
        '纹理': ['清晰', '清晰', '清晰', '清晰', '清晰', '清晰', '稍糊', '清晰', '稍糊', '清晰', '模糊', '模糊', '稍糊', '稍糊', '清晰', '模糊', '稍糊'],
        '脐部': ['凹陷', '凹陷', '凹陷', '凹陷', '凹陷', '稍凹', '稍凹', '稍凹', '稍凹', '平坦', '平坦', '平坦', '凹陷', '凹陷', '稍凹', '平坦', '稍凹'],
        '触感': ['硬滑', '硬滑', '硬滑', '硬滑', '硬滑', '软粘', '软粘', '硬滑', '硬滑', '软粘', '硬滑', '软粘', '硬滑', '硬滑', '软粘', '硬滑', '硬滑'],
        '密度': [0.697, 0.774, 0.634, 0.608, 0.556, 0.403, 0.481, 0.437, 0.666, 0.243, 0.245, 0.343, 0.639, 0.657, 0.360, 0.593, 0.719],
        '含糖率': [0.460, 0.376, 0.264, 0.318, 0.215, 0.237, 0.149, 0.211, 0.091, 0.267, 0.057, 0.099, 0.161, 0.198, 0.370, 0.042, 0.103],
        '好瓜':  [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

dataset = pd.DataFrame(data)
y_train = dataset['好瓜'].ravel()
x_train = dataset.drop(['好瓜'], axis = 1)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.criterion = None
        self.left, self.right = None, None


def decision_tree(x_train, y_train):
    if len(set(y_train)) == 1:
        return TreeNode(y_train[0])
    min_impurity = float('inf')
    for column in x_train.columns:
        if x_train[column].dtype == 'object':
            impurity = get_col_impurity(x_train[column], y_train, method='gini')
        else:
            impurity = get_continuous_impurity(x_train[column], y_train)
        if impurity[0] < min_impurity:
            min_impurity = impurity[0]
            criterion = (column, impurity[1])
    counts = np.bincount(y_train)
    node = TreeNode(np.argmax(counts))
    node.criterion = criterion
    if x_train[criterion[0]].dtype == 'object':
        flag = x_train[criterion[0]] == criterion[1]
    else:
        flag = x_train[criterion[0]] <= criterion[1]
    node.left = decision_tree(x_train[flag], y_train[flag])
    node.right = decision_tree(x_train[~flag], y_train[~flag])
    return node


def predict(tree, x):
    while tree.left or tree.right:
        if isinstance(x[tree.criterion[0]], str):
            if x[tree.criterion[0]] == tree.criterion[1]:
                tree = tree.left
            else:
                tree = tree.right
        else:
            if x[tree.criterion[0]] <= tree.criterion[1]:
                tree = tree.left
            else:
                tree = tree.right
    return tree.val


def get_col_impurity(feature, y_train, method = 'entropy'):
    feature_vals = set(feature)
    impurities = []
    feature_len = len(feature)
    for feature_val in feature_vals:
        flag = feature == feature_val
        feature_val_len = sum(flag)
        ratio = feature_val_len / feature_len
        if method == 'entropy':
            impurity = ratio * cal_entropy(y_train[flag]) + (1 - ratio) * cal_entropy(y_train[~flag])
        else:
            impurity = feature_val_len / feature_len * cal_gini(y_train[flag]) + feature_val_len / feature_len * cal_gini(y_train[~flag])
        heapq.heappush(impurities, (impurity, feature_val))
    return impurities[0]

def cal_entropy(y):
    count = collections.Counter(y)
    entropy = 0
    for i in count.values():
        entropy -= i / len(y) * np.log2(i / len(y))
    return entropy

def cal_gini(y):
    count = collections.Counter(y)
    gini = 1
    for i in count.values():
        gini -= np.square(i / len(y))
    return gini

def get_continuous_impurity(feature, y_train):
    feature_vals = sorted(list(set(feature)))
    impurities = []
    feature_len = len(feature)
    for i in range(1, len(feature_vals)):
        split = (feature_vals[i] + feature_vals[i - 1]) / 2
        flag = feature <= split
        feature_val_len = sum(flag)
        ratio = feature_val_len / feature_len
        impurity = ratio * cal_gini(y_train[flag]) + (1 - ratio) * cal_gini(y_train[~flag])
        heapq.heappush(impurities, (impurity, split))
    return impurities[0]

tree = decision_tree(x_train, y_train)

prediction = np.zeros(y_train.shape)
for i in range(len(y_train)):
    prediction[i] = predict(tree, x_train.loc[i]) == y_train[i]
accuracy = sum(prediction == y_train) / len(y_train)
print(prediction, y_train)

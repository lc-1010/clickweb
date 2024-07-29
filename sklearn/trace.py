import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from excel.excel_handler import ExcelHandler
# 分割数据集为训练集和测试集
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline


if __name__ == "__main__":
    excel_handler = ExcelHandler("/Users/c/Downloads/sex-1.csv","Sheet2")
    df = excel_handler.read_csv()
    # print(  df.iloc[:, 2].values )
    # print( df.iloc[:, 24].values)
    X_labeled = df.iloc[:417, 2].values  
    y_labeled = df.iloc[:417, 24].values 
    #print(y_labeled)
    # 检查 y_labeled 是否包含 NaN 值
    # # 将字符串转换为数值类型
    # y_labeled_numeric = pd.to(y_labeled, errors='coerce')   
    # 检查 y_labeled 是否包含 NaN 值
    nan_indices = df.iloc[:417][pd.isnull(y_labeled)].index

    if len(nan_indices) > 0:
        print("包含 NaN 值的行号：", nan_indices)
        print(df.get(56))
    else:
        print("y_labeled 不包含 NaN 值")

    #exit(0)
    X_unlabeled = df.iloc[417:, 2].values  # 从第418行开始是待标记的文本内容
    # 分割已标记数据为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X_labeled, y_labeled, test_size=0.24, random_state=40)
    # 特征提取
    vectorizer = CountVectorizer()
    X_train_counts = vectorizer.fit_transform(X_train)
    X_test_counts = vectorizer.transform(X_test)
    X_unlabeled_counts = vectorizer.transform(X_unlabeled)
    # print( X_train_counts)
    # print( y_train)
    # nan_values_X_train = np.isnan(X_train_counts.toarray()).any()
    # print("X_train_counts 中是否包含 NaN 值：", nan_values_X_train)
    # 打印 y_train 中的 NaN 值
    # 检查 y_train 中是否包含 NaN 值
    # 检查 y_train 中是否包含 NaN 值
    nan_values_y_train = pd.isnull(y_train).any()
    print("y_train 中是否包含 NaN 值：", nan_values_y_train)
    # 寻找包含 NaN 值的行的索引
    nan_indices = np.where(pd.isnull(y_train))[0]


    print("包含 NaN 值的行的索引：", nan_indices)
    num_nan_rows = len(nan_indices)
    print("包含 NaN 值的行数：", num_nan_rows)

    
    # 模型训练
    nb_classifier = MultinomialNB()
    nb_classifier.fit(X_train_counts, y_train)

    # # 将 y_test 转换为字符串类型
    y_test_str = y_test.astype(str)

    # # # 在测试集上进行预测
    predictions = nb_classifier.predict(X_test_counts)
    # 将 predictions 转换为字符串类型
    predictions_str = predictions.astype(str)

    # # # 评估模型性能
    accuracy = accuracy_score(y_test_str, predictions_str)
    print("已标记数据准确率：", accuracy)
    # 对待标记数据进行预测
    #unlabeled_predictions = nb_classifier.predict(X_unlabeled_counts)

    # 输出待标记数据的预测结果
    #print("待标记数据预测结果：", unlabeled_predictions)
    # 假设 unlabeled_predictions 是包含未标记预测的数组
    # for index, prediction in enumerate(unlabeled_predictions):
    #     if prediction != "色情":
    #         print(f"Index {index}: {prediction}")
    #         break

    # 使用 TF-IDF 特征提取
    # tfidf_vectorizer = TfidfVectorizer()
    # X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
    # X_test_tfidf = tfidf_vectorizer.transform(X_test)
    # X_unlabeled_tfidf = tfidf_vectorizer.transform(X_unlabeled)
    # # 模型训练
    # nb_classifier = MultinomialNB()
    # nb_classifier.fit(X_train_tfidf, y_train)
    # # 在测试集上进行预测
    # predictions_tfidf = nb_classifier.predict(X_test_tfidf)

    # # 评估模型性能
    # #accuracy_tfidf = accuracy_score(y_test, predictions_tfidf)

    # # 将 predictions_tfidf 转换为字符串类型
    # predictions_tfidf_str = predictions_tfidf.astype(str)

    # # 计算准确率
    # accuracy_tfidf = accuracy_score(y_test_str, predictions_tfidf_str)
    # print("TF-IDF 特征提取后的准确率：", accuracy_tfidf)

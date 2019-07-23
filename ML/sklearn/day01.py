from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Imputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
import jieba
import numpy as np


def dictvec():
    """
    数据字典抽取
    :return:
    """
    dv = DictVectorizer(sparse=False)
    data = dv.fit_transform([{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60}, {'city': '深圳', 'temperature': 30}])
    print(data)
    print(dv.get_feature_names())


def countvec():
    """
    对文本进行特征值化
    """
    vector = CountVectorizer()
    data = vector.fit_transform(["life is short short, I like Python", "life is too long , I dislike Python"])
    print(data)
    print(data.toarray())
    print(vector.get_feature_names())
    return None


def cutword():

    content1 = jieba.cut("今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。");
    content2 = jieba.cut("我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。");
    content3 = jieba.cut("如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。");

    # 转换成列表再转换为字符串
    c1 = ' '.join(list(content1))
    c2 = ' '.join(list(content2))
    c3 = ' '.join(list(content3))

    return c1, c2, c3;


def countvec_chs():
    """
    中文文本进行特征值化
    """
    vector = CountVectorizer()
    data = vector.fit_transform(cutword())
    print(data)
    print(data.toarray())
    print(vector.get_feature_names())
    return None


def tfidfvec():
    """
    TFIDF特征值化
    """
    vector = TfidfVectorizer()
    data = vector.fit_transform(cutword())
    print(data)
    print(data.toarray())
    print(vector.get_feature_names())
    return None


def minMaxScaler():
    """
    归一化处理
    :return:none
    """
    mm = MinMaxScaler()
    data = mm.fit_transform([[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]])
    print(data)
    return None


def standardScaler():
    """
    标准化处理
    :return:
    """
    std = StandardScaler()
    data = std.fit_transform([[1., -1., 3.], [2., 4., 2.], [4., 6., 1.]])
    print(data)
    return None


def imputer():
    """
    缺失值处理
    :return:
    """
    ipt = Imputer(missing_values="NaN", strategy="mean", axis=0)
    data = ipt.fit_transform([[1, 2], [np.nan, 3], [7, 6]])
    print(data)
    return None


def variance():
    """
    特征选择，删除低方差的特征
    :return:None
    """
    var = VarianceThreshold(threshold=0.0)
    data = var.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])
    print(data)
    return None


def pca():
    """
    主成分分析进行特征降维
    :return:
    """
    pca = PCA(n_components=0.9)
    data = pca.fit_transform([[2,8,4,5],[6,3,0,8],[5,4,9,1]])
    print(data)
    return None


if __name__ == "__main__":
    pca()

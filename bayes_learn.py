### 贝叶斯分类
import numpy as np
X = np.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
Y = np.array([1,1,1,2,2,2])

from sklearn.naive_bayes import GaussianNB

clf = GaussianNB(priors = None)
clf.fit(X, Y)
print(clf.predict([[-0.8,-1]])) # 第3象限的点似乎是1类点
print(clf.predict([[0.8,1]])) # 第1象限的点似乎是2类点

# 图示
gre_x, gre_y = [], [] # 第一类点
blu_x, blu_y = [], [] # 第二类点


for i in range(len(Y)):
    if Y[i] == 1:
        gre_x.append(X[i][0])
        gre_y.append(X[i][1])
    else:
        blu_x.append(X[i][0])
        blu_y.append(X[i][1])
        

plt.scatter(gre_x, gre_y, c='g', marker='.')
plt.scatter(blu_x, blu_y, c='b', marker='D')

# 参考线
plt.axvline(x=0, c = 'k',ls = '--', lw = 1)
plt.axhline(y=0, c = 'k',ls = '--', lw = 1)

plt.show()
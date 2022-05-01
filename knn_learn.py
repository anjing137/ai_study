x = [[0],[1],[2],[3]]
y = [0,0,1,1]

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3) #创建knn分类器

neigh.fit(x, y)
print(neigh.predict([[1.3]]))
# 0,1,2 是3个最近的邻居，根据投票法，最终将样本归类为0
print(neigh.predict([[1.6]]))
# 1,2,3 是3个最近的邻居，根据投票法，最终将样本归类为1
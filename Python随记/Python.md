## 1. Python

### 01. @lru_cache





### 03. Class中属性的命名规则

​	一般来说，我们给属性命名，假设类中有一个均值属性，我们叫它 mean，那么有如下规则：

​	**Public：**

​	self.mean ，公共属性，完全公开

​	**Protected：**

​	self._mean，受保护属性，开发者约定“请不要在类外直接访问”，但其实并不会限制

​	**Private：**

​	self.__mean，私有属性，名字会被改写，真正的限制访问



### 04. Numpy.random



### 05. Zip( )



















## 2. DeepLearning & ML

### 01. Keras

### 02. MLP

### 03. Dropout

### 04. L2正则化

### 05. ResNet

### 06. CNN

### 07. RNN

### 08. Transformer

### 09. NLP

### 10. Attention - based Model

### 11. 梯度消失

### 12. Random Forest

### 13. Gradient Boosting Trees



### 14. KNN

​		KNN（K Nearest Neighbor），K近邻算法。

​		**基本思想**：给定一个输入样本，找到在数据集中距离它最近的k个样本，采用多数投票的原则确定分类结果。

​		**关键步骤**：

   				1. 数据预处理
   				2. 距离计算：使用欧氏距离计算测试样本与训练样本的距离
   				3. 排序:对所有训练样本的距离从小到大排序
   				4. 选择前k个：取出距离最近的k个样本对应的标签（这里可以使用交叉验证来确定 k 值）
   				5. 多数投票：看哪一个标签出现的次数最多，作为分裂结果

​		**优缺点**：

​				优点：简单、易实现；对异常值不敏感；不需要模型训练，适合小规模数据。

​				缺点：预测时间慢（你在每次预测时都遍历了整个训练集）；受特征维度影响大（高维时效果差）；k的选择影响很大。



​		**有关KNN和交叉验证确定最优 k 值，可以参考''D:\桌面\大三\下\机器学习\实验报告2''**



### 15. 交叉验证

​		**交叉验证**（Cross-Validation）是一种用于评估弄清评估机器学习模型性能的技术，特别是在数据有限的情况下。它通过将数据集分成多个子集（通常称为“折”），在不同的子集上反复训练和测试模型，来估计模型在未见过数据上的表现。

​		**核心思想**：交叉验证的主要目的是通过模拟模型在独立测试集上的表现，来评估模型的**泛化能力**（即模型对新数据的预测能力）。它能有效减少过拟合（模型过于贴合训练数据而无法泛化）的影响，并提供更可靠的性能估计。



**有关k值范围的选择**：

常用的经验法则：

- 如果类别为偶数，一般选取奇数；如果类别为奇数，一般选取为偶数，这样可以**避免投票平局**
- 范围一般在 **1 到数据集规模的开方附近**，比如：
  - 训练集有 100 个样本 → 可以考虑 K 在 10 到 15 之间交叉验证
  - 更大的数据集，比如 10000 个样本 → 可以试 1~50，或按 5 的步长试 1, 5, 9, ..., 4



**优点**

- **更可靠的性能估计**：相比单一的训练-测试划分，交叉验证结果更稳定，减少随机划分的偏差。
- **数据高效利用**：所有数据都用于训练和验证，特别适合小数据集。
- **检测过拟合**：通过比较训练集和验证集性能，判断模型是否过拟合。

**缺点**

- **计算成本高**：需要多次训练模型，尤其是K较大或数据集较大时。
- **数据划分敏感性**：结果可能仍受随机种子或数据分布的影响（分层K折可缓解）。
- **泄漏风险**：若预处理（如特征缩放）在划分前进行，可能导致数据泄漏，影响结果真实性。

**应用场景**

- **模型选择**：比较不同模型或超参数组合的性能，选择最佳配置。
- **性能评估**：估计模型在未见过数据上的表现，用于报告或部署前验证。
- **小数据集**：在数据量有限时，最大化利用数据进行评估。

**注意事项**

- **数据预处理**：特征缩放、编码等预处理应在每折的训练集上单独进行，避免数据泄漏。
- **随机性**：设置随机种子以确保结果可重复。
- **计算资源**：对于大数据集或复杂模型，可选择较小的K或使用持出法以降低成本。
- **不平衡数据集**：使用分层K折以保持类别分布。







### 16. CAFFE





### 17. 特征缩放

​		在进行机器学习的过程中，输入样例的每个特征值之间的大小往往不同，以房价为例， x1表示面积， x2表示卧室数量，那么 x1的范围可能在 100到 300之间，而 x2在 1到 5之间，那么 w1和 w2对于损失函数的影响就不同，如下图：

![image-20250424090057207](C:\Users\30666\AppData\Roaming\Typora\typora-user-images\image-20250424090057207.png)

​		可以看到右边的损失函数图像，由于 x1的取值范围比 x2大得多，所以 w1只需要稍微改变就能很大程度影响到损失函数，相反的 w2则需要改变很多才能对损失函数造成影响。那么 w1的改变就可能导致损失函数在最小值的两边不断震荡，而 w2则会导致梯度下降过程过慢。为了解决这个问题，引入归一化（Normalization）。



#### 归一化

​		归一化包括最小-最大归一化和 Z-score归一化。

​		最小-最大归一化：
$$
x_{norm}=\frac{x - x_{min}}{x_{max}-x_{min}}
$$
​		Z-score归一化：
$$
x_{norm}=\frac{x - \mu}{\sigma}
$$
​		这样操作之后，特征基本上能够收敛到-1和 1之间，或者-3 到 3之间，从而使得 w 关于 损失函数的图像趋近于一个圆形，加快梯度下降。

![image-20250424091238204](C:\Users\30666\AppData\Roaming\Typora\typora-user-images\image-20250424091238204.png)





### 18. Naive Bayes

1. **理论基础**

   ​	朴素贝叶斯（Naive Bayes），这里其实我特指高斯朴素贝叶斯（Gaussian Naive Bayes）。是一种基于**贝叶斯定理**的概率分类算法，因其假设特征之间条件独立而得名“朴素”。它广泛用于分类任务，特别是在文本分类（如垃圾邮件过滤）和小规模数据集上表现优异。

   ​	朴素贝叶斯的核心是贝叶斯定理：
   $$
   P(C|X) = \frac{P(X|C) \cdot P(C)}{P(X)}
   $$

   - \(P(C|X)\)：后验概率，给定特征 \(X\)，样本属于类别 \(C\) 的概率。
   - \(P(X|C)\)：似然概率，给定类别 \(C\)，特征 \(X\) 的概率。
   - \(P(C)\)：先验概率，类别 \(C\) 的概率（通常基于训练数据估计）。
   - \(P(X)\)：证据，特征 \(X\) 的概率（归一化常数）。

   后续根据此公式进行推导的过程就不阐述了

2. **代码实现**

   ```python
   class NaiveBayes:
       def __init__(self):
           self.model = None
       # 数学期望
       @staticmethod
       def mean(X):
           return sum(X) / float(len(X))
       # 标准差（方差）
       def stdev(self, X):
           avg = self.mean(X)
           return math.sqrt(sum([pow(x - avg, 2) for x in X]) / float(len(X)))
       # 概率密度函数
       def gaussian_probability(self, x, mean, stdev):
           exponent = math.exp(-(math.pow(x - mean, 2) /
                                 (2 * math.pow(stdev, 2))))
           return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent
       # 处理X_train
       def summarize(self, train_data):
           summaries = [(self.mean(i), self.stdev(i)) for i in zip(*train_data)]
           return summaries
       # 分类别求出数学期望和标准差
       def fit(self, X, y):
           """
           训练模型
           :param X: 特征数据
           :param y: 标签数据
           :return: 训练结果
           """
           labels = list(set(y))
           data = {label: [] for label in labels}
           for f, label in zip(X, y):
               data[label].append(f)
           self.model = {
               label: self.summarize(value)
               for label, value in data.items()
           }
           return 'gaussianNB train done!'
       # 计算概率
       def calculate_probabilities(self, input_data):
           """
           计算概率
           :param input_data: 待预测的数据
           :return: 概率字典
           """
           probabilities = {}
           for label, value in self.model.items():
               probabilities[label] = 1
               for i in range(len(value)):
                   mean, stdev = value[i]
                   probabilities[label] *= self.gaussian_probability(
                       input_data[i], mean, stdev)
           return probabilities
       # 预测类别
       def predict(self, X_test):
           """
           预测类别
           :param X_test: 测试数据
           :return: 预测结果
           """
           label = sorted(self.calculate_probabilities(X_test).items(),
                          key=lambda x: x[-1])[-1][0]
           return label
       def score(self, X_test, y_test):
           """
           计算准确率
           :param X_test: 测试数据
           :param y_test: 测试标签
           :return: 准确率
           """
           right = 0
           for X, y in zip(X_test, y_test):
               label = self.predict(X)
               if label == y:
                   right += 1
           return right / float(len(X_test))
   ```

   

3. **代码中的关键点**

   - mean( ) 和 stdev( )：计算长=长度的时候都加了一个 float， 这是为了防止分子分母两个整数相除得到的还是整数，所以将分母 float 一下，这是为了保证精度
   - 最终的目的是要得到一个 model ，其类型是一个字典，格式如下：{label: [(mean1, stdev1), ...]}，其中 key 为 特征， value 为元组，包括该特征的均值和方差， len(model) 为特征数量

4. **优缺点**

   - 简单高效：计算复杂度低，训练和预测速度快（ 𝑂 ( 𝑚 ⋅ 𝑛 ) 训练， 𝑂 ( 𝑘 ⋅ 𝑛 ⋅ 𝑐 )  预测， 𝑐  为类别数）。
   - 对小数据集有效：需要较少的训练数据即可估计概率分布，适合小规模数据集。
   - 鲁棒性：对噪声和无关特征有一定鲁棒性，因独立性假设简化了模型。
   - 可解释性：基于概率的输出，易于理解和解释。
   - 适用混合特征：通过混合模型，可以处理连续和离散特征。

5. **使用场景**

   - 文本分类：垃圾邮件过滤、情感分析、主题分类（多项式或伯努利朴素贝叶斯）。
   - 小数据集分类：数据量少时，朴素贝叶斯比复杂模型（如 SVM、神经网络）更稳定。
   - 实时预测：计算速度快，适合在线分类任务。

​		





### 19. Overfitting

​		**过拟合（Overfitting）**，在机器学习中通常可以和 **高方差（High variance）**代指同一个意思，它是指预测函数在训练集上的拟合程度非常好，例如下面图片中最右边的图像，甚至可以认为这个预测函数的损失函数为 0，但是很明显，这个模型的拟合效果并不好。

![image-20250511142339233](C:\Users\30666\AppData\Roaming\Typora\typora-user-images\image-20250511142339233.png)



​		下图是另外一个例子，从左到右依次是 Underfitting、Just right 和 Overfitting，非常形象地展示了过拟合的具体表现。

![image-20250511143144864](C:\Users\30666\AppData\Roaming\Typora\typora-user-images\image-20250511143144864.png)



​		解决过拟合的几个方法：

- **收集足够多的训练集(Collect more training data)**：这是最直接也往往是最有效的方法之一。更多的数据可以帮助模型学习到更普适的规律，减少对训练数据中噪声的拟合。
- **特征选择** **(Feature selection)**：假设要预测房子的价格，影响因素包括房子的大小、地理位置、卧室数量、邻居收入等等特征一共 100 个，而此时训练集的数量又不够多，那么就会发生过拟合；此时若果想要解决过拟合问题，我们可以通过选择几个特定的特征来进行拟合，比如房子大小、地理位置和卧室数量。当然特征选择的缺点就是，一些有用的特征可能会被丢失。
- **正则化（Regularization）减少参数大小**：保留特征，但会防止特征产生过大的影响。





### 20. High Bias & High Variance

**高方差 (High Variance) vs. 高偏差 (High Bias):**

- **高方差 (Overfitting):** 模型对训练数据拟合得非常好，甚至学习到了训练数据中的噪声和随机波动，导致在测试数据上表现很差。模型过于复杂。
- **高偏差 (Underfitting):** 模型对训练数据拟合得不够好，没有捕捉到数据中的基本规律，导致在训练数据和测试数据上表现都很差。模型过于简单。
- 理想的模型是低偏差和低方差的。在实践中，两者之间往往存在一种权衡（Bias-Variance Tradeoff）。





### 21. Regularization



### 22. PCA



### 23. Kmeans













## 3. 数据结构与算法

### 01. 如何计算一个数的某一位

其实这个问题只需要知道两个点，设这串数字为x，一共有n位，那么：

​	第一，这串数字的首位数字为 x / 10的（n-1）次方

​	第二，这串数字的末尾数字为x%10



那么两位数其实很好求了，比如15，十位15/10 = 1，个位15%10 = 5

但是，对于百位千位数怎么办？

其实也是用这两步进行处理，比如数字2025，那么我们首先可以算出首位数，2025 / 1000 = 2，然后是个位数。2025 % 10 = 5，那么十位和百位呢，我们可以先将前两位数求出来，那就是2025 / 100 = 20，此时我们知道了这两位数为千位和百位，要求百位，那也就是求20的末尾，那么20 % 10 = 0，求得；十位也是一样的道理，所以对于四位数，有以下代码来实现求出各位数：

```python
# 一位四位数
x = int(input())
thousands = x // 1000
hundreds  = (x // 100) % 10
tens      = (x // 10) % 10
units     = x % 10
```

其他位数以此类推。

另外注意**Python里 // 是整除， / 是正常除法。**





### 02. 如何快速拿到数字某一位

​	上面介绍的是已知数据位数，如果不知道位数的话，这里有一种更简单的方法：

```python
def get_digit(n):
    # 这里输入的n为int
	number_list = []
    while n > 0:
    	number_list.append(n % 10)
        n = n // 10
    return number_list[::-1] # 这里要倒序输出，因为我们先从个位拿，拿到就放列表，所以最后拿到的会是一个相反的方向
		
```

​	当然你可能会问了，我用字符串分割一下直接取不更简单吗：

```python
def get_digit(n):
	# 这里输入的n为int
    #  这里解释一下为什么要这样写，首先map操作的对象一定要是 可迭代对象，那n是int，不可迭代，所以要先转化为字符串类型（这个类型可迭代），然后在转换为int，此时经过map操作后会返回一个map类型的变量，他是一个迭代器，直接输出不行，需要有一个list或者其他类型来接收，所以这里给map后的返回值list一下
    number_list = list(map(int,str(n)))
    
    return number_list # 这里就不用倒序了，因为是直接分割的
    
```

​	当然可以，而且这个似乎更加直观，但是有一个问题，在数据量大的时候，对字符串的迭代操作的时间复杂对会大于直接对数字进行操作，可以看蓝桥杯国赛的一个题目P10985，这个题目可以加深对上面两个函数的理解。



### 03. 线性筛（Euler 筛）

​		求素数的最优方法，时间复杂度O(N)

```python
def phi_sieve(n):
    phi = [0] * (n + 1)
    primes = []
    phi[1] = 1

    for i in range(2, n + 1):
        if phi[i] == 0:
            phi[i] = i - 1
            primes.append(i)

        for p in primes:
            if i * p > n:
                break
            if i % p == 0:
                phi[i * p] = phi[i] * p
                break
            else:
                phi[i * p] = phi[i] * (p - 1)
    return phi

```





### 04. 二分法

​		深度剖析一下二分法的底层逻辑，讲清楚二分法最容易弄混淆的边界问题以及条件结束问题。

​		首先，二分法的实现，包括左闭右闭和左闭右开，我个人比较喜欢左闭右开的写法，因为 Python 中几乎所有的切片还是什么操作，基本上都是左闭右开，具体代码实现如下：

```python
def bisect(nums, target):
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if target < nums[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo
```

​		这段代码有几个值得注意的点：

​		第一，为什么是 lo < hi  而不是 lo <= hi，其实这点很好理解，因为是左闭右开区间，所以当 lo < hi 的时候 [lo, hi) 才是有意义的，而如果是出现了 lo == hi，那么很显然  [lo, hi) 没有意义了；

​		第二，为什么 mid = lo + (hi - lo) // 2 而不是 mid = (lo + hi) // 2 ，这是为了防止两个数相加导致溢出，虽然 Python 不会溢出（int 是无线精度）但是**跨语言通用模板的标准写法**。

​		第三，最后为什么返回 lo 而不是 hi，其实最后循环结束的时候， lo == hi，返回 lo 和 hi 是一样的。（注意：仅适用于左闭右开写法）

​		第四，这种写法其实是 Python 内置 bisect() 的写法，**返回的是 target 右边界的后一位**，例如一个数组[1, 2, 2, 2, 3, 4]，target = 2，那么我的写法，返回的就是 4；那为什么这种写法返回的就是右边界呢，要实现左边界怎么做到呢，其实也很简单，把 target < nums[mid] 改成 target <= nums[mid] 就可以了。其实这里很值得详细说说，因为这涉及到二分法的边界处理，而往往二分的难点也就是在这里。

​		上面提到的，为什么 把 target < nums[mid] 改成 target <= nums[mid] 就可以实现返回左边界呢？我发现一般别人的代码喜欢把 nums[mid] 放在前面 target 放在后面这样比较，也就是 nums[mid] <  target，那么还有 nums[mid] <= target 的写法，看这么多头都大了，那怎么分辨那种写法返回的是左边界，那种返回的是右边界呢，其实一句话就可以理解。

​		比如我上面实现的 bisect 的写法，为什么是右边界，因为 else 中的条件是  target >= nums[mid]，此时 lo = mid + 1，怎样理解呢？当目标值target >= nums[mid] 的时候，lo 就要一直往右走，就要一直更新，直到 target >= nums[mid] 不成立，**这意味着你不断跳过相等的 target 往右走，最终 lo 会停在第一个大于 target 的位置。**这句话很重要，理解了这句话就能够随时写出返回左边界的代码，代码示例如下：

```python
def bisect_left(nums, target):
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if target <= nums[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo
```

​		为什么返回的是左边界，因为当 target <= nums[mid] 的时候，hi会不断跳过相等的 target 往左走，最终会停在第一个target 的位置。其实这里为什么是停在第一个 target 的位置，而不是和 bisect() 的返回值对称返回第一个target 前一个的位置，也是值得细细品味的。原因就是左闭右开区间。



| 边界类型 | 条件写法              | 目标     | 指针变化       | 最终含义                         |      |
| :------: | --------------------- | -------- | -------------- | -------------------------------- | ---- |
|  左边界  | `target <= nums[mid]` | 向左逼近 | `hi = mid`     | 找到第一个等于 target 的位置     |      |
|  右边界  | `target < nums[mid]`  | 向右跳过 | `lo = mid + 1` | 找到最后一个 target 的后一位位置 |      |
|          |                       |          |                |                                  |      |



### 05. 前缀和

一般来说，前缀和第一时间想到的实现是：

创建一个和 nums 长度一致的 prefix 数组，然后进行以下操作来实现

```python
n = len(nums)
prefix = [0] * n

for i in range(n):
    if i == 0:
        prefix[i] = nums[i]
    prefix[i] = prefix[i - 1] + nums[i]
```

但是这样会导致两个问题，第一，当 left = 0 的时候需要进行特判；第二，如果 nums 是空数组，这种写法无法兼容。



为了解决上述问题，选择初始化一个长度为 n + 1 的 prefix 即可解决

```python
n = len(nums)
prefix = [0] * (n + 1)

for i, x in enumerate(nums):
    prefix[i + 1] = prefix[i] + x 
```















## 4. 其他问题

### 1. 成对比较法

​	给定 2n 个数，找出其中的**最大值和最小值**，问**最少需要比较多少次**

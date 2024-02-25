---
comments: true
---
[TOC]



## 树

### 二叉树

Complete: a binary tree that is completely filled, with the possible exception of the bottom level, which is filled from
left to right. 
It is easy to show that a complete binary tree of height h has between 2h and 2h+1 - 1 nodes. This implies that the
height of a complete binary tree is log n , which is clearly O(log n)

#### Firstchild-nextsibling

- 表示方法不唯一

### 树的计算

$n=\sum_x \deg(x)+1$

> There exists a binary tree with 2016 nodes in total, and with 16 nodes having only one child.

设叶子节点有$x$个,则有$(2000-x)$个度为2的节点

$2(2000-x)+16+1=2016$

$2x=2017$, $x$不是正整数,所以无解

> Given a tree of degree 3. Suppose that there are 3 nodes of degree 2 and 2 nodes of degree 3. Then the number of leaf nodes must be ____.

$3\cdot 2+2\cdot 3+1\cdot y+1=x+y+5$,得$x=8$

### Threaded binary trees

一个二叉树,2n个指向孩子的指针,只有n-1个非空。利用

1. 如果x的左指针为空，就指向中序遍历中x的前一个元素
2. 如果x的右指针为空，就指向中序遍历中x的下一个元素
3. dummy head node。 

## Binary Search Tree

左子树的值<根节点<右子树

中序遍历得到顺序

## 堆

>  If a *d*-heap is stored as an array, for an entry located in position *i*, the parent, the first child and the last child are at:
>
>  $[(i+d-2)/d],(i-1)d+2,id+1$
>
>  第j个孩子是$(i-1)d+2+j$

二叉树，父节点是[i/2]

### 基本操作

**如果是最小堆，就取两个儿子中最小的。如果是最大堆，就和两个儿子中最大的比较。**

```c
void percolateDown(int* h,int x,int n){
    int maxchild=x;//最大堆
    if(x*2<=n&&h[x*2]>h[maxchild]) maxchild=x*2;
    if(x*2+1<=n&&h[x*2+1]>h[maxchild]) maxchild=x*2+1;
    if(maxchild!=x){
        swap(&h[x],&h[maxchild]);
        percolateDown(h,maxchild,n);
    }
}
```



### 线性建堆

从n/2到1 percolate down



> Among the following binary trees, which one can possibly be the decision tree (the external nodes are excluded) for binary search?

## 图论

### 图的遍历

>After the first run of Insertion Sort, it is possible that no element is placed in its final position.

如果是逆序，只有3个元素，则可以。T

>3.Apply DFS to a directed acyclic graph, and output the vertex before the end of each recursion. The output sequence will be:
>A.unsorted
>
>B.topologically sorted
>
>C.reversely topologically sorted
>
>D.None of the above

递归的顺序是遍历1->遍历2->遍历3->.....->遍历n->返回n->返回n-1...->返回3->返回2->返回1

返回的时候打印，因此是从最后一个结点开始打印到源点。是逆拓扑序。


>Use simple insertion sort to sort 10 numbers from non-decreasing to non-increasing, the possible numbers of comparisons and movements are:
A.100, 100

B.100, 54

C.54, 63

D.45, 44

看似好像很复杂：10个元素逆序的话：有C(10,2)=45的逆序对，因此交换的数目不会大于45 D

### 割点

articulation point: 去掉后增加连通分量的个数。 在边缘的单个点不算



### 最小生成树

#### Prim

```
1. 任取一个点作为初始的树
2. 对所有一端u在树上，一端v不在树上的边(u,v)，找出边权最小的，并将v加入到树
3. 重复2直到所有点都被加入
```

#### Kruskal

时间复杂度： 排序$O(E\log E)$, 并查集部分可以优化到$O(E\alpha(n))$,但最终还是$O(E\log E)$

## 排序

### 插入排序

```c
void insertionSort(int arr[], int n) {
    for (int P = 1; P < n; ++P) {
        int tmp = arr[P];
        int i;
        for (i = P; i > 0 && arr[i - 1] > tmp; --i)
            arr[i] = arr[i - 1];
        arr[i] = tmp;
    }
}
```

逆序对有$R(n)$个  那么插入排序时间复杂度为$O(R(n))$

插入不一定每次都有1个元素到原来的位置

### 希尔排序

$h_k-sort$  每$h_k$取一个元素,进行插入排序

1-sort就是插入排序

$h_k=h_{k+1}/2, h_t={n/2}$  最坏$O(n^2)$

```v
void shellSort(int arr[], int n) {
    int i, j, tmp;
    for (int inc = N/2; inc > 0; inc /= 2) {
        //默认的increment sequence
        for (i = inc; i < N; ++i) {
            //插入排序,注意从第二个元素(inc)开始,第一个元素是0
            tmp = arr[i];
            for (j = i; j >= inc; j -= inc) {
                if (tmp < arr[j - inc])
                    arr[j] = arr[j - inc];
                else break;
            }
            a[j] = tmp;
        }
    }
}

```

Hibbard sequence:$h_k=2^k-1$  最坏$O(n^{3/2})$  平均$O(n^{5/4})$

Sedgewick's   

### 堆排序

线性建堆法: 从最后一个非叶子节点(n/2)开始percolate down

- 朴素的实现,时间$O(n\log n)$, 辅助空间$O(n)$  

- 对空间优化到$O(1)$

建最大堆,将堆顶元素和最后一个元素交换(相当于删除最大元素,只不过把删除的元素放在了删除后留下的空间),并percolate down.  删除N-1次即可.

```c
void percolateDown(int* h,int x,int heapSize){
    int lson=x*2,rson=x*2+1;//heapSize随着删除会变
    int maxchild=x;//最大堆
    if(lson<=heapSize&&h[lson]>h[maxchild]) maxchild=lson;
    if(rson<=heapSize&&h[rson]>h[maxchild]) maxchild=rson;
    if(maxchild!=x){
        swap(&h[x],&h[maxchild]);
        percolateDown(h,maxchild,heapSize);
    }
}
void heapSort(int *a,int n,int stopPos){//数组从1开始
    for(int i=n/2;i>=1;i--){ //n/2
        percolateDown(a,i,n);//线性建
    }
    for(int i=n;i>=2;i--){
        swap(&a[1],&a[i]);//最大值换到最
        percolateDown(a,1,i-1);//从根开始 //如果是下标0开始,这里是(a,0,i)
    }
}
```

注意堆的索引是0开始还是1

### 快速排序

#### pivot

-  random  $O(n\log n)$
- median-of-three

无论pivot怎么选, Worse Case都是 $O(n^2)$

#### partition strategy

 $i$移动的条件是是 $a_i<pivot$ 还是 $a_i\leq pivot$?. 如果相等的时候i,j都不移动, 当元素全部相等的时候会不断交换i,j对应的元素.  但好处是两边分出的序列, 时间复杂度

#### small array

$n<20$  用insertion

### sorting large structures

交换两个结构体代价太大. 对指针排序

> During the sorting, processing every element which is not yet at its final position is called a "run". Which of the following cannot be the result after the second run of quicksort?
>
> A.5, 2, 16, 12, **28**, 60, 32, **72**
>
> B.**2**, 16, 5, 28, 12, 60, 32, **72**
>
> C.**2**, 12, 16, 5, **28**, **32**, 72, 60
>
> D.5, 2, **12**, 28, 16, **32**, 72, 60
>
> 2, 5, 12, 16, 28, 32, 60, 72 

快排每轮的pivot都会到最后的位置上. 快排2次, 3个pivot(如果第一轮pivot在边缘,就只有2个)  所以选D

```cpp
```



### 基于比较的排序的下界

决策树  每种排序结果对应一个叶子, 共$n!$个叶子   每次比较相当于两个分支.  二叉树的深度为$\log n!=O(n\log n)$

### 桶排序

$O(n+m)$

### 基数排序

Least Significant digit:

>1.建立0-9的桶
>
>2.放置：将元素按照最后一个字符放入桶中
>
>3.收集并更新桶：按照从0到9的桶序把桶中的元素按照第二字符放在对应的桶中（注意是从小到大取桶的,所以同一个桶里面十位相同,个位从小到大）
>
>4.重复3直到字符排完

$O(P(n+B))$

## 哈希

### separate chaining

对每个哈希值维护一个链表，存储哈希值为$i$的所有元素

- 插入和删除$O(1)$ （因为是链表)
- 查找最坏$O(n)$

>Given input {4371, 1323, 6173, 4199, 4344, 9679, 1989} and a hash function h(X)=X%10. If the collisions are solved by separate chaining with table size being 10, then the indices of the input numbers in the hash table are: (-1 means the insertion cannot be successful)
>A.1, 3, 3, 9, 4, 9, 9 (可以有相同的下标)

loading dencity factor: $\boxed{\lambda=\frac{n}{bs}}$

其中哈希函数有$b$个取值, 哈希表中元素个数$n$, $s$是slot个数()

### open addressing

当有冲突发生时，尝试选择其它单元，直到找到空的为止

```c
void insert(int key){
	index = hash(key);
    while(collision at index)
        index = (hash(key) + f(i)) % b;
    table[index] = key;
}
```



#### linear probing
$f(i)=i$
如果冲突，就一个一个往后找，直到找到空位

```c
void insert(int key) {
    index = hash(key);
    while(collision at index)
        index = (index + 1) % b;//注意取模，是循环着遍历整个哈希表
    table[index] = key;
}

```

#### quadratic probing
$f(i)=i^2$
相比线性探测，每次找的下标是$h(x)+1,h(x)+4,h(x)+9 (\mod T)\dots$
> if the table size is prime and the table is at least half empty, a new element can always be inserted with quadratic probing

> Given a hash table of size 13 and the hash function h(x)=x%13. Assume that quadratic probing is used to solve collisions. After filling in the hash table one by one with input sequence { 10, 23, 1, 36, 19, 5 }, which number is placed in the position of index 6?
>
> 36 （注意冲突了2次,i=3,(10+3^2)%9=6)

#### double hashing
$f(i)=i*h_2(x), h_2(x)=R-(x\mod R)$  $R$是略小于tablesize的质数

> - make sure the table size is prime
> - 理论上
> - 但二次探测已经足够了（因为计算哈希比较快）

>Given input {4371, 1323, 6173, 4199, 4344, 9679, 1989} and a hash function *h*(*X*)=*X*%10. If the collisions are solved by open addressing hash table with second hash function *h*2(*X*)=7−(*X*%7) and table size being 10, then the indices of the input numbers in the hash table are: (-1 means the insertion cannot be successful)

### Rehashing

把Tablesize扩大到原来的2倍，然后把原来哈希表里的元素插入。 哈希函数不变，但因为TableSize变了，哈希的情况也不同。

> Suppose that the numbers {4371, 1323, 6173, 4199, 4344, 9679, 1989} are hashed into a table of size 10 with the hash function *h*(*X*)=*X*%10, and hence have indices {1, 3, 4, 9, 5, 0, 2}. What are their indices after rehashing using *h*(*X*)=*X*%*T**ab**l**e**S**i**ze* with linear probing?
>
> TableSize变为20   11, 3, 13, 19, 4, 0, 9


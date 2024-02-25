---
comments: true
---
[TOC]

## composition

ways of inclusion

- fully has(是这个类独有的) 
- by reference

用初始化列表

一般内部的object都是private, 但是如果要在外部调用它的成员函数，就设成public

client class

## inheritance

### access control

- public 
- private可被本类成员和**友元**(friend)访问，**不能被子类访问**
- protected **可被子类访问** 和friends访问

继承关系

| Inheritance Type | public         | protected      | private |
| :--------------- | :------------- | :------------- | :------ |
| B: public A      | public in B    | protected in B | private |
| B: private A     | private in B   | private in B   | private |
| B: protected A   | protected in B | protected in B | private |

```cpp
class A{
private:
    int i;
protected:
    int ii;
public:
    A(){}
    A(int _i){i=ii=_i;}
    void print(){printf("%d %d\n",i,ii);}
    ~A(){}
};
class B: public A{//B是A的派生类
public:
    void set(int x){
        //i=x; 错误,不可访问
        ii=x;//正确
    }
};
```

如果父类和子类有相同的变量名，**优先调用子类的**。

### c'tors

调用顺序:
1. 构造**基类**（可能继续递归下去，先构造基类的基类，基类的成员变量... 
2. **成员变量**的构造函数
3. 派生类的构造函数

What is not inherited?

- **构造函数没有被继承**，但父类的构造会被自动调用。析构同理。
- **赋值的运算符不会被继承**。
- **友元不会被继承**
- 可以多继承（多个基类

- **先构造父类，再构造子类**。会调用父类的默认构造函数对父类的变量进行初始化
- 子类**不能访问父类的私有变量**，但**私有变量存在于这个类中**。

如何对父类私有变量初始化?: 当调用子类的构造函数时，我们不能调用父类的私有变量，只能用**初始化列表的方式调用父类的构造函数**进行初始化。

```c++
class B: public A{
public:
    B(){}
    B(int _i):A(_i){}//这样i=ii=_i
}
```



### function overload

当子类和父类有同名函数的时候

- 会调用自身重新定义的函数
- 在子类中重新定义函数后，**父类所有重载的同名函数被隐藏，无法使用**！
    - 用virtual解决

```cpp
#include<iostream>
#include<cstdio>
class A{
private:
    int i;
protected:
    int ii;
public:
    A(){}
    A(int _i){i=ii=_i;}
    void print(){printf("A: i=%d ii=%d\n",i,ii);}
    void print(int x){printf("%d :%d\n",x,i);}
    ~A(){}
};
class B: public A{
public:
    void set(int x){
        ii=x;//i=x; 错误,不可访问
    }
    void print(){
        printf("B: %d\n",ii);
    }
};
int main(){
    B b;
    b.set(20);
    b.print();//输出B: 20  原因:子类中重新定义
    b.print(10);//错误! 不能调用父类的print(int x) 
    //原因:重新定义子类的print之后,父类所有名字为print的函数被隐藏
    A* ptr=&b;
    ptr->print();//输出A: 0 20   原因: B中存在父类继承过来的i,但i未初始化(会报Warning)
}
```



### friends

指定类或者函数，可以访问private和public

```c++
class A{
    friend class B;//B可以访问A的成员变量，但A不能访问B
};
```



```cpp
class B;//前向声明
class A{
private:
    int numA
    friend class B;//声明B是A的friend
public:
    int add(B b){
        return b.numB+numa;//错误,friend是单向的
    }
};
class B{
private:
    int numB;
public:
    int add(A a){
        return a.numA+numB;//因为B是A的friend,可以访问A的private numB:
    }
};
```

全局函数是friend

```cpp
class A{
    int numA;
    friend int addAB(class A,class B);//声明
};
class B{
    int numB;
    friend int addAB(class A,class B);//声明
};
int addAB(A a,B b){
    return a.numA+b.numB;
}
```

## 习题

> the output at //1 is  114 ; the output at //2 is  303062 ; the output at //3 is  115 ; the output at //4 is  303062

```c++
#include<bits/stdc++.h>
using namespace std;
class A{
    int i;
public:
    A(int ii=0):i(ii) { cout<<ii<<" "<< 1; }
    A(const A& a) {
        i = a.i;
        cout << 2;     
    }
    void print() const { cout << 3 << i; }
};

class B : public A {//继承,本身要调用一次A的构造函数
    int i;
    A a;//组合，再调用一次A
public:
    B(int ii = 0) : i(ii) { cout << 4; }
    B(const B& b) {
        i = b.i;
        cout << 5;
    }
    void print() const {
        A::print();
        a.print();
        cout << 6 << i;    
    }
};

int main()
{
    B b(2);        //1
    b.print();    //2
    B c(b);        //3
    c.print();    //4
}
```


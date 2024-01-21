[TOC]
## Function in C++
### lifecycle/scope

### default arguments

**默认值必须从最右边往左**,只需要在声明中指出。在定义的时候不需要重复定义
```cpp
int f(int x,int y=1,int z=0);//ok
int g(int x,int y=1,int z);//illegal
```



### inline

类似宏的

- 代码长度增加，时间减少

inline may not in-line: 

- 由编译器控制,加inline也不一定内联, 不加也可能自动内联
- 现在inline关键词的含义是可重复定义(**multiple definition are permitted**):   inline的函数相当于声明，所以重复定义也没关系了。

#### inline function in class

在类内**定义**(不是声明)的函数会默认变成内联函数

### pass parameter

传入:

```c++
class A;
f(A x);//会复制
f(A* p);//不会复制，如果则加const
f(A& p);//不会复制,如果不想修改则加const
```

- pass in a const pointer/reference if want to get values

传出:

函数尽量不要返回指针(delete的时候容易出问题)。

- 如果不关心效率,则返回object
- 如果想要高效率,就把引用当做参数传进去

- **Never new something and return the poin**ter

## `::`resolver

- `<Class Name>::<function name>`
- `::<function name>` 代表全局的
## Reference

定义一个别名 

- local or global variables: `type& refname=name` name只能是变量不能是`i*3`之类的表达式

- 函数调用中的参数 `void f(int &x);`  函数调用的时候才绑定. 在函数内部修改外部变量

- can't be null

- are dependent on an existing variable, they are an alias for an **variable**.  

- **一旦定义后不能更改**   **`T& c=a, c=b` 相当于修改`a=b`, 但`c`的值就是a的值**  

    ```cpp
        int a=1,b=2;int& c=a;
        cout<<a<<" "<<b<<" "<<c<<" "<<"\n";//1 2 1
        c=b;
        cout<<a<<" "<<b<<" "<<c<<" "<<"\n";//2 2 2
        c=3;
        cout<<a<<" "<<b<<" "<<c<<" "<<"\n";//3 2 3
    ```

    在定义引用的时候，就已经和引用变量绑定了，不能再修改

- 可以对指针进行引用.反过来不行

    ```cpp
    f(int*& p);//ok
    int&* p;//illegal
    ```

    如何判断指针类型



const引用

`const int& z=x`.  不能写z, 但是x本身是可写的

```cpp
void f(int& x){};
void g(const int& x){};
f(i*3);//error
g(i*3);//ok
```

## const

- Constants are variables

    - Observe scoping rules
    - Declared with `const` type modifier

- A const in C++ defaults to internal linkage

    - the compiler tries to avoid creating storage for a const（存在symbol table中)
    - extern forces storage to be allocated

- Compile time constant(编译阶段就知道值)

    ```cpp
    const int size=8;//定义的时候复制
    extern const int x;//声明的时候不能给值
    ```

- Run-time constant

    ```cpp
    int x;
    cin>>x;
    const int y=x;//ok
    ```

    ```cpp
    cin>>x;
    const int sz=x;
    int array[sz];//C++98 error
    ```

- Aggregates:

    ```cpp
    const int i[]={1,2,3,4};//ok
    ```

    会分配存储空间(意义是这一段空间的内容不能改变)，但在编译期不能使用它的值

    ```cpp
    double d[i[3]];//error
    ```

    

### pointer and const

- **若const在*前面，表示指向的内容不可修改**： `const A* p`和`A const *p` 都是合法的
- **若const在*后面，表示指针本身不可修改**

```cpp
char * const q="abc"//指针q是const,指向的内容也是const
q++;//error
*q='c';//error
const char * p="ABCD"//指针p不是const,指向的内容是const
p="DEF";//ok
*p='c';//error

int i=3;
int* const pi2=&i;//pi2是const,指向的内容不是const（只是普通的int
(*pi2)=2;//ok
pi2++;//error
```

第一种: `*p` 是const char, p指向的地址可以修改，但不能通过 p 修改 p 指向的值。 把char换成int同理

第二种: q指向的地址不能被修改,比如`q++,q--`

```cpp
const int ci=3;
int *p=&ci;
const int *p=&ci;
```

### const objects

```c++
const currency a(48);
```

#### const member functions

内部成员函数可能会改成员变量的，所以要定义member functions const

```cpp
int Date::getday() const {
    day++;//Error,函数内部不能修改成员变量
    return day;//ok
}
```

const对象**只能调用有const修饰的成员函数**

好的习惯: 如果没有改变成员变量的值，就设为const函数

#### constant int class

```cpp
class A{
    const int i;
}
```

**必须在初始化列表里初始化i,否则会出错**

#### compile-time constant in class

```cpp
class A{
    const int size=2;
    int a[size];//Error!
}
```

**必须要在前面加static**

```c
class A{
    static const int size=100;//static代表所有object共用一个
	int a[size];//ok!
}
```

或者用anonymous enum hack

### 特例:字面字符串

```cpp
char *s="ABCD";//为了兼容C,这里s实际上是const char
			  //不能修改s指向的字符串的内容！！！！
char s[]="ABCD";//这样就可以修改字符串的内容
```

## static

- for local stuff: persistence
- for global: external linkage

static local variable: 实际上是全局变量，但只能在当前函数中访问

static global variable/static free function:  只能在本文件中访问，其他.cpp文件不能使用该变量

static member variable: 在这个类内所有的对象都维持相同的值，对象 A 修改了变量x,  那么对象 B 的变量x的值也会改变

```c++

//引用static member的两种方式
A::var_static;//推荐
a.var_static;
```



static member function:  所有对象共享的，只能访问static member variable
- 没有this指针



## Namespace

可出现多次
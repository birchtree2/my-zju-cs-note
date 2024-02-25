---
comments: true
---
不能重载的运算符: 
`.`  `::` 

 `.*`    

`?:`(三目) `sizeof` `typeid` `static_cast` `dynamic_cast` `const_cast` `reinterpret_cast`

https://en.cppreference.com/w/cpp/language/operators



## 重载的方式

| Expression |  As member function  | As non-member function |      |
| :--------: | :------------------: | :--------------------: | ---- |
|            |                      |                        |      |
|     @a     |  (a).operator@ ( )   |     operator@ (a)      |      |
|    a@b     |  (a).operator@ (b)   |    operator@ (a, b)    |      |
|    a=b     |  (a).operator= (b)   |  cannot be non-member  |      |
|  a(b...)   | (a).operator()(b...) |  cannot be non-member  |      |
|  a[b...]   | (a).operator[](b...) |  cannot be non-member  |      |
|    a->     |  (a).operator-> ( )  |  cannot be non-member  |      |
|     a@     |  (a).operator@ (0)   |    operator@ (a, 0)    |      |

### as member function

写在类里面  

- Implicit first argument: 如重载a+b, 只需要写`const T operator + (const T &b)`     `a`作为`*this`
- **No type conversion performed on receiver**  只会对第二个参数做类型转换
- **`=,(),[],->`只能在类里面定义**

```c++
#include<bits/stdc++.h>
class T{
public:
    T(int n=0):x(n){}
    const T operator + (const T &b)const{
        return x+b.x;
    }
   T operator -(){return -x;}//单目的
private:
    int x;
};
int main(){
    T x,y,z;
    z=x+y;//正确 相当于x.operator +(y)
    z=x+3;//正确 相当于x.+(3) 因为我们定义了T(int n),编译器会对3自动构造
    z=3+y;//错误!!  编译器不会把3变成T类型
}
```



### as global function

- **Explicit first argument**
- **两个参数都会类型转换**

- 访问类的私有变量,需要**在类里声明friend**

```c++
#include<bits/stdc++.h>
class T{
public:
    T(int n=0):x(n){}
    const T operator + (const T &b)const{return x+b.x;}
    friend const T operator - (const T &a,const T &b);
private:
    int x;
};
const T operator-(const T &a, const T &b) { //声明过了,定义的时不需要加friend
    return a.x-b.x; //因为要访问私有的x, 所以在类里面要声明friend
}
int main(){
    T x,y,z;
    z=x.operator+(y);
    z=x+3;
    // z=3+y; error
    z=3-y;//ok
}
```

### const

3处const

```c++
const/*(1)*/ T operator X (const/*(2)*/ T &b) const/*(3)*/;
```

- (1)对返回值:  算术运算,应该返回const object, 这样不会作为左值.   `[],<<,>>`应该返回引用
- (2)对参数  和成员函数一样,如果不修改参数,用const&
- (3)和成员函数一样, 如果不修改对象本身的成员,用const

## 重载的例子

### 常用模板

```c++
const T operator +(const T &l,const T &r)
template<typename T> Vector<T>::T& operator [] (int i)
const T operator + (const T &l,const T &r);//返回值加const防止作为左值

bool operator == (const T &other) const;//注意const
bool operator == (const T &l,const T&r) const;

T& operator [] (int i){//注意引用,没有const
    if(/*不越界*/) return m[i];
    throw ERROR();
}
```



### prefix/suffix ++

```c++
const T& operator ++(){//++a
    *this+=1;
    return *this;
}
const T operator ++(int){//a++
    T old(*this);
    ++(*this);//复用上面定义的++()
    return old;
}
```

### operator []

```c++
T& operator [](int index){
	return a[index];
}
```

### stream operator

```c++
friend std::ostream& operator<<();

istream & oeprator >>(istream &)
ostream &operator <<(ostream &os, const A &a){
    os << a.size() << endl;
    return os;
}
istream& operator >>(istream &is,A &a){//因为要修改a
	
}
```

### 赋值运算

T& operator =
T& operator [] (int i)


```c++
T& T::operator=( const T& rhs ) {
    if ( this != &rhs ) {// check for self assignment
     // perform assignment
    }
	return *this;//记得返回自己
}

```

### 类型转换

构造函数的方法和重载运算符的方法,不能同时用

#### 用构造函数 

```c++
class PathName {
 string name;
public:
 explicit PathName(const string&);//string-->PathName
 ~ PathName();
};
...
string abc("abc");
PathName xyz(abc); // OK!
xyz = abc; // error!  如果不加explicit就ok
```





#### 用重载运算符

```c++
A::operator B(){}
class Rational {

 // Rational to double
     operator double() const {
        return numerator_/(double)denominator_;
     }
} 
```

#### static,dynamic,const,reinterpret_cast

static_cast主要用于
1.基本类型的转换，比如int转char
2.类的**上行转换**，**子类的指针或者引用转换为基类**（安全）
类的下行转换不安全

dynamic_cast用于类的指针或引用的转换
1.类的上行转换，子类的指针或引用转化为基类（安全）
2.类的**下行转换**，**基类的指针或引用转化为子类**
（因为有类型检查所以是安全的，但类型检查需要运行时类型信息，这个信息位于虚函数表中，所以**必须要有虚函数**） 如果失败，变成空指针

const_cast 主要是用于改变类型的常量属性：常量指针转化为非常量指针；常量引用转化为非常量引用；常量对象转化。为非常量对象

reinterpret_cast用于非关联类型的转换，**操作结果是一个指针到其他指针的二进制拷贝，没有类型检查**。

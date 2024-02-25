---
comments: true
---
## polymorphism

多态： 同一句代码(如函数调用)，但实际执行中可能会有多种执行方式

### up-casting

向上造型，把为对象当成父类来对待，但并没有改变对象的值

用父类的指针/引用指向子类，**只能调用父类的函数**，子类的被隐藏了

```c++
Manager pete( "Pete", "444-55-6666","Bakery");
Employee* ep = &pete; // Upcast
Employee& er = pete; // Upcast
ep->print(cout);//调用父类的print()
```

### virtual function

`virtual` 定义了虚函数，意味着子类**可能**出现这个函数的新版本

- static binding： call the function as the code
- dynamic binding： call the function as the object  编译器会根据对象的类型调用不同的函数
    - virtual关键字告诉编译器使用动态绑定。  否则即使利用指针调用，也是静态绑定。

- 在虚函数中，默认参数的解析是静态的，不是动态的。因此，使用的是基类函数中 x 的默认值

仍然可以在子类中调用父类的被 overide 的函数

```c++
#include<bits/stdc++.h>
using namespace std;
class Entity{
public:
    virtual string getName(){//定义虚函数
        return "Entity";
    }
};
class Player:public Entity{
    string name;
public:
    Player(string _name):name(_name){}
    string getName(){
        return name;
    }
};
void print(Entity *p){
    //输出为Entity \n Cirno
    cout<<p->getName()<<endl;
    //因为getName()是virtual类型， p是动态绑定. 
    //虽然代码里写的是Entity*, 但是会根据传进来的对象类型决定调用哪个类的getName()
    //如果不加virtual, 就是静态绑定，调用Entity类的getName(), 输出Entity \n Entity
}
int main(){
    Entity entity;
    Player player("Cirno");
    print(&entity);
    print(&player);
}
```
#### virtual的编译器实现

虚函数表

对象里放了一个指向虚函数表的指针`VPTR` 

`VPTR` 只会在构造函数执行的时候对其进行赋值。

```cpp
Ellipse elly(20F, 40F);
Circle circ(60F);
elly = circ; 
elly.render(); // Ellipse::render()
```

但是用指针的时候

```c++
Ellipse* elly = new Ellipse(20F, 40F);
Circle* circ = new Circle(60F);
elly = circ; //指向circle
elly->render(); // Circle::render()
```

#### virtual dtor

如果析构函数不是virtual的，

### override

- overload  名字一样,参数不一样
- override 父类和子类的两个函数是虚函数的，名称相同，参数列表也相同名字一样，参数一样

### call up the chain

仍然可以在子类中调用父类的被 override 的函数。不需要重写代码

```cpp
void Derived::func() {
    cout << "In Derived::func!";
    Base::func(); // call to base class
    
}
```

- don't redefine inherited non virtual function: 不会报错，但不会发生多态, 会出现意想不到的结果

### return types relaxation

- Suppose D is publicly derived from B
- `D::f()` can return a subclass of the return type defined in `B::f()`
- 返回值只能**pointer and reference types**

```cpp
class Expr{
public:
    virtual Expr* newExpr();
    virtual Expr& clone();
    virtual Expr self();
};
class BinaryExpr:public Expr{
public:
    virtual BinaryExpr* newExpr();	//ok
    virtual BinaryExpr& clone();	//	ok
    virtual BinaryExpr self();	//error
};

```

因为本质上是upcast,只能通过引用和指针实现



### abstract class

pure virtual function `virtual xxx func()=0;`

- 条件: 有一个虚函数=0（纯虚函数
- 特点：**不能创建对象**

https://blog.csdn.net/YMGogre/article/details/126952858

#### interface class

- 所有非静态的函数是纯虚函数（析构函数除外
- 析构函数是虚的，且为空`virtual ~A(){}`
- 没有非静态成员变量(可以有静态的)
可安全的多继承（不会有重名问题

## 多继承(MI)

会继承所有父类的成员变量

```c++
class B1 { int m_i; };
class D1 : public B1 {};
class D2 : public B1 {};
class M : public D1, public D2 {};
void main() {
    Mm; //OK
    B1* p = new M; // ERROR: which B1
    B1* p2 = dynamic_cast<D1*>(new M); // OK
}
```

问题: 变量重名

安全的方式: protocol(interface) class

尽量不要出多继承

## copy ctor

`T(const T& t)`



### **调用拷贝构造**的情况

- 函数传参(call by value) `func(T t)`   调用`func(a)`  就会把a拷贝到t
- 函数返回一个对象  （但编译器可能会优化
- **定义**变量时(初始化)  看前面有没有类名，如`A a1=a2,A a1(a2)` **都是拷贝构造**

```cpp
Person baby_a;
Person baby_c( baby_a ); //初始化,调用拷贝构造
Person baby_b = baby_a; // 虽然用了=,也是初始化,调用拷贝构造


Person p1;
p1=p2;//赋值
p1=p3;//赋值
```

定义变量时做的是初始化，其他时候是赋值。
初始化是要拷贝构造，赋值要重载赋值运算符。一个对象只能被构造（初始化）一次，析构一次，但可以被赋值很多次。

### Default ctor

如果没有定义拷贝构造函数，C++会自己生成一个

- Copies each member variable
    - 如果成员是另一个对象,会调用它的拷贝构造函数
    - copies pointer!!!   析构的时候可能会出问题   a,b都有一个指针p, a析构时把p指向的内容释放了,b用的时候就出错



```
class Base{
protected:
    int x;
public:
    Base(int b=0): x(b) { }
    virtual void display() const {cout << x << endl;}//const
};
class Derived: public Base{
    int y;
public:
    Derived(int d=0): y(d) { }
    void display() {cout << x << "," << y << endl;}//没有const
};
int main()
{
  Base b(1);
  Derived d(2);
  Base *p = &d;
  b.display();
  d.display();
  p->display();
  return 0;
}
```

父类有const,子类没有const,类型不一样，不会形成多态。因此p->display调用的是Base的display
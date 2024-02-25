---
comments: true
---
### throw

- throw 用于抛出异常（可以抛出任意东西，一般是一个类），然后离开这个大括号（有点像 return ），直到被匹配的 catch 捕捉到
-  **throw 之后的语句都不会执行** 在栈中的本地变量都会被正确析构，但 throw 出来的东西直到 catch 之后才被析构

### try

### catch
- catch的时候**不会进行隐式类型转换**  比如throw了1,不会被`catch(double)` 而是`catch(int)`
- `catch(...)`表示捕获任意类型
- `catch`之后默认异常就不会继续传递了，但花括号中`throw`再次抛出


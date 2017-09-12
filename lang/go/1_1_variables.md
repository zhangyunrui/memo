1. 可只指定类型，也可只赋值(由编译器自动推断类型)；若在函数内部，可用更简略的":="赋值。
```go
var x int
var f float32 = 1.6
var s = "abc"

func main() {
    x := 123
}
````

2. 可一次定义多个变量
```go
var x, y, z int
var s, n = "abc", 123


var (
    a int
    b float32
)

func main() {
    n, s := 0x1234, "Hello, World!"
}
```

3. 多变量赋值时，先计算所有相关值，再从左至右依次赋值
```go
data, i := [3]int{0, 1, 2}, 0
i, data[i] = 2, 100
// (i = 0) -> (i = 2), (data[0] = 100)
````

4. "_"用于占位
```go
i := 0  //若变量未被使用会报错，可以用"_ = i"避免
```

5. 注意重新赋值与定义新同名变量的区别
```go
s := "abc"
println(&s)

s, y := "hello", 20 // 重新赋值: 与前 s 在同一层次的代码块中,且有新的变量被定义。
println(&s, y) // 通常函数多返回值 err 会被重复使用。

{
    s, z := 1000, 30
    // 定义新同名变量: 不在同一一层次代码块。
    println(&s, z)
}
```
输出:
```go
0x2210230f30
0x2210230f30 20
0x2210230f18 30
```
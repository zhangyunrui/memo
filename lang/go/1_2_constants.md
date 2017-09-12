1. 在常量组中，若不提供初始化值，那么视作与上一常量相同
```go
const (
    s = "abc"
    x // x = "abc"
)
````

2. 枚举
  - 关键字 iota 定义常量组中从 0 开始按行行计数的自自增枚举值
```go
const (
    Sunday = iota // 0
    Monday // 1,通常省略后续行行表达式。
    Tuesday // 2
    Wednesday // 3
    Thursday // 4
    Friday // 5
    Saturday // 6
)
```
```go
const (
    _ = iota // iota = 0
    KB int64 = 1 << (10 * iota) // iota = 1
    MB // 与 KB 表达式相同,但 iota = 2
    GB
    TB
)
```

  - 在同一一常量组中,可以提供多个 iota,它们各自自增⻓长。
```go
const (
    A, B = iota, iota << 10 // 0, 0 << 10
    C, D // 1, 1 << 10
)
```

  - 如果 iota 自自增被打断,须显式恢复。
```go
const (
    A = iota // 0
    B // 1
    C = "c" // c
    D // c,与上一一行行相同。
    E = iota // 4,显式恢复。注意计数包含了 C、D 两行行。
    F // 5
)
```

3. 可以通过自定义类型来实现枚举类型限制
```go
type Color int

const (
    Black Color = iota
    Red
    Blue
)

func test (c Color) {}

func main() {
    c := Black
    test(c)
    
    x := 1
    test(x) // Error: cannot use x (type int) as type Color in function argument
    test(1) // 常量会被编译器自自动转换。
}
```
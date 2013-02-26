def a() -> "bar":
 pass

def a(x: "bar",):
 return x

def c(x: "bar", y: "baz") -> "bleb":
 return x*y



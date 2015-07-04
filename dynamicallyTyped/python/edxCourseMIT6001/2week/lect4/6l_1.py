x = 12
def g(x):
      x = x + 1
      def h(y):
          return x + y
      return h(6)

print g(x)

def foo(x):
   def bar(x):
      return x + 1
   return bar(x * 2)

print foo(3)

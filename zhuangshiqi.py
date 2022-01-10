"""
装饰器在执行调用的函数前会先执行装饰器中的函数
"""
def logging_decorator(func): #只有一个参数，即要修饰的函数sum
    def logging_wrapper(*args, **kwargs): #定义了一个函数logging_wrapper返回logging_wrapper，并替代原修饰函数
        print(f'Before {func.__name__}')
        func(*args, **kwargs) #装饰器应用到sum函数
        print(f'After {func.__name__}')

    return logging_wrapper

@logging_decorator
def sum(x, y):
    print(x + y)

def test_func():
    a = '123'
    print(logging_decorator.__name__) #函数拥有name属性，会显示其原来的名称

if __name__ == '__main__':
    # test_func()
    sum(3,2)

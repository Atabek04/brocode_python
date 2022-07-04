def hello(**kwargs):
    # print("Hello", kwargs['first'], kwargs['last'])
    print("HELLO", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(first="Atabek", last="Shadimatov", middle="Ulugbekovich", nick="coder")

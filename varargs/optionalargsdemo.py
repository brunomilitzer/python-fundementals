def my_fun(x, *pos_param, **key_param):
    print(x)
    print(pos_param)

    for each_args in pos_param:
        print(each_args)

    for key, val in key_param.items():
        print(key, ":", val)

    modified_pos_param = pos_param+(50,)
    my_fun2(*modified_pos_param, **key_param)

#    print(kwargs)


def my_fun2(*args, **kwargs):
    print(args)
    print(kwargs)


my_fun(10, 20, 30, 40, name="Bruno", salary=4000)
# my_fun(10, name="Bruno", salary=4000)

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)


args = ("um", 2, 3)
test_args_kwargs(*args)
kwargs = {'arg3': 3, 'arg2': 'dois', 'arg1': 'um'}
test_args_kwargs(**kwargs)

#args = ("um", 2, 3, 'quatro')
#kwargs = {'arg3': 3, 'arg2': 'dois', 'arg1': 'um', 'arg4':'cuatro'}
#test_args_kwargs(*args)
#test_args_kwargs(**kwargs)
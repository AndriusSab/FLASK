# import functools
# import time

# def timer(func):
#     """Print the runtime of the decorated function"""
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()    # 1
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()      # 2
#         run_time = end_time - start_time    # 3
#         print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
#         return value
#     return wrapper_timer

# @timer
# def waste_some_time(num_times):
#     for _ in range(num_times):
#         sum([i**2 for i in range(10000)])

# print(waste_some_time(10000))
# import functools

# def debug(func):
#     """Print the function signature and return value"""
#     @functools.wraps(func)
#     def wrapper_debug(*args, **kwargs):
#         args_repr = [repr(a) for a in args]                      # 1
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
#         signature = ", ".join(args_repr + kwargs_repr)           # 3
#         print(f"Calling {func.__name__}({signature})")
#         value = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {value!r}")           # 4
#         return value
#     return wrapper_debug

# @debug
# def make_greeting(name, age=None):
#     if age is None:
#         return f"Howdy {name}!"
#     else:
#         return f"Whoa {name}! {age} already, you are growing up!"
    
# print(make_greeting("ANdrius", 30))

# import functools
# import time

# def slow_down(func):
#     """Sleep 1 second before calling the function"""
#     @functools.wraps(func)
#     def wrapper_slow_down(*args, **kwargs):
#         time.sleep(1)
#         return func(*args, **kwargs)
#     return wrapper_slow_down

# @slow_down
# def countdown(from_number):
#     if from_number < 1:
#         print("Liftoff!")
#     else:
#         print(from_number)
#         countdown(from_number - 1)
        
# print(countdown(10))




# import random
# PLUGINS = dict()

# def register(func):
#     """Register a function as a plug-in"""
#     PLUGINS[func.__name__] = func
#     return func

# @register
# def say_hello(name):
#     return f"Hello {name}"

# @register
# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"

# def randomly_greet(name):
#     greeter, greeter_func = random.choice(list(PLUGINS.items()))
#     print(f"Using {greeter!r}")
#     return greeter_func(name)

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat
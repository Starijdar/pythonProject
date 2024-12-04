import sys
import time
import inspect

def introspection_info(obj):
    info = {'Type': type(obj).__name__, 'Attribute': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
            'Method': [meth for meth in dir(obj) if callable(getattr(obj, meth))]}
    module = inspect.getmodule(obj)
    if module:
        info['Module'] = module.__name__
    elif module is None:
        info['Module'] = '__main__'
    return info

number_info = introspection_info(42)
print(number_info)

modulegetter = inspect.getmodule(time)
print(modulegetter.__name__)

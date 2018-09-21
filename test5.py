class OopsException(Exception):
    pass

try:
    raise OopsException('Caught an Oops')
except OopsException as e:
    print(e)
    

def document_it(func):
    def new_func(*args,**kwargs):
        print('start')
        result = func(*args,**kwargs)
        print(result)
        print('end')
        return result
    return new_func

def good():
    return ['hww']

new_good = document_it(good)
new_good()


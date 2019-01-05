'''we can create own error class by inherting existing classes or by inherting exception class'''
class My_TypeError(TypeError):
    def __init__(self,message,statuscode):
        super().__init__(f'message:{message},status:{statuscode}')



def raise_custom_error():
    raise My_TypeError("Some Error occured",  404)

#raise_custom_error()

class My_Custom_Excepion(Exception):
    def __init__(self,message,statuscode):
        super().__init__(f'messgae:{message},statusCode:{statuscode}')

def Raise_Custom_Eror():
    raise My_Custom_Excepion("Some Error Occured",405)

Raise_Custom_Eror()



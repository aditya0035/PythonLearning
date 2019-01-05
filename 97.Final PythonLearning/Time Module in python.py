import  time

def power(numb):
    return [x**2 for x in range(numb)]

start_time=time.time()
power(5000)
end_time=time.time()

print(end_time-start_time)


def Measuretime(function):
    start=time.time()
    function()
    end=time.time()
    return  end-start

print(Measuretime(lambda :power(5000)))


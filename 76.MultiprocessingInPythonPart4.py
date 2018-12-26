from concurrent.futures import  ProcessPoolExecutor
def Complex_Calculation():
    x=[x**2 for x in range(10000000)]
    return x

result1,result2=(0,0)
if __name__=='__main__':
    with ProcessPoolExecutor(max_workers=2) as pool:
        future1= pool.submit(Complex_Calculation)
        future2= pool.submit(Complex_Calculation)
        result1,result2=future1.result(),future2.result()
    print(result1)
    print("--------------")
    print(result2)

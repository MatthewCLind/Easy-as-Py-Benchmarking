import EZ_Benchmark as ezb
from math import sqrt


ezb.mark('start test')
for i in range(100):
    sqrt(i)
    ezb.mark(str(i))

ezb.save_results()

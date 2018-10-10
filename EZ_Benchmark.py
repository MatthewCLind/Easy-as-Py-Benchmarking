from time import time


start_time = -1
last_time = 0
results = []


def mark(label):
    global start_time
    global last_time
    global results
    
    if(start_time == -1):
        start_time = time()
        last_time = start_time
    new_time = time()
    total_time = new_time - start_time
    incremental_time = new_time - last_time
    last_time = new_time
    add_result(label, incremental_time, total_time)


def add_result(label, incremental_time, total_time):
    global start_time
    global last_time
    global results
    
    result = {'label':label, 'increment':incremental_time, 'total time':total_time}
    results.append(result)


def clear():
    global start_time
    global last_time
    global results

    start_time = -1
    last_time = 0
    results = []


def save_results(filename = 'results.csv'):
    global start_time
    global last_time
    global results
    
    with open(filename, 'w') as f:
        f.write('label,increment,total time\n')
        for result in results:
            f.write(result['label'] + ',' + str(result['increment']) + ',' + str(result['total time']) + '\n')
        clear()
        f.write('\n' + self_test())


def self_test(n = 10000):
    global last_time
    global results
    
    for i in range(n):
        mark(i)
    total_time = last_time - start_time
    return 'Benchmark Self Test\nTotal time for n=' + str(n) + ': ' + str(total_time) + '\nAverage mark time for n=' + str(n) + ': ' + str(total_time / n)
    
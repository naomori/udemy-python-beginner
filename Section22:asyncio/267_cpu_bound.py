import concurrent.futures
import os
import time


LARGE_TEXT = 'some string' * 1024 * 1024 * 10

def cpu_bound():
    i = 0
    while i < 1024*1024*10:
        i = i + 1 - 2 + 3 - 4 + 5
    return 'Future is done!'

if __name__=='__main__':
    start = time.time()
    print(cpu_bound('1.txt'))
    print(cpu_bound('2.txt'))
    end = time.time()
    print('I/O bound: Sync {:.4f}\n'.format(end - start))

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        start = time.time()
        future1 = executor.submit(cpu_bound, '1.txt')
        future2 = executor.submit(cpu_bound, '2.txt')
        print(future1.result())
        print(future2.result())
        end = time.time()
        print('CPU bound: Thread {:.4f}\n'.format(end - start))

    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        start = time.time()
        future1 = executor.submit(cpu_bound, '1.txt')
        future2 = executor.submit(cpu_bound, '2.txt')
        print(future1.result())
        print(future2.result())
        end = time.time()
        print('The number of cpu: {}'.format(os.cpu_count()))
        print('CPU bound: Thread {:.4f}\n'.format(end - start))
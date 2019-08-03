import concurrent.futures
import os
import time


LARGE_TEXT = 'some string' * 1024 * 1024 * 10

def io_bound(file_name):
    with open(file_name, 'w+') as f:
        f.write(LARGE_TEXT)
        f.seek(0)
        f.read()

    os.remove(file_name)
    return 'Future is done!'

def cpu_bound():
    i = 0
    while i < 1024*1024*10:
        i = i + 1 - 2 + 3 - 4 + 5
    return 'Future is done!'

if __name__=='__main__':
    start = time.time()
    print(io_bound('1.txt'))
    print(io_bound('2.txt'))
    end = time.time()
    print('I/O bound: Sync {:.4f}\n'.format(end - start))

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        start = time.time()
        future1 = executor.submit(io_bound, '1.txt')
        future2 = executor.submit(io_bound, '2.txt')
        print(future1.result())
        print(future2.result())
        end = time.time()
        print('I/O bound: Thread {:.4f}\n'.format(end - start))

    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        start = time.time()
        future1 = executor.submit(io_bound, '1.txt')
        future2 = executor.submit(io_bound, '2.txt')
        print(future1.result())
        print(future2.result())
        end = time.time()
        print('The number of cpu: {}'.format(os.cpu_count()))
        print('I/O bound: Thread {:.4f}\n'.format(end - start))

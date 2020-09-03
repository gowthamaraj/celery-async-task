from celery import Celery 
import time

app = Celery('task', backend= 'redis://localhost', broker= 'redis://localhost')

@app.task()
def task():
    '''
    this is async
    '''
    print('work started')
    time.sleep(5)
    f = open('file.text', 'w', encoding= 'utf-8')
    for i in range(5000):
        for j in range(i):
            f.write(str(i))
        f.write('\n')
    f.close()
    print('work completed')
    return "Task result"

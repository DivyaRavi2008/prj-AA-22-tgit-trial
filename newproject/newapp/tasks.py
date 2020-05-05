from celery import task

@task(name='add_trial')
def add_trial(x,y):
    c = x + y
    print(c)
    add_trial.retry(countdown=1 ,max_retries=1)

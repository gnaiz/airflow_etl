from random import random

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import random
dag = DAG(
    dag_id = 'first_dag',
    start_date = datetime(2024,10,26),
    schedule_interval = None #lịch chạy dag pre_set: @once, @daily, @hourly, @weekly, @monthly, @yearly
)
def plays(ti):
    sums = 0
    for i in range(3): #đổ xí ngầu 3 lần
        for j in range(2): #đổ 2 viên xí ngầu
            sums += random.randint(1,6)

    ti.xcom_push(key='what_ob', value=sums)

def result(ti):
    total = sum([val for val in ti.xcom_pull(key='what_ob', task_ids=['ob1','ob2'])])
    return total

task1 = PythonOperator(
    task_id = 'ob1',
    python_callable = plays,
    dag=dag
)


task2 = PythonOperator(
    task_id = 'ob2',
    python_callable = plays,
    dag=dag
)

ketqua = PythonOperator(
    task_id = 'result',
    python_callable = result,
    dag = dag
)

[task1, task2] >> ketqua
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow import DAG


def generate_dag():

    def do_something():
        print('something')

    default_args = {            
        'schedule_interval': '@hourly',
        'start_date': datetime(2022, 1, 1),
        'is_paused_upon_creation': True
    }

    dag = DAG("generated_dag",
              default_args=default_args,
              catchup=False
              )
    with dag:
        do_something = PythonOperator(
            task_id="do_something",
            python_callable=do_something,
            dag=dag
        )
        do_something

    return dag

def create_dag():
    dag = generate_dag()
   
    globals()['generated_dag'] = dag

create_dag()
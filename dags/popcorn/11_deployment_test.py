from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum

def print_hello():
    print("=" * 60)
    print("축하합니다! GitHub에서 자동으로 배포된 DAG가 정상 작동 중입니다.")
    print("Hello! This DAG was deployed automatically via GitHub Actions!")
    print("=" * 60)

default_args = {
    'owner': 'datapopcorn',
    'start_date': pendulum.today('UTC').add(days=-1),
}

with DAG(
    dag_id='popcorn_11_deployment_test_dag',
    default_args=default_args,
    schedule='0 0 * * *',
    catchup=False,
) as dag:

    hello_task = PythonOperator(
        task_id='print_hello_message',
        python_callable=print_hello,
    )

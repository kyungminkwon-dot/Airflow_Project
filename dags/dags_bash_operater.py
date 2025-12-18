from __future__ import annotations
from datetime import timedelta  
import pendulum

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, chain

with DAG(
    # Airflow 상에서 표기되는 이름. 가급적 파일명과 동일시하는 것을 권장.
    dag_id="dags_bash_operater",

    # 분 / 시 / 일 / 월 / 요일 = 매일 0시 0분에 실행
    schedule="0 0 * * *",

    # Dag 시작 시간. KST 기준 2021년 1월 1일. (UTC + 9)
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),

    # False일 경우, 이전 실행 내역을 처리하지 않음. True일 경우, 이전 실행 내역을 처리함. 
    # True로 실행하면 누락된 구간을 매일 돌리는게 아니라 한방에 확 돌림. 기본은 False 권장
    catchup=False,

    # Dag 실행 시간 제한. 1시간 이상 실행되면 중단.
    dagrun_timeout=timedelta(hours=1),

    # Airflow UI 상에서 Dag 이름 밑에 표기되는 태그를 의미
    tags=["test", "bashoperater"],

) as dag:

    # task group

    bash_task_1 = BashOperator(
            task_id="bash_task_1", 
            bash_command="echo bash_task_1"
        )

    bash_task_2 = BashOperator(
            task_id="bash_task_2", 
            bash_command="echo $HOSTNAME"
        )

    bash_task_1 >> bash_task_2




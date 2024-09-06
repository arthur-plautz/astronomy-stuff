from airflow import Dataset
from airflow.decorators import dag, task
from pendulum import datetime
from astroquery.esa.xmm_newton import XMMNewton
from defaults import DATALAKE

def build_query(start_dt, end_dt): 
    return f"""
        select * from
            v_public_observations
        where
            start_utc > '{start_dt}'
        and
            end_utc <= '{end_dt}'
    """

def build_dl_path(dt):
    return f'{DATALAKE}/xmm-observations/public-observations-{dt}.csv'

@dag(
    start_date=datetime(2000, 1, 1),
    schedule="@monthly",
    catchup=True,
    doc_md=__doc__,
    default_args=dict(
        retries=2
    ),
    max_active_runs=1,
    tags=["XMM"],
)
def xmm_observations():

    @task(
        outlets=[Dataset("current_observations")]
    )
    def get_observations(ds, prev_ds) -> list[dict]:
        query = build_query(prev_ds, ds)
        print("Query:", query)

        try:
            file_path = build_dl_path(ds)
            result = XMMNewton.query_xsa_tap(
                query,
                output_format='csv',
                output_file=file_path
            )

        except:
            raise Exception("Something went wrong during the request.")
        
        print(result)
        df = result.to_pandas().to_dict(orient='records')
        return df

    get_observations()

# Instantiate the DAG
xmm_observations()

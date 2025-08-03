# Exemplo de um fluxo Prefect que orquestra Airbyte e dbt. [14]
from prefect import flow, task
from prefect_airbyte.connections import trigger_sync
from prefect_dbt.cli.commands import DbtCoreOperation

@task(retries=2, retry_delay_seconds=60)
def trigger_airbyte_sync():
    """Uma tarefa para acionar uma sincronização de conexão do Airbyte."""
    # Substitua pelo seu ID de conexão do Airbyte
    connection_id = "SEU_AIRBYTE_CONNECTION_ID"
    result = trigger_sync(connection_id=connection_id)
    return result

@task
def run_dbt_transformation(wait_for_result):
    """Uma tarefa para executar transformações do dbt após a sincronização do Airbyte."""
    dbt_result = DbtCoreOperation(
        commands=["dbt build"],
        project_dir="../components/07-transformation/dbt_project/",
        profiles_dir="../components/07-transformation/dbt_project/"
    ).run()
    return dbt_result

@flow(name="ELT Pipeline Principal")
def elt_flow():
    """
    Fluxo principal que executa a ingestão do Airbyte seguida pela transformação do dbt.
    """
    airbyte_sync_result = trigger_airbyte_sync()
    dbt_transform_result = run_dbt_transformation(wait_for_result=airbyte_sync_result)

if __name__ == "__main__":
    elt_flow()
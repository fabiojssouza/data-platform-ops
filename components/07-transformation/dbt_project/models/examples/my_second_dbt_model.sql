-- models/examples/my_second_dbt_model.sql
select * from {{ ref('my_first_dbt_model') }} where id = 1
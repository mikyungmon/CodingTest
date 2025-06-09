with july_sum as (
    select FLAVOR, SUM(TOTAL_ORDER) as sum_order
    from JULY
    group by FLAVOR
),
two_table_join as (
    select js.*, fh.TOTAL_ORDER, (js.sum_order + fh.TOTAL_ORDER) as sum_two
    from july_sum js join FIRST_HALF fh on js.FLAVOR = fh.FLAVOR
    )
select FLAVOR
from two_table_join
order by sum_two desc
limit 3
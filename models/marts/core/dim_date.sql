-- Date dimension derived from all dates present in the orders data.
-- Provides calendar attributes for time-based analysis.
with date_spine as (
    select distinct order_date as date_day
    from {{ ref('stg_tpch_orders') }}
),

final as (
    select
        date_day,
        year(date_day)                                      as year_number,
        quarter(date_day)                                   as quarter_number,
        month(date_day)                                     as month_number,
        to_char(date_day, 'MMMM')                          as month_name,
        day(date_day)                                       as day_of_month,
        dayofweek(date_day)                                 as day_of_week,
        dayofyear(date_day)                                 as day_of_year,
        to_char(date_day, 'DY')                            as day_name,
        iff(dayofweek(date_day) in (0, 6), true, false)   as is_weekend,
        year(date_day) || '-Q' || quarter(date_day)        as year_quarter,
        to_char(date_day, 'YYYY-MM')                       as year_month
    from date_spine
)

select * from final

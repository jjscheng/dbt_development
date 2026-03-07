with customers as (
    select * from {{ ref('stg_tpch_customers') }}
),

nations as (
    select * from {{ ref('stg_tpch_nations') }}
),

regions as (
    select * from {{ ref('stg_tpch_regions') }}
),

final as (
    select
        c.customer_key,
        c.customer_name,
        c.customer_address,
        c.phone_number,
        c.account_balance,
        c.market_segment,
        n.nation_name,
        r.region_name
    from customers c
    left join nations n on c.nation_key = n.nation_key
    left join regions r on n.region_key = r.region_key
)

select * from final

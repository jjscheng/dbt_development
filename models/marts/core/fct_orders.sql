-- Order-level fact table. One row per order.
-- Aggregates line item financials up to the order grain.
with orders as (
    select * from {{ ref('stg_tpch_orders') }}
),

lineitems_agg as (
    select
        order_key,
        sum(extended_price)                                  as gross_item_sales_amount,
        sum(extended_price * (1 - discount_percentage))      as net_item_sales_amount,
        sum(extended_price * discount_percentage)            as item_discount_amount,
        count(*)                                             as line_item_count
    from {{ ref('stg_tpch_lineitems') }}
    group by order_key
),

final as (
    select
        o.order_key,
        o.customer_key,
        o.status_code,
        o.priority_code,
        o.clerk_name,
        o.ship_priority,
        o.order_date,
        year(o.order_date)              as order_year,
        quarter(o.order_date)           as order_quarter,
        month(o.order_date)             as order_month,
        l.line_item_count,
        l.gross_item_sales_amount,
        l.net_item_sales_amount,
        l.item_discount_amount
    from orders o
    left join lineitems_agg l on o.order_key = l.order_key
)

select * from final

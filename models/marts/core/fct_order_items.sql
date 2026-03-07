-- Line-item fact table. One row per order line item (most granular fact).
-- Joins to dim_customer, dim_supplier, dim_part, and dim_date.
with lineitems as (
    select * from {{ ref('stg_tpch_lineitems') }}
),

orders as (
    select
        order_key,
        customer_key,
        order_date,
        priority_code,
        status_code as order_status_code
    from {{ ref('stg_tpch_orders') }}
),

final as (
    select
        -- surrogate key
        md5(cast(l.order_key as varchar) || '-' || cast(l.line_number as varchar)) as order_item_key,

        -- foreign keys
        l.order_key,
        l.line_number,
        l.part_key,
        l.supplier_key,
        o.customer_key,

        -- dates
        o.order_date,
        l.ship_date,
        l.commit_date,
        l.receipt_date,

        -- order attributes
        o.priority_code,
        o.order_status_code,

        -- line item attributes
        l.ship_mode,
        l.ship_instructions,
        l.return_flag,
        l.line_status,

        -- measures
        l.quantity,
        l.extended_price                                                         as gross_item_sales_amount,
        l.discount_percentage,
        l.tax_rate,
        l.extended_price * (1 - l.discount_percentage)                          as net_item_sales_amount,
        l.extended_price * l.discount_percentage                                as item_discount_amount,
        l.extended_price * (1 - l.discount_percentage) * (1 + l.tax_rate)      as net_item_sales_amount_after_tax
    from lineitems l
    left join orders o on l.order_key = o.order_key
)

select * from final

# TPC-H DuckDB dbt Project

A dbt project that connects to a DuckDB database with the TPC-H benchmark dataset.

## Setup

### 1. Install dependencies

```bash
pip install dbt-duckdb
```

### 2. Initialize the TPC-H database

Run the setup script to create the DuckDB database with TPC-H sample data:

```bash
python scripts/setup_tpch.py
```

This creates `tpch.duckdb` with the following tables:
- `customer` - Customer information
- `lineitem` - Order line items
- `nation` - Nations reference data
- `orders` - Customer orders
- `part` - Parts catalog
- `partsupp` - Part-supplier relationships
- `region` - Geographic regions
- `supplier` - Supplier information

### 3. Run dbt

```bash
# Test the connection
dbt debug --profiles-dir .

# Run all models
dbt run --profiles-dir .

# Run tests
dbt test --profiles-dir .
```

## Project Structure

```
models/
  staging/
    _sources.yml          # Source definitions for TPC-H tables
    stg_customers.sql     # Staging model for customers
    stg_lineitems.sql     # Staging model for line items
    stg_nations.sql       # Staging model for nations
    stg_orders.sql        # Staging model for orders
    stg_parts.sql         # Staging model for parts
    stg_partsupps.sql     # Staging model for part-supplier
    stg_regions.sql       # Staging model for regions
    stg_suppliers.sql     # Staging model for suppliers
```

## TPC-H Overview

TPC-H is a decision support benchmark that consists of a suite of business-oriented ad-hoc queries and concurrent data modifications. The data model represents a wholesale supplier with parts, suppliers, customers, orders, and nations/regions.

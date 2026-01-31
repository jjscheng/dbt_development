#!/usr/bin/env python3
"""
Setup script to initialize DuckDB with TPC-H dataset.
Creates the TPC-H schema and loads sample data.
"""
import duckdb

conn = duckdb.connect('/home/user/dbt_development/tpch.duckdb')

print("Creating TPC-H schema and sample data...")

# Create the TPC-H tables with proper schema
conn.execute("""
-- Nation table
CREATE TABLE IF NOT EXISTS nation (
    n_nationkey INTEGER PRIMARY KEY,
    n_name VARCHAR(25),
    n_regionkey INTEGER,
    n_comment VARCHAR(152)
);

-- Region table
CREATE TABLE IF NOT EXISTS region (
    r_regionkey INTEGER PRIMARY KEY,
    r_name VARCHAR(25),
    r_comment VARCHAR(152)
);

-- Part table
CREATE TABLE IF NOT EXISTS part (
    p_partkey INTEGER PRIMARY KEY,
    p_name VARCHAR(55),
    p_mfgr VARCHAR(25),
    p_brand VARCHAR(10),
    p_type VARCHAR(25),
    p_size INTEGER,
    p_container VARCHAR(10),
    p_retailprice DECIMAL(15,2),
    p_comment VARCHAR(23)
);

-- Supplier table
CREATE TABLE IF NOT EXISTS supplier (
    s_suppkey INTEGER PRIMARY KEY,
    s_name VARCHAR(25),
    s_address VARCHAR(40),
    s_nationkey INTEGER,
    s_phone VARCHAR(15),
    s_acctbal DECIMAL(15,2),
    s_comment VARCHAR(101)
);

-- Partsupp table
CREATE TABLE IF NOT EXISTS partsupp (
    ps_partkey INTEGER,
    ps_suppkey INTEGER,
    ps_availqty INTEGER,
    ps_supplycost DECIMAL(15,2),
    ps_comment VARCHAR(199),
    PRIMARY KEY (ps_partkey, ps_suppkey)
);

-- Customer table
CREATE TABLE IF NOT EXISTS customer (
    c_custkey INTEGER PRIMARY KEY,
    c_name VARCHAR(25),
    c_address VARCHAR(40),
    c_nationkey INTEGER,
    c_phone VARCHAR(15),
    c_acctbal DECIMAL(15,2),
    c_mktsegment VARCHAR(10),
    c_comment VARCHAR(117)
);

-- Orders table
CREATE TABLE IF NOT EXISTS orders (
    o_orderkey INTEGER PRIMARY KEY,
    o_custkey INTEGER,
    o_orderstatus VARCHAR(1),
    o_totalprice DECIMAL(15,2),
    o_orderdate DATE,
    o_orderpriority VARCHAR(15),
    o_clerk VARCHAR(15),
    o_shippriority INTEGER,
    o_comment VARCHAR(79)
);

-- Lineitem table
CREATE TABLE IF NOT EXISTS lineitem (
    l_orderkey INTEGER,
    l_partkey INTEGER,
    l_suppkey INTEGER,
    l_linenumber INTEGER,
    l_quantity DECIMAL(15,2),
    l_extendedprice DECIMAL(15,2),
    l_discount DECIMAL(15,2),
    l_tax DECIMAL(15,2),
    l_returnflag VARCHAR(1),
    l_linestatus VARCHAR(1),
    l_shipdate DATE,
    l_commitdate DATE,
    l_receiptdate DATE,
    l_shipinstruct VARCHAR(25),
    l_shipmode VARCHAR(10),
    l_comment VARCHAR(44),
    PRIMARY KEY (l_orderkey, l_linenumber)
);
""")

# Insert sample data - Regions
conn.execute("""
INSERT INTO region VALUES
    (0, 'AFRICA', 'Special requests from customers in Africa'),
    (1, 'AMERICA', 'Special requests from customers in Americas'),
    (2, 'ASIA', 'Special requests from customers in Asia'),
    (3, 'EUROPE', 'Special requests from customers in Europe'),
    (4, 'MIDDLE EAST', 'Special requests from Middle Eastern customers');
""")

# Insert sample data - Nations
conn.execute("""
INSERT INTO nation VALUES
    (0, 'ALGERIA', 0, 'furiously regular accounts'),
    (1, 'ARGENTINA', 1, 'furiously regular pinto beans'),
    (2, 'BRAZIL', 1, 'unusual theodolites'),
    (3, 'CANADA', 1, 'final accounts sleep slyly'),
    (4, 'EGYPT', 4, 'regular requests detect'),
    (5, 'ETHIOPIA', 0, 'even accounts are furiously'),
    (6, 'FRANCE', 3, 'regular deposits boost'),
    (7, 'GERMANY', 3, 'final courts wake silently'),
    (8, 'INDIA', 2, 'special packages haggle'),
    (9, 'INDONESIA', 2, 'carefully regular deposits'),
    (10, 'IRAN', 4, 'ironic requests boost slyly'),
    (11, 'IRAQ', 4, 'final pinto beans sleep'),
    (12, 'JAPAN', 2, 'regular foxes sleep'),
    (13, 'JORDAN', 4, 'final pinto beans'),
    (14, 'KENYA', 0, 'pending pinto beans'),
    (15, 'MOROCCO', 0, 'final excuses detect'),
    (16, 'MOZAMBIQUE', 0, 'furiously silent pinto'),
    (17, 'PERU', 1, 'regular deposits wake'),
    (18, 'CHINA', 2, 'express requests after'),
    (19, 'ROMANIA', 3, 'regular requests alongside'),
    (20, 'SAUDI ARABIA', 4, 'regular pinto beans'),
    (21, 'VIETNAM', 2, 'regular requests boost'),
    (22, 'RUSSIA', 3, 'furiously regular accounts'),
    (23, 'UNITED KINGDOM', 3, 'special accounts cajole'),
    (24, 'UNITED STATES', 1, 'furiously unusual ideas');
""")

# Insert sample data - Parts
conn.execute("""
INSERT INTO part VALUES
    (1, 'goldenrod lavender spring chocolate lace', 'Manufacturer#1', 'Brand#13', 'PROMO BRUSHED STEEL', 7, 'JUMBO PKG', 901.00, 'ly final depend'),
    (2, 'blush thistle blue yellow saddle', 'Manufacturer#1', 'Brand#13', 'LARGE BRUSHED BRASS', 1, 'LG CASE', 902.00, 'lar accounts'),
    (3, 'spring green yellow purple cornsilk', 'Manufacturer#4', 'Brand#42', 'STANDARD POLISHED BRASS', 21, 'WRAP CASE', 903.00, 'egular deposits'),
    (4, 'cornflower chocolate smoke green pink', 'Manufacturer#3', 'Brand#34', 'SMALL PLATED BRASS', 14, 'MED DRUM', 904.00, 'p]ironic, final'),
    (5, 'forest brown coral puff cream', 'Manufacturer#3', 'Brand#32', 'STANDARD POLISHED TIN', 15, 'SM PKG', 905.00, 'wake carefully'),
    (6, 'bisque cornflower lawn forest magenta', 'Manufacturer#2', 'Brand#24', 'PROMO PLATED STEEL', 4, 'MED BAG', 906.00, 'even requests'),
    (7, 'moccasin green thistle khaki floral', 'Manufacturer#1', 'Brand#11', 'SMALL PLATED COPPER', 45, 'SM BAG', 907.00, 'carefully ironic'),
    (8, 'misty lace thistle blanched hot', 'Manufacturer#4', 'Brand#44', 'PROMO BURNISHED TIN', 41, 'LG DRUM', 908.00, 'regular accounts'),
    (9, 'thistle dim navajo dark gainsboro', 'Manufacturer#4', 'Brand#43', 'SMALL BURNISHED STEEL', 12, 'WRAP CASE', 909.00, 'careful requests'),
    (10, 'linen pink saddle puff powder', 'Manufacturer#5', 'Brand#54', 'LARGE BURNISHED STEEL', 44, 'LG CAN', 910.00, 'furiously even');
""")

# Insert sample data - Suppliers
conn.execute("""
INSERT INTO supplier VALUES
    (1, 'Supplier#000000001', 'N kD4on9OM Ipw3', 17, '27-918-335-1736', 5755.94, 'each slyly above the careful'),
    (2, 'Supplier#000000002', '89eJ5ksX3Imx', 5, '15-679-861-2259', 4032.68, 'carefully final courts'),
    (3, 'Supplier#000000003', 'q1,G3Pj6OjIuUYfUoH', 1, '11-383-516-1199', 4192.40, 'blithely silent requests'),
    (4, 'Supplier#000000004', 'Bk7ah4CK8SYQTe', 15, '25-843-787-7479', 4641.08, 'recklessly regular ideas'),
    (5, 'Supplier#000000005', 'Gcdm2rJRzl5eLuxX', 11, '21-151-690-3663', -531.44, 'slyly bold instructions');
""")

# Insert sample data - Customers
conn.execute("""
INSERT INTO customer VALUES
    (1, 'Customer#000000001', 'IVhzIApeRb ot,c,E', 15, '25-989-741-2988', 711.56, 'BUILDING', 'regular deposits'),
    (2, 'Customer#000000002', 'XSTf4,NCwDVaWNe6tE', 13, '23-768-687-3665', 121.65, 'AUTOMOBILE', 'furiously regular accounts'),
    (3, 'Customer#000000003', 'MG9kdTD2WBHm', 1, '11-719-748-3364', 7498.12, 'AUTOMOBILE', 'special packages'),
    (4, 'Customer#000000004', 'XxVSJsLAGtn', 4, '14-128-190-5944', 2866.83, 'MACHINERY', 'slyly final requests'),
    (5, 'Customer#000000005', 'KvpyuHCplrB84WgAi', 3, '13-750-942-6364', 794.47, 'HOUSEHOLD', 'final accounts'),
    (6, 'Customer#000000006', 'sKZz0CsnMD7mp4X', 20, '30-114-968-4951', 7638.57, 'AUTOMOBILE', 'regular excuses'),
    (7, 'Customer#000000007', 'TcGe5gaZNgVePxU', 18, '28-190-982-9759', 9561.95, 'AUTOMOBILE', 'pending requests'),
    (8, 'Customer#000000008', 'I0B10bB0AymmC', 17, '27-147-574-9335', 6819.74, 'BUILDING', 'regular requests'),
    (9, 'Customer#000000009', 'xKiAFTjUsCux', 8, '18-338-906-3675', 8324.07, 'FURNITURE', 'ironic deposits'),
    (10, 'Customer#000000010', '6LrEaV6KR6PLVcG', 5, '15-741-346-9870', 2753.54, 'HOUSEHOLD', 'slyly regular');
""")

# Insert sample data - Partsupp
conn.execute("""
INSERT INTO partsupp VALUES
    (1, 1, 3325, 771.64, 'requests after the carefully'),
    (1, 2, 8076, 993.49, 'accounts are alongside'),
    (2, 1, 3956, 337.09, 'dependencies. furiously'),
    (2, 2, 4069, 357.84, 'after the furiously final'),
    (3, 3, 4651, 920.92, 'foxes wake slyly'),
    (3, 4, 3538, 788.99, 'pending requests sleep'),
    (4, 3, 1339, 113.97, 'regular excuses boost'),
    (4, 4, 6377, 591.18, 'blithely bold accounts'),
    (5, 5, 4018, 530.82, 'pending accounts are'),
    (6, 1, 3336, 642.13, 'across the express');
""")

# Insert sample data - Orders
conn.execute("""
INSERT INTO orders VALUES
    (1, 1, 'O', 173665.47, '1996-01-02', '5-LOW', 'Clerk#000000951', 0, 'nstructions sleep'),
    (2, 2, 'O', 46929.18, '1996-12-01', '1-URGENT', 'Clerk#000000880', 0, 'foxes. pending accounts'),
    (3, 3, 'F', 193846.25, '1993-10-14', '5-LOW', 'Clerk#000000955', 0, 'sly final accounts'),
    (4, 4, 'O', 32151.78, '1995-10-11', '5-LOW', 'Clerk#000000124', 0, 'sits. slyly regular'),
    (5, 5, 'F', 144659.20, '1994-07-30', '5-LOW', 'Clerk#000000925', 0, 'quickly. bold deposits'),
    (6, 6, 'F', 58749.59, '1992-02-21', '4-NOT SPECIFIED', 'Clerk#000000058', 0, 'ggle. special, final'),
    (7, 7, 'O', 252004.18, '1996-01-10', '2-HIGH', 'Clerk#000000470', 0, 'ly special requests'),
    (32, 8, 'O', 208660.75, '1995-07-16', '2-HIGH', 'Clerk#000000616', 0, 'ise blithely bold'),
    (33, 9, 'F', 163243.98, '1993-10-27', '3-MEDIUM', 'Clerk#000000409', 0, 'uriously. furiously'),
    (34, 10, 'O', 58949.67, '1998-07-21', '3-MEDIUM', 'Clerk#000000223', 0, 'ly final packages');
""")

# Insert sample data - Lineitem
conn.execute("""
INSERT INTO lineitem VALUES
    (1, 1, 1, 1, 17, 21168.23, 0.04, 0.02, 'N', 'O', '1996-03-13', '1996-02-12', '1996-03-22', 'DELIVER IN PERSON', 'TRUCK', 'egular courts above'),
    (1, 2, 2, 2, 36, 45983.16, 0.09, 0.06, 'N', 'O', '1996-04-12', '1996-02-28', '1996-04-20', 'TAKE BACK RETURN', 'MAIL', 'ly final dependencies'),
    (1, 3, 3, 3, 8, 13309.60, 0.10, 0.02, 'N', 'O', '1996-01-29', '1996-03-05', '1996-01-31', 'TAKE BACK RETURN', 'REG AIR', 'riously. regular,'),
    (2, 4, 3, 1, 38, 44694.36, 0.00, 0.05, 'N', 'O', '1997-01-28', '1997-01-14', '1997-02-02', 'TAKE BACK RETURN', 'RAIL', 'ven requests. deposits'),
    (3, 5, 5, 1, 45, 54058.05, 0.06, 0.00, 'R', 'F', '1994-02-02', '1994-01-04', '1994-02-23', 'NONE', 'AIR', 'ongside of the fur'),
    (3, 6, 1, 2, 49, 43567.06, 0.10, 0.00, 'R', 'F', '1993-11-09', '1993-12-20', '1993-11-24', 'TAKE BACK RETURN', 'RAIL', 'unusual accounts'),
    (4, 7, 1, 1, 30, 27180.00, 0.03, 0.08, 'N', 'O', '1996-01-10', '1995-12-14', '1996-01-18', 'DELIVER IN PERSON', 'REG AIR', 'carefully silent'),
    (5, 8, 4, 1, 15, 13620.00, 0.02, 0.04, 'R', 'F', '1994-10-31', '1994-08-31', '1994-11-20', 'NONE', 'AIR', 'ironic, final accounts'),
    (5, 9, 4, 2, 26, 23634.00, 0.07, 0.08, 'R', 'F', '1994-08-08', '1994-10-13', '1994-08-26', 'DELIVER IN PERSON', 'AIR', 'pending foxes wake'),
    (6, 10, 5, 1, 37, 33670.00, 0.08, 0.03, 'A', 'F', '1992-04-27', '1992-05-15', '1992-05-02', 'TAKE BACK RETURN', 'TRUCK', 'p]ironic foxes');
""")

# Verify the tables were created
tables = conn.execute("SHOW TABLES").fetchall()
print(f"\nCreated {len(tables)} TPC-H tables:")
for table in tables:
    count = conn.execute(f"SELECT COUNT(*) FROM {table[0]}").fetchone()[0]
    print(f"  - {table[0]}: {count:,} rows")

conn.close()
print("\nTPC-H database setup complete!")

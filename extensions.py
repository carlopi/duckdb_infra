import duckdb
import random
import time

print(duckdb.__version__)

extension_list = ['aws', 'icu', 'fts', 'spatial', 'httpfs', 'tpch', 'tpcds', 'arrow', 'azure', 'excel', 'iceberg', 'inet', 'mysql', 'postgres', 'sqlite', 'sqlsmith', 'vss']

to_be_tested = random.sample(extension_list, 5)

print('extension_name', 'install_time', 'load_time')
for ext in to_be_tested:
    a = time.perf_counter()
    duckdb.install_extension(ext)
    b = time.perf_counter()
    duckdb.load_extension(ext)
    c = time.perf_counter()
    print(ext, b-a, c-b)

for ext in to_be_tested:
    a = time.perf_counter()
    duckdb.install_extension(ext)
    b = time.perf_counter()
    duckdb.load_extension(ext)
    c = time.perf_counter()
    print(ext, b-a, c-b)

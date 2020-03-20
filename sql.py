def bulk_insert_table(df, command, engine, name, schema):
    connection = engine.raw_connection()
    cursor = connection.cursor()
    if f'{schema}.' in name:
        name = name.replace(f'{schema}.', '')
    # df.rename(columns={'index': 'Index'}, inplace=True)
    # create the table but first drop if it already exists
    cursor.execute(command)
    connection.commit()
    # stream the data using 'to_csv' and StringIO(); then use sql's 'copy_from' function
    output = io.StringIO()
    # ignore the index
    df.to_csv(output, sep='\t', header=False, index=False)
    # jump to start of stream
    output.seek(0)
    cur = connection.cursor()
    # null values become ''
    # print(output)
    cur.copy_from(output, f'{schema}.{name}', null="")
    connection.commit()
    cur.close()
    output.close()
def push_transactions_table(df, name, engine, schema):
    if f'{schema}' in name:
        name = name.replace(f'{schema}.', '')
    # create the table but first drop if it already exists
    command = f'''DROP TABLE IF EXISTS {schema}.{name};
        CREATE TABLE {schema}.{name}
        (
        "index" int,
        "date" timestamp,
        "transaction_id" int,
        "store_id" int, 
        "product" text,
        "quantity" float,
        "price_paid" float,
        "customer_id" int,
        "staff_id" int, 
        "comment" text, 
        "year" int
             );'''
    bulk_insert_table(df, command, engine, name, schema)
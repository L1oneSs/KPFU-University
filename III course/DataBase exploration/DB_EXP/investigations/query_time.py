import timeit
from investigations.graphics import graph_generate_info, graph_info
from lib.creator import create_table_entry

def query_time_generate(table_name, num_entries, mycursor, connection):
    count_query = f"SELECT COUNT(*) FROM {table_name}"
    mycursor.execute(count_query)
    row_count = mycursor.fetchone()[0]

    start_time = timeit.default_timer()
    create_table_entry(table_name, num_entries, mycursor)
    connection.commit()
    end_time = timeit.default_timer()

    time_query = end_time - start_time

    data = ["GENERATE", num_entries, time_query]
    graph_generate_info.append(data)
    return time_query

def query_time_custom(mycursor, connection, custom_query, first_word, row_count):
    start_time = timeit.default_timer()
    mycursor.execute(custom_query)
    _ = mycursor.fetchall()
    connection.commit()
    end_time = timeit.default_timer()
    time_query = end_time - start_time
    data = [first_word, row_count, time_query]
    graph_info.append(data)
    return time_query

def query_time_select(mycursor, connection, query, row_count):
    start_time = timeit.default_timer()
    mycursor.execute(query)
    _ = mycursor.fetchall()
    connection.commit()
    end_time = timeit.default_timer()
    time_query = end_time - start_time
    data = ["SELECT", row_count, time_query]
    graph_info.append(data)
    return time_query

def query_time_insert(mycursor, connection, query, values, row_count):
    start_time = timeit.default_timer()
    mycursor.execute(query, values)
    _ = mycursor.fetchall()
    connection.commit()
    end_time = timeit.default_timer()
    time_query = end_time - start_time
    data = ["INSERT", row_count, time_query]
    graph_info.append(data)
    return time_query

def query_time_delete(mycursor, connection, query, row_count):
    start_time = timeit.default_timer()
    mycursor.execute(query)
    connection.commit()
    end_time = timeit.default_timer()
    time_query = end_time - start_time
    data = ["DELETE", row_count, time_query]
    graph_info.append(data)
    return time_query
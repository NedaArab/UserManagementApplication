import functools
import time
from datetime import datetime
import sqlite3

def performance_logger_decorator(main_function):
    @functools.wraps(main_function)
    def wrapper(*args, **kwargs):
        function_name=main_function.__name__
        call_date=datetime.now()
        start_time=time.time()
        result=main_function(*args,**kwargs)
        stop_time=time.time()

        execution_time=stop_time-start_time

        with sqlite3.connect("user_management_app2.db") as connection:
            cursor=connection.cursor()
            cursor.execute(f"""
            INSERT INTO PerformanceLoger (
                                 function_name,
                                 execution_time,
                                 call_date
                             )
            VALUES (
                                 '{function_name}',
                                 {execution_time},
                                 '{call_date}'
                             );

            """)
            connection.commit()



        return result
    return wrapper



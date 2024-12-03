# Movie-Theater-DataBase-Project

PREREQS
- Python > 3.12
- SQLite3
- Pandas
   - If on Windows, open terminal > pip install pandas
- Make sure you have MovieDataBase.xlsx in your project.

RUN FOLLOWING SCRIPTS IN ORDER

1. RUN the script > python setup_database.py
   - This will create the database schema. After running this script, you should see that movie_theater.db has been created in your solution explorer.
2. RUN the script > python generate_data.py
   - This will populate the database with data. You should see data inserted for each table.
3. RUN the script > sqlite3 movie_theater.db
   - This is where we want you guys to test the five queries we have made. You will see a "sqlite>" prompt. Follow with typing in queries.
4. RUN the script > python cli.py
   - This is where the interaction hub is at. I made options to add a movie, remove a customer, update a movie rating, add an employee, and update any movie start time. You can exit this at any time too.


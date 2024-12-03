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
   - This is where we want you guys to test the five queries we have made(check for queries below). You will see a "sqlite>" prompt. Follow with typing in queries.
4. RUN the script > python cli.py
   - This is where the interaction hub is at. I made options to add a movie, remove a customer, update a movie rating, add an employee, and update any movie start time. You can exit this at any time too.
  
QUERIES TO TEST!
1. List all movies and their genre
   SELECT Movies.title, Genre.genre_name
        FROM Movies
        JOIN Genre ON Movies.genre_ID = Genre.genre_ID
2. List all customers with a Premium Membership
   SELECT Customer.name, Membership.membership_name
        FROM Customer
        JOIN Membership ON Customer.membership_ID = Membership.membership_ID
        WHERE Membership.membership_name = 'Premium'
3. List all employees earning above $15.00
   SELECT Employee.name, Employee.position, Employee.wage
        FROM Employee
        WHERE Employee.wage > 15.00
4. Get all theaters and the number of seats in each theater
   SELECT Theater.room, COUNT(Seat.seat_number) AS total_seats
    FROM Theater
    LEFT JOIN Seat ON Theater.theater_ID = Seat.theater_ID
    GROUP BY Theater.room
5. List all the movies being shown on a Friday
   SELECT Movies.title, MovieTime.day
        FROM Movies
        JOIN MovieTime ON Movies.movies_ID = MovieTime.movie_ID
        WHERE MovieTime.day = 'Friday'



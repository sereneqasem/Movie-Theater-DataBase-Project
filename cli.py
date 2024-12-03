import sqlite3

def add_movie():
    conn = sqlite3.connect('movie_theater.db')
    cursor = conn.cursor()
    try:
        title = input("Enter movie title: ")
        genre_id = input("Enter genre ID: ")
        rating = input("Enter movie rating (e.g., PG, PG-13): ")
        cursor.execute(
            "INSERT INTO Movies (title, genre_ID, rating) VALUES (?, ?, ?)",
            (title, genre_id, rating)
        )
        conn.commit()
        print("Movie added successfully!")
    except sqlite3.Error as e:
        print(f"Error adding movie: {e}")
    finally:
        conn.close()

def remove_customer():
    conn = sqlite3.connect('movie_theater.db')
    cursor = conn.cursor()
    try:
        customer_id = input("Enter the customer ID to remove: ")
        cursor.execute("DELETE FROM Customer WHERE customer_ID = ?", (customer_id,))
        conn.commit()
        print("Customer removed successfully!")
    except sqlite3.Error as e:
        print(f"Error removing customer: {e}")
    finally:
        conn.close()

def update_movie_rating():
    conn = sqlite3.connect('movie_theater.db')
    cursor = conn.cursor()
    try:
        movie_id = input("Enter the movie ID to update: ")
        new_rating = input("Enter the new movie rating: ")
        cursor.execute(
            "UPDATE Movies SET rating = ? WHERE movies_ID = ?", (new_rating, movie_id)
        )
        conn.commit()
        print("Movie rating updated successfully!")
    except sqlite3.Error as e:
        print(f"Error updating movie rating: {e}")
    finally:
        conn.close()

def add_employee():
    conn = sqlite3.connect('movie_theater.db')
    cursor = conn.cursor()
    try:
        name = input("Enter employee name: ")
        position = input("Enter employee position: ")
        wage = input("Enter employee wage: ")
        cursor.execute(
            "INSERT INTO Employee (name, position, wage) VALUES (?, ?, ?)",
            (name, position, wage)
        )
        conn.commit()
        print("Employee added successfully!")
    except sqlite3.Error as e:
        print(f"Error adding employee: {e}")
    finally:
        conn.close()

def update_movie_start_time():
    conn = sqlite3.connect('movie_theater.db')
    cursor = conn.cursor()
    try:
        movie_id = input("Enter the movie ID to update start time: ")
        new_start_time = input("Enter the new start time: ")
        cursor.execute(
            "UPDATE MovieTime SET start_time = ? WHERE movie_ID = ?",
            (new_start_time, movie_id)
        )
        conn.commit()
        print("Movie start time updated!")
    except sqlite3.Error as e:
        print(f"Error updating start time: {e}")
    finally:
        conn.close()

def main_menu():
    while True:
        print("\nWelcome to the Interaction Hub!")
        print("1. Add Movie")
        print("2. Remove Customer")
        print("3. Update Movie Rating")
        print("4. Add Employee")
        print("5. Update Movie Start Time")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_movie()
        elif choice == "2":
            remove_customer()
        elif choice == "3":
            update_movie_rating()
        elif choice == "4":
            add_employee()
        elif choice == "5":
            update_movie_start_time()
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Pick a number!")

if __name__ == "__main__":
    main_menu()


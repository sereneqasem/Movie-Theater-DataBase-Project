import sqlite3
import pandas as pd

def clear_existing_data(cursor):
    try:
        tables = ['Customer', 'Movies', 'Theater', 'Membership']
        
        for table in tables:
            cursor.execute(f"DELETE FROM {table}")
        print("Existing data cleared.")
    except sqlite3.Error as e:
        print(f"Error while clearing data: {e}")

def table_exists(cursor, table_name):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    tables_in_db = [t[0] for t in tables]  
    return table_name in tables_in_db

def insert_data_from_excel(db_connection, excel_file):
    try:
        xl = pd.ExcelFile(excel_file)
        
        print(f"Sheet names in the Excel file: {xl.sheet_names}")
        
        for sheet_name in xl.sheet_names:
            df = xl.parse(sheet_name, header=0)  
            
            cursor = db_connection.cursor()
            if not table_exists(cursor, sheet_name):
                print(f"Table {sheet_name} does not exist in the database. Skipping data insertion for this sheet.")
                continue  
            
            for _, row in df.iterrows():
                columns = ', '.join([f'"{col}"' for col in df.columns])  
                placeholders = ', '.join(['?'] * len(df.columns))  
                values = tuple(row)  
                
                query = f'INSERT INTO "{sheet_name}" ({columns}) VALUES ({placeholders})'
                try:
                    cursor.execute(query, values)
                except sqlite3.IntegrityError as e:
                    if 'UNIQUE constraint failed' in str(e):
                        print(f"Skipping row due to UNIQUE constraint violation: {row.to_dict()}")
                    else:
                        print(f"Error inserting row {row.to_dict()}: {e}")
            
            print(f"Data inserted for table: {sheet_name}")
        
        db_connection.commit()
    except Exception as e:
        print(f"Error inserting data: {e}")


def populate_database(excel_file, db_file):
    try:
        db_connection = sqlite3.connect(db_file)
        cursor = db_connection.cursor()
        
        clear_existing_data(cursor)
        
        insert_data_from_excel(db_connection, excel_file)
        
        db_connection.close()
        print("Database connection closed.")
    
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    excel_file = 'MovieDataBase.xlsx'  #path to your Excel file. make sure on the names it is similar!!!!!!!!!!
    db_file = 'movie_theater.db'         
    
    populate_database(excel_file, db_file)

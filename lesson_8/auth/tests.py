from config import DATABASE_URL


def run_tests():
    db_connection = Database(DATABASE_URL)


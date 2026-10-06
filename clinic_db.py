import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="clinic_db",
            autocommit=False
        )
        return conn
    except mysql.connector.Error as e:
        print("DB Connection Error:", e)
        raise

def save_form_data(data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.callproc('sp_add_medical_form', (
            data['email'],
            data['sr_code'],
            data['control_no'],
            data['purpose'],
            data['last_name'],
            data['first_name'],
            data['middle_name'],
            data['age'],
            data['sex'],
            data['civil_status'],
            data['address'],
            data['height_cm'],
            data['weight_kg']
        ))

        conn.commit()

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        cursor.close()
        conn.close()
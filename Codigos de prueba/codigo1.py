import sqlite3

def get_user_data(user_id):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    
    # 🚨 SQL Injection: No sanitiza la entrada del usuario
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    
    result = cursor.fetchall()
    connection.close()
    return result

def unsafe_execution():
    user_input = input("Ingresa el código a ejecutar: ")
    # 🚨 Eval es un problema de seguridad
    eval(user_input)  

print(get_user_data("1 OR 1=1"))  # 🚨 Ejecutará una inyección SQL

unused_variable = "Este valor nunca se usa"

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
import Login as main
import psycopg2 as psy



if __name__ == "__main__":
    import sys 
    try:
        connection=psy.connect(
            host='localhost',
            user='postgres',
            password='1234',
            port='5432',
            database='easyfit'
        )
        print("Conexion Exitosa")
        cursor=connection.cursor()
    
        app = QtWidgets.QApplication(sys.argv)
        Login = QtWidgets.QMainWindow()
        ui = main.Ui_LogIn()
        ui.setupUi(Login,cursor)
        Login.show()
        sys.exit(app.exec_())
    except Exception as ex:
        print(ex)
    finally:
        connection.close()  # Se cerró la conexión a la BD.
        print("La conexión ha finalizado.")
    
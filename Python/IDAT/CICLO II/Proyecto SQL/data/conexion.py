from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel


server_name="DESKTOP-JDTQKVK"
database="OASIS"

def Conexion():
    connString =f'DRIVER={{SQL SERVER}};'\
                f'SERVER={server_name};'\
                f'DATABASE={database}'
    global db
    if QSqlDatabase.contains("qt_sql_default_connection"):
        db=QSqlDatabase.database("qt_sql_default_connection")
    else:
        db=QSqlDatabase.addDatabase('QODBC')
        db.setDatabaseName(connString)
        if db.open():
            print("Conexion correcta")
            return True
        else:
            print("Conexion incorrecta")
            return False

def mostrarDatos(sql):
    Conexion()
    qry = QSqlQuery(sql)
    return qry

def Query(sql, args):
    Conexion()
    qry=QSqlQuery(db)
    qry.prepare(sql)
    for arg in args:
        qry.addBindValue(arg)
    return qry.exec()



    # def insertar_datos(self, codigo, nombre, telefono, fecha):
    #   cur = self.db
    #    sql = '''INSERT INTO TBL_PERSONAL (COD_PERSONAL, NOMBRE, TELEFONO, FECHA)
    #    VALUES('{}','{}','{}','{}')'''.format(codigo, nombre, telefono, fecha)
    #   cur.execute(sql)
    #    self.Conexion()
    #    cur.close()
    
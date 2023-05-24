# este módulo será usado para posibles configuraciones
#
# cadena conector a la base de datos
#
# Sqlite
#cadena_base_datos = 'sqlite:///baseclase07.db' 
cadena_base_datos = "postgresql+psycopg2://invitado:UTPLUTPL@localhost:5432/baseclase07"
#engine = create_engine("postgresql+psycopg2://invitado:UTPLUTPL@localhost:5432/demo100", echo=True)
# Mysql
# para el uso de este dialecto en SqlAlchemy
# instalar "pip install PyMySQL"
# cadena_base_datos = 'mysql+pymysql://usuario:clave@localhost/bd_name'

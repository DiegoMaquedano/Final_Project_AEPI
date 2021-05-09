from peewee import *

db = SqliteDatabase('ProyectoFinal.db')

class Fabricantes(Model):
    Nombre_Fabricante = CharField(unique=True)
    Numero_Registro_Fabricante = CharField(unique=True)
    Localizacion_Fabricante=CharField()
    CIF_Fabricante = CharField(unique=True)

    class Meta:
        database = db

class Piezas(Model):

    Nombre_Pieza = CharField()
    Numero_Registro_Pieza = CharField(unique=True)
    Fecha_Fabri_Pieza=DateTimeField()
    Fabri_Pieza=ForeignKeyField(Fabricantes,
                               on_delete="CASCADE",
                               backref="fabricantes")
    Localidad_Fabri_Pieza=CharField()
    Precio_Pieza=FloatField()
    Piezas_Vendidas=IntegerField(default=0)

    class Meta:
        database = db

class Ordenes(Model):

    ID_Compra_Orden= CharField(unique=True)
    Fecha_Compra_Orden = DateTimeField()
    Vendedor_Orden=CharField()
    Piezas_Compra_Orden=CharField()
    Precio_Orden=FloatField()

    class Meta:
        database = db

db.connect()
db.create_tables([Fabricantes,Piezas,Ordenes])
db.close()

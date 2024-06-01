import graphene
from graphene import Mutation

from .models import *




# class NuevaCategoria(Mutation):
#     class Arguments:
#         nombre = graphene.String(required=True) 

#     success = graphene.Boolean()
#     errors = graphene.String()

#     def mutate(self, info, nombre):
#         try:
#             Categoria.objects.create(nombre=nombre)
#             return NuevaCategoria(success=True, errors=None)
#         except Exception as e:
#             return NuevaCategoria(success=False, errors=str(e))


# class ActualizarCategoria(Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#         nombre = graphene.String(required=True)
        

#     success = graphene.Boolean()
#     errors = graphene.String()

#     def mutate(self, info, nombre, id):
#         try:
#             categ = Categoria.objects.get(id=id)
#             categ.nombre = nombre
#             categ.save()
#             return ActualizarCategoria(success=True, errors=None)
#         except Exception as e:
#             return ActualizarCategoria(success=False, errors=str(e))


# class EliminarCategoria(Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)

#     success = graphene.Boolean()
#     errors = graphene.String()

#     def mutate(self, info, id):
#         try:
#             categ = Categoria.objects.get(id=id)
#             categ.delete()
#             return EliminarCategoria(success=True, errors=None)
#         except Exception as e:
#             return EliminarCategoria(success=False, errors=str(e))




# class NuevoCodifResultado(Mutation):
#     class Arguments:
#         resultado = graphene.String(required=True)
#         descripcion = graphene.String(required=True)

#     success = graphene.Boolean()
#     errors = graphene.String()

#     def mutate(self, info, resultado, descripcion):
#         try:
#             CodifResultado.objects.create(resul=resultado, descripcion=descripcion)
#             return NuevoCodifResultado(success=True, errors=None)
#         except Exception as e:
#             return NuevoCodifResultado(success=False, errors=str(e))


# class ActualizarCodifResultado(Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#         resultado = graphene.String(required=True)
#         descripcion = graphene.String(required=True)

#     success = graphene.Boolean()
#     errors = graphene.String()

#     def mutate(self, info, resultado, id, descripcion):
#         try:
#             item = CodifResultado.objects.get(id=id)
#             item.resul = resultado
#             item.descripcion = descripcion
#             item.save()
#             return ActualizarCodifResultado(success=True, errors=None)
#         except Exception as e:
#             return ActualizarCodifResultado(success=False, errors=str(e))


# class EliminarCodifResultado(Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)

#     success = graphene.Boolean()
#     errors = graphene.String()

#     def mutate(self, info, id):
#         try:
#             item = CodifResultado.objects.get(id=id)
#             item.delete()
#             return EliminarCodifResultado(success=True, errors=None)
#         except Exception as e:
#             return EliminarCodifResultado(success=False, errors=str(e))


# class NuevoTipoEvento(Mutation):
#     class Arguments:
#         nombre = graphene.String(required=True)

#     success = graphene.Boolean()
#     errors = graphene.String()

#     def mutate(self, info, nombre):
#         try:
#             TipoEvento.objects.create(tipo=nombre)
#             return NuevoTipoEvento(success=True, errors=None)
#         except Exception as e:
#             return NuevoTipoEvento(success=False, errors=str(e))


# class ActualizarTipoEvento(Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#         nombre = graphene.String(required=True)

#     success = graphene.Boolean()
#     errors = graphene.String()

#     def mutate(self, info, nombre, id):
#         try:
#             item = TipoEvento.objects.get(id=id)
#             item.tipo = nombre
#             item.save()
#             return ActualizarTipoEvento(success=True, errors=None)
#         except Exception as e:
#             return ActualizarTipoEvento(success=False, errors=str(e))


# class EliminarTipoEvento(Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)

#     success = graphene.Boolean()
#     errors = graphene.String()

#     def mutate(self, info, id):
#         try:
#             item = TipoEvento.objects.get(id=id)
#             item.delete()
#             return EliminarTipoEvento(success=True, errors=None)
#         except Exception as e:
#             return EliminarTipoEvento(success=False, errors=str(e))


# class NuevoReglamento(Mutation):
#     class Arguments:
#         tipo = graphene.String(required=True)
#         cant_r = graphene.Int(required=True)
#         duracion = graphene.Int(required=True)

#     success = graphene.Boolean()
#     errors = graphene.String()

#     def mutate(self, info, tipo, cant_r, duracion):
#         try:
#             Reglamento.objects.create(tipo=tipo, cant_r=cant_r, duracion=duracion)
#             return NuevoReglamento(success=True, errors=None)
#         except Exception as e:
#             return NuevoReglamento(success=False, errors=str(e))

        
class Mutation(graphene.ObjectType):
    nuevaCategoria = NuevaCategoria.Field()
    actualizarCategoria = ActualizarCategoria.Field()
    eliminarCategoria = EliminarCategoria.Field()

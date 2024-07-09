import graphene
from graphene import Mutation

from .models import *




class NuevoPais(Mutation):
    class Arguments:
        nombre = graphene.String(required=True) 

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre):
        try:
            Pais.objects.create(nombre=nombre)
            return NuevoPais(success=True, errors=None)
        except Exception as e:
            return NuevoPais(success=False, errors=str(e))




        
class Mutation(graphene.ObjectType):
    nuevoPais = NuevoPais.Field()
    

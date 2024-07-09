import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from .models import *


class PaisType(DjangoObjectType):
    class Meta:
        model = Pais
        fields = '__all__'
              
      
class IDArray(graphene.InputObjectType):
    ids = graphene.List(graphene.ID, required=True)
    
      
class Query(graphene.ObjectType):
    paises = graphene.List(PaisType, name=graphene.String(),last=graphene.Int())
    
    
    def resolve_paises(self, info, name, last=None):
        paises = Pais.objects.all()
        if name != "":
            paises = paises.filter(nombre__icontains=name)
        if last is not None:
            paises = paises.order_by('-id')[:last]
        return paises         
        
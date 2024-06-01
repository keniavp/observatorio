import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from .models import *


# class CategoriaType(DjangoObjectType):
#     class Meta:
#         model = Categoria
#         fields = '__all__'
                
# class HistoricalCategoriaType(DjangoObjectType):
#     class Meta:
#          model = Categoria.history.model
        
# class PublicadoresType(DjangoObjectType):
#     class Meta:
#         model = Publicadores
#         fields = '__all__'
        
# class ConjuntoDatosType(DjangoObjectType):
#     class Meta:
#         model = ConjuntoDatos
#         fields = '__all__'
        
# class ConjuntoIdsType(DjangoObjectType):
#     class Meta:
#         model = ConjuntoDatos
#         fields = ['id']
        
# class HistoricalCjtodatosType(DjangoObjectType):
#     class Meta:
#          model = ConjuntoDatos.history.model
        
# class ProyectosType(DjangoObjectType):
#     class Meta:
#         model = Proyectos
#         fields = '__all__'
        
# class DatosType(DjangoObjectType):
#     class Meta:
#         model = Datos
#         fields = '__all__'
        
# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = '__all__'
        
# class IDArray(graphene.InputObjectType):
#     ids = graphene.List(graphene.ID, required=True)
    
      
# class Query(graphene.ObjectType):
#     categorias = graphene.List(CategoriaType, name=graphene.String(),last=graphene.Int())
#     historical_categoria = graphene.List(HistoricalCategoriaType, id=graphene.Int(required=True))
#     publicadores = graphene.List(PublicadoresType, name=graphene.String(),last=graphene.Int())
#     conjunto = graphene.List(ConjuntoDatosType, name=graphene.String())
#     conjuntoids = graphene.List(ConjuntoIdsType, name=graphene.String())
#     historical_cjtodatos = graphene.List(HistoricalCjtodatosType, id=graphene.Int())
#     proyectos = graphene.List(ProyectosType, name=graphene.String(),last=graphene.Int())
#     datos = graphene.List(DatosType, name=graphene.String(),last=graphene.Int())
#     usuarios = graphene.List(UserType, name=graphene.String())
    
    
#     def resolve_usuarios(self, info, name):
#         if name == "":
#             return User.objects.all()
#         else:
#             return User.objects.filter(
#                 Q(username__icontains=name) |
#                 Q(first_name__icontains=name) |
#                 Q(last_name=name) |
#                 Q(email__icontains=name)
#             )

#     def resolve_categorias(self, info, name, last=None):
#         categorias = Categoria.objects.all()
#         if name != "":
#             categorias = categorias.filter(nombre__icontains=name)
#         if last is not None:
#             categorias = categorias.order_by('-id')[:last]
#         return categorias 
         
            
#     def resolve_publicadores(self, info, name, last=None):
#         publicadores = Publicadores.objects.all()
#         if name != "":
#             publicadores = publicadores.filter(nombre__icontains=name)
#         if last is not None:
#             publicadores = publicadores.order_by('-id')[:last]
#         return publicadores 
    
    
#     def resolve_conjunto(self, info, name):
#         conjuntos = ConjuntoDatos.objects.all()
#         if name != "":
#             conjuntos = conjuntos.filter(publicadores__id=name)
#         # if last is not None:
#         #     publicadores = publicadores.order_by('-id')[:last]
#         return conjuntos 
    
#     def resolve_conjuntoid(self, info, name):
#         conjuntoids = ConjuntoDatos.objects.all()
#         if name != "":
#             conjuntoids = conjuntoids.filter(publicadores__id=name)
#         # if last is not None:
#         #     publicadores = publicadores.order_by('-id')[:last]
#         return conjuntoids 
    
    
#     def resolve_proyectos(self, info, name, last=None):
#         proyectos = Proyectos.objects.all()
#         if name != "":
#             proyectos = proyectos.filter(nombre__icontains=name)
#         if last is not None:
#             proyectos = proyectos.order_by('-id')[:last]
#         return proyectos 
    
#     def resolve_datos(self, info, name):
#         datos = Datos.objects.all()
#         if name != "":
#             datos = datos.filter(cjtodatos__id=name)
#         return datos 
    
#     def resolve_historical_categoria(self, info, id):
#         categoria = Categoria.objects.get(id=id)
#         return categoria.history.all()
    
   

#     def resolve_historical_cjtodatos(self, info, id):
       
#         if id == 0:
            
#             # Si el ID es 0, devuelve el historial de cambios de todos los objetos ConjuntoDatos
#             historial = ConjuntoDatos.history.all()
#             for obj in historial:
#                 print(obj)
#                 obj.id=id
                
#             return historial
#         else:
#             # Si el ID no es 0, obtén el objeto ConjuntoDatos correspondiente al ID y devuelve su historial de cambios
#             try:
#                 conjunto_datos = ConjuntoDatos.objects.get(id=id)
#                 return conjunto_datos.history.all()
#             except ConjuntoDatos.DoesNotExist:
#                 # Si no se encuentra ningún objeto ConjuntoDatos con el ID proporcionado, devuelve un error o un valor nulo según sea necesario
#                 return None

       
            
   
    
   
       

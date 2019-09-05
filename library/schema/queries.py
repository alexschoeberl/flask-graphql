import graphene

from library.data import items
from library.schema.libraries import Library


class Query(graphene.ObjectType):
	libraries = graphene.List(Library)
	library = graphene.Field(Library, name=graphene.String())

	@staticmethod
	def resolve_libraries(parent, info):
		libraries = {item.library for item in items}
		return [Library(name=name) for name in libraries]

	@staticmethod
	def resolve_library(parent, info, name):
		if name in {item.library for item in items}:
			return Library(name=name)

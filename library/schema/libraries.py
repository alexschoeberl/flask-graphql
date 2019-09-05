import graphene

from library.data import items
from library.schema.items import Item, Collection, CD, Book


class Library(graphene.ObjectType):
	name = graphene.String(required=True)
	items = graphene.List(graphene.NonNull(Item))

	@staticmethod
	def resolve_items(parent, info):
		derive = lambda id: {'Book': Book, 'Collection': Collection, 'CD': CD}[items[id].medium](id=id)
		return [derive(id) for id, item in enumerate(items) if item.library == parent.name]

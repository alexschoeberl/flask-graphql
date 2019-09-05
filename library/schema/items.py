from datetime import datetime

import graphene

from library.data import items


class Item(graphene.Interface):
	id = graphene.ID(required=True)
	title = graphene.String(required=True)
	included = graphene.types.datetime.Date(required=True)

	@staticmethod
	def resolve_title(parent, info):
		return items[parent.id].title

	@staticmethod
	def resolve_included(parent, info):
		return datetime.strptime(items[parent.id].included, '%Y/%m/%d').date()


class Book(graphene.ObjectType):
	class Meta:
		interfaces = (Item,)

	author = graphene.String(required=True)
	editor = graphene.String(required=True)
	publisher = graphene.String(required=True)
	published = graphene.Int(required=True)

	@staticmethod
	def resolve_author(parent, info):
		item = items[parent.id]
		return ', '.join(c.name for c in item.contributors if c.role == 'Author')

	@staticmethod
	def resolve_editor(parent, info):
		item = items[parent.id]
		return ', '.join(c.name for c in item.contributors if c.role == 'Editor')

	@staticmethod
	def resolve_publisher(parent, info):
		return items[parent.id].publisher

	@staticmethod
	def resolve_published(parent, info):
		return int(items[parent.id].published[0:4])


class Collection(graphene.ObjectType):
	class Meta:
		interfaces = (Item,)

	books = graphene.List(graphene.NonNull(Book))
	publisher = graphene.String(required=True)

	@staticmethod
	def resolve_publisher(parent, info):
		child = items[parent.id].parts[0]
		return items[child].publisher

	@staticmethod
	def resolve_books(parent, info):
		item = items[parent.id]
		return [Book(id=id) for id in item.parts]


class CD(graphene.ObjectType):
	class Meta:
		interfaces = (Item,)

	artist = graphene.String(required=True)
	label = graphene.String(required=True)
	published = graphene.Int(required=True)

	@staticmethod
	def resolve_artist(parent, info):
		item = items[parent.id]
		return ', '.join(c.name for c in item.contributors if c.role == 'Artist')

	@staticmethod
	def resolve_label(parent, info):
		return items[parent.id].publisher

	@staticmethod
	def resolve_published(parent, info):
		return int(items[parent.id].published[0:4])

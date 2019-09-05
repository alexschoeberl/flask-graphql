from flask import Flask
from flask_graphql import GraphQLView
import graphene


def application():
	app = Flask('library')
	add_interface(app)
	return app


def add_interface(app):
	from library.schema.queries import Query
	from library.schema.items import Book, CD, Collection

	schema = graphene.Schema(query=Query, types=[Book, Collection, CD])
	view = GraphQLView.as_view('api', schema=schema, graphiql=True)
	app.add_url_rule('/api', view_func=view)

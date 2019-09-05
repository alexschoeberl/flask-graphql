class Contributor:
	def __init__(self, name, role):
		self.name = name
		self.role = role


class Item:
	def __init__(self, medium, title, library, included, contributors=None, publisher=None, published=None, parts=None):
		self.medium = medium
		self.title = title
		self.contributors = contributors
		self.publisher = publisher
		self.published = published
		self.parts = parts
		self.library = library
		self.included = included


ctrbs = [
	Contributor(name='An Author 1', role='Author'),
	Contributor(name='An Author 2', role='Author'),
	Contributor(name='A Musician 1', role='Artist'),
	Contributor(name='A Musician 2', role='Artists'),
	Contributor(name='An Editor 1', role='Editor')
]

items = [
	Item('Book', 'A Book 1', 'Library 1', '2005/05/02', (ctrbs[0],), 'A publisher 1', '1995/06/11'),
	Item('Book', 'A Book 2', 'Library 1', '2005/05/02', (ctrbs[1], ctrbs[4]), 'A publisher 1', '1995/06/11'),
	Item('CD', 'A CD 1', 'Library 1', '2005/05/02', (ctrbs[2], ctrbs[3]), 'A label 1', '1995/06/11'),
	Item('CD', 'A CD 2', 'Library 1', '2005/05/02', (ctrbs[3],), 'A label 2', '1995/06/11'),
	Item('Book', 'A Book 1', 'Library 2', '2010/07/05', (ctrbs[0],), 'A publisher 1', '1995/06/11'),
	Item('Book', 'A Book 2', 'Library 2', '2010/07/05', (ctrbs[1], ctrbs[4]), 'A publisher 1', '1995/06/11'),
	Item('CD', 'A CD 1', 'Library 2', '2010/07/05', (ctrbs[2], ctrbs[3]), 'A label 1', '1995/06/11'),
	Item('CD', 'A CD 2', 'Library 2', '2010/07/05', (ctrbs[3],), 'A label 2', '1995/06/11'),
	Item('Collection', 'A Collection 1', 'Library 1', '2005/05/02', parts=(0, 1)),
	Item('Collection', 'A Collection 1', 'Library 2', '2010/07/05', parts=(4, 5))
]

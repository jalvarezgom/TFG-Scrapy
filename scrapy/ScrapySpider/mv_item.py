from scrapy import Item, Field
from py2neo.ogm import GraphObject, Property, RelatedTo

class mv_item(Item):
    user = Field()
    url = Field()
    score = Field ()
    amigos = Field (defaul=[])

class GraphItem(GraphObject):
    __primarykey__ = "user"

    user = Property()
    url = Property()
    score = Property()
    plataforma = Property()
    relation = RelatedTo("GraphItem")


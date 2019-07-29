
from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    def resolve_hello(root, info, name):
        return 'Hello {name}!'

    def resolve_goodbye(root,info):
        return 'See ya!'

schema = Schema(query=Query)

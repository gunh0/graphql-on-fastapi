import strawberry
from time import sleep

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Query:
    @strawberry.field
    def hello(self, info) -> str:
        print("[+] Recived hello request")
        sleep(1)
        return "world"


schema = strawberry.Schema(Query)


graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

import strawberry
from time import sleep

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


# Define the Query type for the GraphQL schema
@strawberry.type
class Query:
    @strawberry.field
    def hello(self, info) -> str:
        # Log each incoming GraphQL hello request
        print("[+] Received hello request")
        # Simulate processing delay
        sleep(1)
        return "world"


# Create the Strawberry GraphQL schema
schema = strawberry.Schema(Query)

# Create the GraphQL router for FastAPI
graphql_app = GraphQLRouter(schema)

# Initialize the FastAPI application
app = FastAPI()

# Mount the GraphQL router under the /graphql endpoint
app.include_router(graphql_app, prefix="/graphql")

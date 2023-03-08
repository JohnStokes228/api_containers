# api_containers
dummy API architecture to play with docker / k8s etc...

current features:
- uses fast API and uvicorn to deploy locally
- I have dockerised the project to be deployed online if desired (it's not desired what a piece of shit)
- pydantic schemas protect the request and response to the endpoint

desired updates:
- i have this image in my head of using a graphDB to store the logs / inputs / outputs. I'd like to experiment with this
- i think its worth replacing the shitty IOManager object with MLFlow for the sake of getting some experience with it
- the more i use pydantic the more uncomfortable in its 'validator' methods i am - id like to factor these out of the model. in order to ensure I'm doing this as sustainably as possible, its worth thinking up more elaborate validators and seeing if i can work around them such that the type is wholly described by its hint?
- I'd like to try out pyright and see just how much of my code fails
- I need to write some unit tests


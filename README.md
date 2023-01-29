# api_containers
dummy API architecture to play with docker / k8s etc...

to include:
- test fastAPI
- think about logging etc... <- maybe look to build this using a graph database?
- dockerise the code
- utilise pydantic to validate inputs as apparently it works very well with fastapi
- attempt a quality architecture rather than some shitty script but you know how these things go

potentially worth replacing the current IOManager object with one that uses MLFlow, just so we can 
get hands on with logging crap with that - does it work for random objects or just models though?

# Layered FastAPI — Diagram



```mermaid
flowchart TD
Client[Client]
App[app.main (FastAPI)]
Routes[Routes (/users, /health)]
Controller[Controller (UserController)]
Service[Service (UserService)]
Repository[Repository (UserRepository - in-memory)]
Models[Models (Pydantic DTOs)]
DB[(Data store)]


Client --> App
App --> Routes
Routes --> Controller
Controller --> Service
Service --> Repository
Repository --> DB


Routes -.-> Models
Controller -.-> Models
Service -.-> Models
Repository -.-> Models
```


**Legend (minimal)**

* **Routes**: HTTP mapping and DI.
* **Controller**: HTTP→service translation. Maps errors to HTTP responses.
* **Service**: Business rules and orchestration.
* **Repository**: Data access (swap for real DB later).
* **Models**: Pydantic request/response DTOs.



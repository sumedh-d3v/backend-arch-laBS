# Layered FastAPI — Diagram



```mermaid
flowchart TD
  Client[Client]
  App[app.main<br/>(FastAPI)]
  Routes[Routes<br/>(/users, /health)]
  Controller[Controller<br/>(UserController)]
  Service[Service<br/>(UserService)]
  Repository[Repository<br/>(UserRepository - in-memory)]
  Models[Models<br/>(Pydantic DTOs)]
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


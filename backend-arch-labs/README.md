# Layered FastAPI — Diagram

```mermaid
flowchart TD
  Client[Client]
  App[app.main\n(FastAPI)]
  Routes[Routes\n(/users, /health)]
  Controller[Controller\n(UserController)]
  Service[Service\n(UserService)]
  Repository[Repository\n(UserRepository - in-memory)]
  Models[Models\n(Pydantic DTOs)]
  DB[(Data store)]

  Client --> App
  App --> Routes
  Routes --> Controller
  Controller --> Service
  Service --> Repository
  Repository --> Models
  Repository --> DB
```

**Legend (minimal)**

* **Routes**: HTTP mapping and DI.
* **Controller**: HTTP→service translation. Maps errors to HTTP responses.
* **Service**: Business rules and orchestration.
* **Repository**: Data access (swap for real DB later).
* **Models**: Pydantic request/response DTOs.

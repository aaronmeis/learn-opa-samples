# FastAPI Starter - Architecture Diagrams

This document outlines the architectural design for the `fastapi-starter` project, which uses FastAPI with an OPA sidecar for RBAC.

## C4 Container Diagram

The system consists of two primary containers running in a single POD/Service unit (Docker Compose).

```mermaid
C4Container
    title Container diagram for FastAPI + OPA RBAC

    Person(user, "User/Client", "An external user making API requests.")
    
    System_Boundary(c1, "FastAPI Service Unit") {
        Container(api, "FastAPI Application", "Python/Uvicorn", "Handles business logic and enforces policies via OPA.")
        Container(opa, "Open Policy Agent", "Go/OPA", "Evaluates Rego policies and returns authorization decisions.")
    }

    Rel(user, api, "Makes API requests", "HTTPS/JSON")
    Rel(api, opa, "Sends authorization queries", "HTTP/JSON (Port 8181)")
    
    UpdateRelStyle(user, api, $lineColor="blue", $textColor="blue")
    UpdateRelStyle(api, opa, $lineColor="red", $textColor="red")
```

## Sequence Diagram: Authorization Flow

This diagram shows the step-by-step process of a request being authorized by OPA.

```mermaid
sequenceDiagram
    autonumber
    participant Client
    participant FastAPI as FastAPI App
    participant OPA as OPA Sidecar

    Client->>FastAPI: GET /resource (with X-User-Role header)
    FastAPI->>FastAPI: Extract user/context
    FastAPI->>OPA: POST /v1/data/rbac/allow (Input JSON)
    Note over OPA: Evaluates Rego policy
    OPA-->>FastAPI: 200 OK {"result": true}
    FastAPI->>FastAPI: Policy Check (Allow/Deny)
    FastAPI-->>Client: 200 OK (Resource Data)
```

## Policy Input Schema

The data structure sent from FastAPI to OPA for decision making.

```json
{
  "input": {
    "method": "GET",
    "path": ["resource"],
    "user": "alice",
    "role": "admin"
  }
}
```

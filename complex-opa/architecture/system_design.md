# Complex OPA - System Design

This project demonstrates a multi-service architecture with centralized policy management via a bundle server.

## C4 System Context Diagram

```mermaid
C4Context
    title System Context for Complex OPA RBAC

    Person(admin, "Security Administrator", "Defines and manages access control policies.")
    Person(user, "User", "Accesses the User Service to manage profiles.")

    System(opa_system, "OPA RBAC System", "Provides distributed policy enforcement.")
    
    System_Ext(bundle_server, "Policy Bundle Server", "Nginx server hosting compiled Rego policy bundles.")

    Rel(admin, bundle_server, "Pushes policy updates", "Git/CI-CD")
    Rel(user, opa_system, "Requests resources", "REST/JSON")
    Rel(opa_system, bundle_server, "Downloads bundles", "HTTP (Polling)")
```

## C4 Container Diagram

```mermaid
C4Container
    title Container architecture for Complex OPA

    System_Boundary(service, "User Service Environment") {
        Container(api, "User Service", "Node/Express", "Handles user data and requests authorization.")
        Container(opa, "OPA Agent", "Go/OPA", "Downloads policies from bundle server & evaluates them.")
    }

    System_Boundary(management, "Policy Management") {
        Container(bundle, "Bundle Server", "Nginx", "Serves rbac.tar.gz bundles.")
    }

    Rel(api, opa, "Queries for access", "Unix Socket/HTTP")
    Rel(opa, bundle, "Fetches latest bundles", "HTTP/Tarball")
```

## Implementation Strategy
- **OPA Agent**: Configured to poll the bundle server every 60 seconds.
- **Service Security**: The User Service only communicates with the local OPA agent.
- **Policy Distribution**: Policies are versioned and served as compressed tarballs.

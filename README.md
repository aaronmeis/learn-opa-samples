# OPA RBAC Samples

A collection of sample projects demonstrating Open Policy Agent (OPA) integration for Role-Based Access Control (RBAC) across different frameworks and architectures.

## Project Overviews

| Folder | Tech Stack | OPA Architecture | Features |
| :--- | :--- | :--- | :--- |
| `fastapi-starter` | FastAPI (Python) | Sidecar | High-performance async API with automated OPA enforcement. |
| `simple-opa` | Flask (Python) | Co-located | Lightweight demo using Python's Flask and local OPA decisions. |
| `complex-opa` | Node.js / Nginx | Centralized Bundle | Enterprise-grade setup with OPA agents and policy bundle server. |

## 🚀 Interactive Learning Guide

This repository features a **Premium Interactive Guide** (`index.html`) that provides:
- **Visual Deep-Dives**: Dynamic Mermaid diagrams for each architectural pattern.
- **Side-by-Side Code**: Comparative views of Rego policies and API implementations.
- **Deployment Blueprints**: Ready-to-use Docker and Docker Compose snippets.
- **One-Click Navigation**: Seamless hash-based routing between project views.

To use the guide, simply open `index.html` in your browser.

## Quick Start

### 1. Prerequisites
- Docker & Docker Compose
- (Optional) Python 3.11+, Node.js 18+ for local testing

### 2. Running a Project
Navigate to any project folder and run:
```bash
docker-compose up -d
```

## Testing Strategy

Each project includes a dedicated suite to verify both API endpoints and Rego policies.

- **FastAPI**: `pytest` + `httpx`
- **Simple OPA**: `pytest`
- **Complex OPA**: `jest` + `opa test`

Run the master verification script from the root:
```bash
./scripts/verify_all.sh
```

## Repository Hygiene
This repo is configured for clean development:
- `.gitignore`: Handles macOS metadata (`._*`), Python bytecode, and Node modules.
- `architecture/`: Contains C4 and Mermaid diagrams for each sample.
- `.github/workflows/`: Automated CI pipeline for OPA and API verification.

## Security & Licensing
- **Security**: See [SECURITY.md](SECURITY.md) for critical disclaimers regarding production authentication (JWT/OIDC).
- **License**: This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

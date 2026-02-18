# Security Policy

## 🛡️ OPA RBAC Learning Samples

This repository is designed for **educational purposes**. It demonstrates how to integrate Open Policy Agent (OPA) into various application architectures.

### ⚠️ Important Security Disclaimer
> [!WARNING]
> **This is not production-ready authentication.** 
> To simplify the RBAC demonstration, these projects use custom HTTP headers (like `X-User-Role`) for identity. In a production environment:
> 1. **OIDC/JWT**: You must use a cryptographically signed token (like JWT) from an Identity Provider (IdP).
> 2. **Verification**: Your application (or OPA) must verify the signature of these tokens.
> 3. **mTLS**: Ensure communication between your API and OPA is secured via TLS/mTLS if they are not co-located in a trusted pod.

## Reporting a Vulnerability

If you find a security issue in the **OPA policy logic** or the **integration patterns**, please open an issue or contact the maintainers. Since this is a learning sample, we value architectural feedback that helps users build more secure systems!

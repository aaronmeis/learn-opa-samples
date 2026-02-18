from fastapi import FastAPI, Request, HTTPException, Header
import httpx
import json

app = FastAPI(title="FastAPI OPA RBAC Starter")

OPA_URL = "http://opa:8181/v1/data/rbac/allow"

async def check_opa_permission(user: str, role: str, method: str, path: list):
    input_data = {
        "input": {
            "user": user,
            "role": role,
            "method": method,
            "path": path
        }
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(OPA_URL, json=input_data)
            response.raise_for_status()
            result = response.json().get("result", False)
            return result
        except Exception as e:
            print(f"Error connecting to OPA: {e}")
            return False

@app.middleware("http")
async def opa_auth_middleware(request: Request, call_next):
    # Skip OPA for docs
    if request.url.path in ["/docs", "/openapi.json", "/redoc"]:
        return await call_next(request)

    user = request.headers.get("X-User-Id", "anonymous")
    role = request.headers.get("X-User-Role", "guest")
    method = request.method
    path = request.url.path.strip("/").split("/")

    allowed = await check_opa_permission(user, role, method, path)
    
    if not allowed:
        raise HTTPException(status_code=403, detail="Forbidden by OPA Policy")
        
    return await call_next(request)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI OPA RBAC Starter!"}

@app.get("/admin")
async def admin_only():
    return {"message": "Hello Admin! You have access to this secure endpoint."}

@app.get("/user")
async def user_area():
    return {"message": "Hello User! This is your workspace."}

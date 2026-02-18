package rbac

import future.keywords.if

default allow := false

# Admin has full access
allow if {
    input.role == "admin"
}

# Users can view profiles
allow if {
    input.role == "user"
    input.method == "GET"
    input.path[0] == "users"
}

# Audit policy meta
meta := {
    "version": "1.0.0",
    "environment": "production"
}

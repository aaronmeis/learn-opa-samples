package rbac

import future.keywords.if

default allow := false

# Public access
allow if {
    input.path == ["public"]
}

# User and Admin access to secure
allow if {
    input.role in ["user", "admin"]
    input.path == ["secure"]
}

# Admin only access to admin
allow if {
    input.role == "admin"
    input.path == ["admin"]
}

# Allow root
allow if {
    input.path == [""]
}

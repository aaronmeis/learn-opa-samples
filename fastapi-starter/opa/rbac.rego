package rbac

import future.keywords.if
import future.keywords.contains

default allow := false

# Allow admin to do anything
allow if {
    input.role == "admin"
}

# Allow users to access "/user" path
allow if {
    input.role == "user"
    input.path == ["user"]
}

# Allow everyone to access the root path
allow if {
    input.path == [""]
}

# Allow everyone to access the root path (empty list if path is empty)
allow if {
    count(input.path) == 0
}

package rbac

test_allow_admin {
    allow with input as {"role": "admin", "path": ["users"]}
}

test_allow_user_get_users {
    allow with input as {"role": "user", "method": "GET", "path": ["users"]}
}

test_deny_user_post_users {
    not allow with input as {"role": "user", "method": "POST", "path": ["users"]}
}

test_deny_guest {
    not allow with input as {"role": "guest", "path": ["users"]}
}

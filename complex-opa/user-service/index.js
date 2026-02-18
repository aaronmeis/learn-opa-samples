const express = require('express');
const axios = require('axios');
const app = express();

const OPA_URL = process.env.OPA_URL || 'http://opa:8181/v1/data/rbac/allow';

async function checkPermission(user, role, method, path) {
    try {
        const response = await axios.post(OPA_URL, {
            input: {
                user,
                role,
                method,
                path: path.split('/').filter(p => p)
            }
        });
        return response.data.result === true;
    } catch (error) {
        console.error('Error querying OPA:', error.message);
        return false;
    }
}

app.use(async (req, res, next) => {
    const user = req.headers['x-user-id'] || 'anonymous';
    const role = req.headers['x-user-role'] || 'guest';

    const allowed = await checkPermission(user, role, req.method, req.path);

    if (allowed) {
        next();
    } else {
        res.status(403).json({ error: 'Forbidden by OPA' });
    }
});

app.get('/users', (req, res) => {
    res.json([{ id: 1, name: 'Alice' }, { id: 2, name: 'Bob' }]);
});

app.get('/users/:id', (req, res) => {
    res.json({ id: req.params.id, name: 'User Info' });
});

app.listen(3000, () => {
    console.log('User Service listening on port 3000');
});

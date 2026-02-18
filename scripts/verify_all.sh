#!/bin/bash
set -e

echo "🚀 Starting Master Verification Suite..."

echo "------------------------------------------------"
echo "📂 Project 1: fastapi-starter"
echo "------------------------------------------------"
pytest fastapi-starter/api/tests/

echo "------------------------------------------------"
echo "📂 Project 2: simple-opa"
echo "------------------------------------------------"
pytest simple-opa/tests/

echo "------------------------------------------------"
echo "📂 Project 3: complex-opa"
echo "------------------------------------------------"
echo "Verifying Rego policies with 'opa test'..."
if command -v opa &> /dev/null
then
    opa test complex-opa/policies/ -v
else
    echo "⚠️  OPA binary not found. Skipping Rego unit tests."
    echo "Download OPA from: https://www.openpolicyagent.org/docs/latest/#1-download-opa"
fi

echo "------------------------------------------------"
echo "✅ All local checks completed!"

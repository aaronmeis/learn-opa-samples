#!/bin/bash
# Script to create the OPA bundle
mkdir -p bundles
tar -czvf bundles/rbac.tar.gz -C ../policies rbac.rego
mv bundles/rbac.tar.gz ../bundle-server/www/bundles/
rm -rf bundles
echo "Bundle created at complex-opa/bundle-server/www/bundles/rbac.tar.gz"

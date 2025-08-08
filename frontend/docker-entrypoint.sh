#!/bin/sh
set -e

# Generate /usr/share/nginx/html/config.js from env var FRONTEND_API_BASE_URL
: "${FRONTEND_API_BASE_URL:=http://localhost:5000}"
cat > /usr/share/nginx/html/config.js <<EOF
window.APP_CONFIG = {
  API_BASE_URL: "${FRONTEND_API_BASE_URL}"
};
EOF

# Continue with default nginx entrypoint

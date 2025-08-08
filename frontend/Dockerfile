# Frontend Dockerfile (production-ready)
FROM node:20-alpine AS build
WORKDIR /frontend
COPY frontend/package.json frontend/vite.config.js frontend/index.html ./
COPY frontend/src ./src
COPY frontend/public ./public
RUN npm install --no-audit --no-fund && npm run build

FROM nginx:1.27-alpine AS runtime
# Copy built assets
COPY --from=build /frontend/dist /usr/share/nginx/html
# Default runtime config.js; can be overridden at container start via env or volume
COPY frontend/nginx.conf /etc/nginx/conf.d/default.conf
COPY frontend/docker-entrypoint.sh /docker-entrypoint.d/99-config.sh
RUN chmod +x /docker-entrypoint.d/99-config.sh

EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]

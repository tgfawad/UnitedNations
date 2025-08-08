window.APP_CONFIG = {
  API_BASE_URL:
    (typeof importMetaEnv !== "undefined" &&
      importMetaEnv?.VITE_FALLBACK_API_BASE_URL) ||
    "http://localhost:5000",
};

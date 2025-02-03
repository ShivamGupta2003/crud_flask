// import { defineConfig } from 'vite'
// import react from '@vitejs/plugin-react-swc'

// // https://vite.dev/config/
// export default defineConfig({
//   plugins: [react()],
// })
// import { defineConfig } from "vite";
// import react from "@vitejs/plugin-react-swc";

// export default defineConfig({
//   plugins: [react()],
//   server: {
//     port: parseInt(process.env.PORT) || 3000, // Use Render's assigned port
//     host: "0.0.0.0", // Allow external access
//   },
// });

import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";

export default defineConfig({
  plugins: [react()],
  server: {
    port: parseInt(process.env.PORT) || 3000, // Use Render's assigned port
    host: "0.0.0.0", // Allow external access
    allowedHosts: ["crud-flask-xwmq.onrender.com"], // Add your backend host here
    proxy: {
      "/api": {
        target: "https://crud-flask-xwmq.onrender.com", // Your Flask backend URL on Render
        changeOrigin: true,
        secure: false, // If you're using HTTP, set this to false. For HTTPS, set true
      },
    },
  },
});

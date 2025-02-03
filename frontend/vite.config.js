// import { defineConfig } from 'vite'
// import react from '@vitejs/plugin-react-swc'

// // https://vite.dev/config/
// export default defineConfig({
//   plugins: [react()],
// })
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";

export default defineConfig({
  plugins: [react()],
  server: {
    port: parseInt(process.env.PORT) || 3000, // Use Render's assigned port
    host: "0.0.0.0", // Allow external access
    allowedHosts: ["crud-flask-xwmq.onrender.com"], // Add your host here
  },
});

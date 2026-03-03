// webpack.config.js
import path from "path";

export default {
  entry: "./src/index.js",       // Entry point of your React app
  output: {
    path: path.resolve("dist"),  // Output folder
    filename: "bundle.js",       // Output bundle
    publicPath: "/",             // Ensure DevServer serves bundle from root
  },
  mode: "development",           // Development mode
  module: {
    rules: [
      {
        test: /\.jsx?$/,         // Handles .js and .jsx files
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-react"], // Transpile React JSX
          },
        },
      },
      {
        test: /\.css$/i,         // Handles CSS imports
        use: ["style-loader", "css-loader"], // Inject CSS into DOM
      },
      {
        test: /\.(png|jpe?g|gif|svg)$/i, // Handles image assets
        type: "asset/resource",
      },
    ],
  },
  resolve: {
    extensions: [".js", ".jsx"], // Allow imports without specifying extensions
  },
  devServer: {
    static: {
      directory: path.join("public"), // Serve static files from public/
    },
    compress: true,        // Enable gzip compression
    port: 3000,            // Dev server port
    open: true,            // Opens browser automatically
    historyApiFallback: true, // For React Router (SPA fallback)
  },
};
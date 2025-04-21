# Sports Performance Pro - Zip #5

## Structure

```
SPP-Zip5/
├── server/
│   ├── package.json
│   └── index.js
└── client/
    ├── package.json
    ├── vite.config.js
    ├── public/
    │   └── index.html
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── contexts/
        │   └── AuthContext.jsx
        └── pages/
            ├── Login.jsx
            └── Profile.jsx
```

## Getting Started

1. **Server**  
   ```bash
   cd server
   npm install
   JWT_SECRET=your_secret node index.js
   ```

2. **Client**  
   ```bash
   cd client
   npm install
   npm run dev
   ```

Client will run on `http://localhost:3000`, server on `http://localhost:4000`.

# Sports Performance Pro - Zip #5 (v4)

## Structure

```
SPP-Zip5-v4/
├── backend/
│   ├── package.json
│   ├── index.js
│   └── Procfile
└── frontend/
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

- **backend/**: Node/Express auth server. Deploy this directory to Railway, root is backend.
- **frontend/**: Vite/React app. Deploy this directory to Vercel, root is frontend.

No confusion—each directory is self-contained for its platform.

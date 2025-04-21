import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Login from './pages/Login';
import Profile from './pages/Profile';
import { useAuth } from './contexts/AuthContext';

function App() {
  const { token } = useAuth();
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route
        path="/profile"
        element={token ? <Profile /> : <Navigate to="/login" />}
      />
      <Route path="*" element={<Navigate to={token ? '/profile' : '/login'} />} />
    </Routes>
  );
}

export default App;

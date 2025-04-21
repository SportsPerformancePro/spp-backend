import React, { createContext, useState, useContext } from 'react';

const AuthContext = createContext();
export function AuthProvider({ children }) {
  const [token, setToken] = useState(localStorage.getItem('token'));
  const [name, setName] = useState(localStorage.getItem('name'));

  const login = (jwtToken, userName) => {
    localStorage.setItem('token', jwtToken);
    localStorage.setItem('name', userName);
    setToken(jwtToken);
    setName(userName);
  };

  const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('name');
    setToken(null);
    setName(null);
  };

  return (
    <AuthContext.Provider value={{ token, name, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
export const useAuth = () => useContext(AuthContext);

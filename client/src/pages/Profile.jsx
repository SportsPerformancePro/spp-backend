import React, { useEffect, useState } from 'react';
import { useAuth } from '../contexts/AuthContext';

export default function Profile() {
  const { token, name, logout } = useAuth();
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    fetch('http://localhost:4000/api/profile', {
      headers: { Authorization: `Bearer ${token}` }
    })
      .then(res => res.json())
      .then(data => setProfile(data));
  }, [token]);

  return (
    <div>
      <h2>Welcome, {profile?.name || name}!</h2>
      <button onClick={logout}>Log Out</button>
    </div>
  );
}

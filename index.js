import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import jwt from 'jsonwebtoken';

const app = express();
app.use(bodyParser.json());
app.use(cors());

const users = [
  { id: 1, email: 'demo@test.com', password: 'password123', name: 'Demo User' }
];
const JWT_SECRET = process.env.JWT_SECRET || 'your_jwt_secret';

app.post('/api/login', (req, res) => {
  const { email, password } = req.body;
  const user = users.find(u => u.email === email && u.password === password);
  if (!user) return res.status(401).json({ message: 'Invalid credentials' });
  const token = jwt.sign({ sub: user.id, name: user.name }, JWT_SECRET, { expiresIn: '2h' });
  res.json({ token, name: user.name });
});

app.get('/api/profile', (req, res) => {
  const auth = req.headers.authorization;
  if (!auth) return res.status(401).json({ message: 'No token' });
  const token = auth.split(' ')[1];
  try {
    const payload = jwt.verify(token, JWT_SECRET);
    res.json({ id: payload.sub, name: payload.name });
  } catch {
    res.status(401).json({ message: 'Invalid token' });
  }
});

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => console.log(`Auth server running on http://localhost:${PORT}`));

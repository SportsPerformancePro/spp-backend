const express = require('express');
const auth = require('../middleware/auth');
const router = express.Router();

// Demo profile store
const profiles = {};

router.get('/', auth, (req, res) => {
  const profile = profiles[req.user.email] || {};
  res.json(profile);
});

router.post('/', auth, (req, res) => {
  profiles[req.user.email] = req.body;
  res.json({ message: 'Profile saved' });
});

module.exports = router;

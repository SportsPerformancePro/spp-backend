const express = require('express');
const auth = require('../middleware/auth');
const { Configuration, OpenAIApi } = require('openai');
const router = express.Router();

const config = new Configuration({ apiKey: process.env.OPENAI_API_KEY });
const openai = new OpenAIApi(config);

router.post('/', auth, async (req, res) => {
  const { sport, key } = req.body;
  const prompt = `Analyze this ${sport} video: s3://${process.env.S3_BUCKET_NAME}/${key}`;
  try {
    const completion = await openai.createChatCompletion({
      model: process.env.CHATGPT_MODEL,
      messages: [{ role: 'user', content: prompt }]
    });
    res.json({ feedback: completion.data.choices[0].message.content });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;

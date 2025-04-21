const express = require('express');
const auth = require('../middleware/auth');
const AWS = require('aws-sdk');
const router = express.Router();

AWS.config.update({ region: process.env.AWS_REGION });
const s3 = new AWS.S3();

router.get('/upload-url', auth, async (req, res) => {
  const key = `videos/${req.user.email}/${Date.now()}.mp4`;
  const url = s3.getSignedUrl('putObject', {
    Bucket: process.env.S3_BUCKET_NAME,
    Key: key,
    Expires: 3600,
    ContentType: 'video/mp4'
  });
  res.json({ url, key });
});

module.exports = router;

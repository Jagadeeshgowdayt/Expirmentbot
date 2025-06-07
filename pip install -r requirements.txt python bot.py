
   - Push to GitHub.
   - In Koyeb Dashboard, create a new app from GitHub repo.
   - Provide the above secret environment variables.
   - Choose Dockerfile and HTTP port `8443` for webhooks or leave default for polling.

5. **Set webhook** (if using webhooks):
   ```bash
curl -F "url=https://<your-koyeb-domain>/webhook" \
     https://api.telegram.org/bot${BOT_TOKEN}/setWebhook

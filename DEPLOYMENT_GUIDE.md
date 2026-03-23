# 📚 Panduan Deployment Flask Documentation App

Dokumentasi lengkap untuk men-deploy aplikasi Flask ke berbagai platform production.

---

## 🚀 Persiapan Production

### 1. Update requirements.txt
```bash
pip freeze > requirements.txt
```

Pastikan file `requirements.txt` sudah dibuat dengan semua dependencies yang diperlukan.

### 2. Buat file .env
Buat file `.env` di root project dengan secret key yang kuat:

```
FLASK_ENV=production
FLASK_DEBUG=0
SECRET_KEY=generate-secret-key-yang-sangat-kuat
```

Untuk generate secret key di Python:
```python
import secrets
print(secrets.token_hex(16))
```

### 3. Update app.py untuk Production

```python
import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-change-me')
app.config['DEBUG'] = False  # CRITICAL: Set debug=False di production

# ... rest of code ...

if __name__ == "__main__":
    # Production mode
    app.run(
        host='0.0.0.0',
        port=int(os.getenv('PORT', 5000)),
        debug=False
    )
```

---

## 📋 Pilihan Platform Deployment

### OPSI 1: Render (RECOMMENDED - Free & Easy)

**Keuntungan:**
- ✅ Free tier tersedia
- ✅ Auto deployment dari GitHub
- ✅ Custom domain support
- ✅ SSL certificate gratis
- ✅ Tidak perlu credit card awal

**Langkah-langkah:**

1. **Push ke GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Buat akun Render:**
   - Kunjungi https://render.com
   - Sign up dengan GitHub account
   - Authorize Render

3. **Deploy di Render:**
   - Click "New +" → "Web Service"
   - Pilih repository Flask Anda
   - Isi form:
     - **Name:** flask-documentation-app
     - **Environment:** Python 3
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn app:app`
   - Click "Create Web Service"

4. **Set Environment Variables:**
   - Go to Settings → Environment
   - Add:
     ```
     FLASK_ENV=production
     FLASK_DEBUG=0
     SECRET_KEY=<your-secret-key>
     ```
   - Click "Save"

5. **URL Aplikasi:**
   - Aplikasi akan live di: `https://your-app-name.onrender.com`

---

### OPSI 2: Heroku

**Persiapan:**

1. **Install Heroku CLI:**
   ```bash
   # Windows: Download dari https://devcenter.heroku.com/articles/heroku-cli
   # macOS/Linux:
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. **Login ke Heroku:**
   ```bash
   heroku login
   ```

3. **Buat app di Heroku:**
   ```bash
   heroku create nama-app-anda
   ```

4. **Set Config Variables:**
   ```bash
   heroku config:set FLASK_ENV=production
   heroku config:set FLASK_DEBUG=0
   heroku config:set SECRET_KEY=<secret-key-anda>
   ```

5. **Deploy:**
   ```bash
   git push heroku main
   # atau untuk branch lain:
   git push heroku <branch-name>:main
   ```

6. **Lihat log:**
   ```bash
   heroku logs --tail
   ```

---

### OPSI 3: PythonAnywhere (Beginner Friendly)

**Keuntungan:**
- ✅ Sangat mudah untuk pemula
- ✅ Free tier dengan subdomain
- ✅ Web-based terminal
- ✅ Django/Flask preset tersedia

**Langkah-langkah:**

1. **Buat akun**
   - Kunjungi https://www.pythonanywhere.com
   - Sign up (free account)

2. **Buka bash console** di PythonAnywhere website

3. **Clone repository:**
   ```bash
   git clone <github-repo-url>
   cd <project-name>
   ```

4. **Setup virtual environment:**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 myapp
   pip install -r requirements.txt
   pip install gunicorn
   ```

5. **Create WSGI file:**
   - Di Web tab → Add a new web app
   - Choose "Manual configuration" → Python 3.10
   - Di WSGI configuration file, edit dan ganti dengan:

   ```python
   import os
   import sys
   
   path = '/home/your-username/your-project'
   if path not in sys.path:
       sys.path.append(path)
   
   from app import app as application
   ```

6. **Reload web app**

7. **Custom domain:**
   - Edit configuration atau upgrade untuk custom domain

---

### OPSI 4: DigitalOcean Droplet (Advanced)

**Biaya:** ~$5/bulan untuk droplet kaecil

**Setup:**

1. **Create Droplet:**
   - OS: Ubuntu 22.04 LTS
   - Size: Basic ($5/month)

2. **Di terminal server:**

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y python3-pip python3-venv nginx supervisor

# Clone repo
cd /home/ubuntu
git clone <your-repo>
cd <project-name>

# Setup venv
python3 -m venv venv
source venv/bin/activate

# Install packages
pip install -r requirements.txt
pip install gunicorn

# Create .env file
cp .env.example .env
# Edit .env dengan secret key yang kuat
nano .env

# Test run
gunicorn app:app --bind 0.0.0.0:8000
```

3. **Setup Supervisor (untuk auto-restart):**

Create `/etc/supervisor/conf.d/flask_app.conf`:
```ini
[program:flask_app]
directory=/home/ubuntu/flask-documentation-app
command=/home/ubuntu/flask-documentation-app/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 app:app
user=ubuntu
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/home/ubuntu/flask-documentation-app/logs/gunicorn.log
```

```bash
sudo systemctl restart supervisor
```

4. **Setup Nginx (Reverse Proxy):**

Create `/etc/nginx/sites-available/flask_app`:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /home/ubuntu/flask-documentation-app/static;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/flask_app /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

5. **Enable HTTPS dengan Let's Encrypt:**
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

---

### OPSI 5: Google Cloud Run (Container)

**Keuntungan:**
- ✅ Serverless (pay-per-use)
- ✅ Auto-scaling
- ✅ Gratis first 2 juta requests/bulan

**Setup:**

1. **Install Google Cloud SDK:**
   ```bash
   # Download dari https://cloud.google.com/sdk/docs/install
   ```

2. **Install Docker:**
   ```bash
   # Download Docker Desktop
   ```

3. **Create Dockerfile:**
   ```dockerfile
   FROM python:3.10-slim
   
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   
   ENV FLASK_APP=app.py
   ENV FLASK_ENV=production
   
   CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
   ```

4. **Build & Deploy:**
   ```bash
   gcloud auth login
   gcloud config set project PROJECT_ID
   
   gcloud run deploy python-flask-docs \
       --source . \
       --platform managed \
       --region us-central1 \
       --set-env-vars SECRET_KEY=<your-key>,FLASK_ENV=production
   ```

---

## 🔒 Security Checklist

Sebelum deploy ke production, pastikan:

- ☑️ `FLASK_DEBUG = False` di production
- ☑️ `SECRET_KEY` yang kuat (pakai secrets module)
- ☑️ Update semua packages ke versi terbaru
- ☑️ Environment variables tersimpan di `.env` (jangan di-commit)
- ☑️ HTTPS enabled
- ☑️ Database password & credentials di env vars
- ☑️ Input validation & SQL injection protection
- ☑️ CORS settings sesuai kebutuhan
- ☑️ Rate limiting untuk API
- ☑️ Regular backups untuk database

---

## 📊 Monitoring & Logging

### Di Production, setup logging yang baik:

```python
import logging
from logging.handlers import RotatingFileHandler
import os

if not os.path.exists('logs'):
    os.mkdir('logs')

file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240000, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

app.logger.info('Flask app startup')
```

### Monitor aplikasi menggunakan:
- **Heroku:** Built-in logs & monitoring
- **Render:** Logs tab di dashboard
- **PythonAnywhere:** Web logs & error logs
- **DigitalOcean:** Systemd status & supervisor logs
- **Google Cloud:** Cloud Logging

---

## 🚨 Troubleshooting Deployment

| Error | Solusi |
|-------|---------|
| **Module not found** | Pastikan `requirements.txt` lengkap dan `pip install` di production |
| **Static files tidak load** | Pastikan `STATIC_FOLDER` dan `TEMPLATE_FOLDER` paths benar |
| **Database connection error** | Check environment variables, pastikan database accessible |
| **CORS error** | Install & setup `Flask-CORS`, add to allowed origins |
| **Memory error** | Reduce workers di gunicorn atau upgrade instance |
| **Timeout error** | Increase timeout di load balancer atau optimize code |

---

## 📞 Support & Resources

- **Flask Docs:** https://flask.palletsprojects.com/
- **Render Docs:** https://render.com/docs
- **Heroku Docs:** https://devcenter.heroku.com/
- **PythonAnywhere Help:** https://www.pythonanywhere.com/help/
- **DigitalOcean Tutorials:** https://www.digitalocean.com/community/tutorials

---

## 💡 Recommended Next Steps AFTER Deploy

1. ✅ Setup domain custom (.com, .id, dll)
2. ✅ Enable HTTPS/SSL certificate
3. ✅ Setup monitoring & alerting
4. ✅ Implement CI/CD pipelines (GitHub Actions)
5. ✅ Setup database untuk data persistence
6. ✅ Implement authentication & authorization
7. ✅ Add API rate limiting
8. ✅ Setup automated backups
9. ✅ Monitor performance & optimize
10. ✅ Plan untuk scaling

---

Selamat deploy! 🚀

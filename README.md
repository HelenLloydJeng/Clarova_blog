# Clarova Blog

A Django-based blog platform featuring user authentication, post management, and responsive design. Deployed on **Heroku**.

---

## 🚀 Deployment

Access the live application here:  
👉 [https://ai-tools-training-blog.herokuapp.com/](https://ai-tools-training-blog.herokuapp.com/)

---

## 📚 Features

- User authentication (sign up, log in, log out)
- Create, edit, and delete blog posts
- Responsive design using HTML templates
- SQLite for development database
- Production deployment on Heroku

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Django 4.x**
- **SQLite** (development)
- **Heroku** (deployment)
- **Git/GitHub** (version control)

---

## 📁 Project Structure

```plaintext
├── blog/                # Blog application
├── templates/           # HTML templates # User authentication application
├── users/               # User authentication application
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
├── Procfile             # Heroku process file
├── README.md            # Project documentation
└── LICENSE              # Project license
```

---

## 🐛 Known Issues & Fixes

Here is your **cleaned and properly formatted Markdown table** for the `README.md` – including the original issues and newly fixed ones. I've also updated the status of the previously pending issues based on your progress.

---

### 🐛 Known Issues & Fixes

| Issue                                        | Status     | Resolution                                      |
|---------------------------------------------|------------|-------------------------------------------------|
| `requirements.txt` not detected by Heroku   | ✅ Fixed   | Placed in root directory.                       |
| `.venv` included in Git repository          | ⚠️ Unnecessary | Added `.venv/` to `.gitignore`.            |
| Incorrect project structure                 | ✅ Fixed   | Moved app folders and settings to root.         |
| Migrations not applied on Heroku            | ✅ Fixed   | Ran `heroku run python manage.py migrate`.      |
| Static files not loading                    | 🚧 Pending | Whitenoise is set up — confirm `collectstatic`. |
| Secret key / env settings hardcoded         | 🚧 Pending | Use env vars or `django-environ`.               |
| `TemplateDoesNotExist: home.html`           | ✅ Fixed   | Moved `home.html` to lowercase `templates/`.    |
| `templates/Blog/` not recognized            | ✅ Fixed   | Renamed to `templates/blog/`.                   |
| `Reverse for 'post_list'` error             | ✅ Fixed   | Added `post_list` view and URL pattern.         |
| Broken HTML in `base.html`                  | ✅ Fixed   | Added `<!DOCTYPE html>` and HTML structure.     |
| `home.html` not extending base              | ✅ Fixed   | Verified `{% extends 'base.html' %}` syntax.    |
| Wrong Heroku app name in deploy             | ✅ Fixed   | Used correct name: `ai-tools-training-blog`.    |
| Git case sensitivity conflict               | ✅ Fixed   | Renamed `Templates` safely to `templates`.      |
| Heroku showed default page                  | ✅ Fixed   | Home view and URL configured correctly.         |




## 💻 Local Development Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/HelenLloydJeng/Clarova_blog.git
   cd Clarova_blog
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

---

## 📝 Future Improvements

- Add post categories and tags
- Implement search functionality
- Enhance UI/UX design
- Add pagination for blog posts
- Use PostgreSQL in production
- Write tests for key functionalities

---

## 🏷️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- The Django community for their extensive documentation and support.
- Heroku for providing an accessible deployment platform.
````
---
## Credits

---

## 🔁 Automatic Deployment (CI/CD)

This project includes **GitHub Actions integration** to automatically deploy the app to Heroku whenever changes are pushed to the `main` branch.

### ⚙️ How it works:

- On every push to `main`, GitHub runs a workflow (`deploy.yml`)
- The workflow authenticates with Heroku using stored secrets
- It builds and deploys the latest version to Heroku automatically

### 🔐 GitHub Secrets Used:

| Secret Name        | Description                            |
|--------------------|----------------------------------------|
| `HEROKU_API_KEY`   | Your Heroku account API key            |
| `HEROKU_EMAIL`     | Email linked to your Heroku account    |
| `HEROKU_APP_NAME`  | Your app’s name on Heroku              |

### 📝 To trigger deployment:
Just commit and push to `main`:

```bash
git add .
git commit -m "Update blog features"
git push origin main
```

GitHub will take care of the deployment automatically.



---






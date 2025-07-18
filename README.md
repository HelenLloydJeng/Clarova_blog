# Clarova Blog

A Django-based blog platform featuring user authentication, post management, and responsive design. Deployed on **Heroku**.

---
## 🧑‍💻 User Stories

| User Story | Screenshot |
|------------|------------|
| ✅ As a visitor, I can view blog posts | ![View Posts](screenshots/view-posts.png) |
| ✅ As a logged-in user, I can leave a comment | ![Leave Comment](screenshots/leave-comment.png) |
| ✅ As an admin, I can create/edit/delete posts | ![Admin Actions](screenshots/admin-actions.png) |


## 🚀 Deployment

Access the live application here:  
👉 [https://ai-tools-training-blog.herokuapp.com/](https://ai-tools-training-blog.herokuapp.com/)

## 🔑 Admin Credentials (for assessment only)

**Username:** admin  
**Password:** SecureTemp123

## 🖼️ Application Preview

![Screenshot of post list](screenshots/post-list.png)

---

## 📚 Features

- User authentication (sign up, log in, log out)
- Create, edit, and delete blog posts (superuser only)
- Responsive design using HTML templates
- SQLite for development database
- Production deployment on Heroku

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Django 4.x**
- **PostSQL** (development)
- **Heroku** (deployment)
- **Git/GitHub** (version control)

---

## 📁 Project Structure

├── blog/                # Blog logic (models, views, urls)
├── users/               # User authentication
├── templates/           # HTML templates
├── static/              # CSS and static files
├── manage.py            # Django CLI

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
|Second Heroku PostgreSQL databases attached  | ✅ Fixed	 |Remove 2nd add-on HEROKU_POSTGRESQL_NAVY destroy |
|`ProgrammingError: relation "blog_post" 
does not exist`                               | ✅ Fixed   |Add 'heroku run python manage.py migrate` apply missing database tables |
| `Page not found (404)` after login redirect | ✅ Fixed   | Added `LOGIN_REDIRECT_URL = '/users/profile/'` to `settings.py` to override Django default `/accounts/profile/` |

---

## ✅ Testing

| Test Description                      | Status | Notes                                                  |
| ------------------------------------- | ------ | ------------------------------------------------------ |
| Unit tests for blog views and forms   | ✅ Pass | All 5 tests passed including create, update, and delete |
| `PostForm` field validation           | ✅ Pass | Confirmed `title` and `content` are validated correctly |

### 🧪 Feature Testing & Fixes

| Feature                                | Status     | Notes                                                                 |
|----------------------------------------|------------|-----------------------------------------------------------------------|
| Django `PostTests` test suite          | ✅ Passed   | 5 tests passed after correcting field name mismatches in forms/tests. |
| `TemplateDoesNotExist: signup.html`    | ✅ Fixed    | Created `registration/signup.html` and confirmed proper template path. |
| User signup and login functionality    | ✅ Working  | Tested locally using Django's `runserver`; signup and login succeed.  |
| Page not found for `/users/signup/`    | ✅ Fixed    | Corrected `urls.py` to point to correct signup view and route.        |

| Feature Tested                | Expected Result                       | Actual Result       | Pass? |
| ----------------------------- | ------------------------------------- | ------------------- | ----- |
| User login                    | Redirect to profile after login       | ✅ Works as expected | ✅     |
| Create blog post (admin only) | Form should save and redirect to post | ✅ Saved correctly   | ✅     |
| Leave comment (logged in)     | Comment appears under post            | ✅ Displayed         | ✅     |

## ✅ Code Validation

All templates and CSS files passed W3C validation. Minor warnings were addressed.

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

Credits
This project was built with the help of the following tools and resources:

🧠 ChatGPT (OpenAI) – for troubleshooting, guidance, and step-by-step debugging

🤖 GitHub Copilot – for intelligent code suggestions and auto-completions

📚 Django Documentation – https://docs.djangoproject.com

🎓 Code Institute and YouTube tutorials – for examples on user authentication, blog functionality, and deployment

☁️ Heroku Documentation – for assistance with deployment and PostgreSQL setup

💻 Bootstrap – for front-end styling and responsive design



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

---






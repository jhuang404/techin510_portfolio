# Jialu Huang Portfolio Website


## Project Structure

```
PORTFOLIO/
│
├── app.py                 # Flask application file
│
├── static/
│   ├── style.css          # CSS stylesheet
│   │
│   └── images/            # Image assets
│       ├── profile.jpg
│       ├── mobile_temple_cover.png
│       └── mobile_temple_1.png
│
└── templates/             # HTML templates
    ├── index.html         # Homepage
    ├── about.html         # About page
    └── mobile_temple.html # Project page
```

## Requirements

- Python 3.6 or higher
- Flask

## Installation

1. Clone the repository or download the project files

2. Create and activate a virtual environment (recommended):

   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install Flask:

   ```bash
   pip install flask
   ```

## Running the Application

1. Make sure your virtual environment is activated

2. Navigate to the project directory:

   ```bash
   cd path/to/PORTFOLIO
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Open your web browser and go to http://127.0.0.1:5000/

## Customizing the Portfolio

### Adding New Projects

1. Add project images to the `static/images/` folder

2. Create a new HTML template for your project in the `templates/` folder

3. Add a new route in `app.py`:

   ```python
   @app.route('/your-project-name')
   def your_project_function():
       return render_template('your_project.html')
   ```

4. Add a new project card to the homepage (`index.html`):

   ```html
   <a href="/your-project-name" class="work-card" style="text-decoration:none;">
     <img src="{{ url_for('static', filename='images/your_project_cover.png') }}" alt="Project Name" class="work-img">
     <div class="work-info">
       <div class="work-title">Project Name</div>
       <div class="work-meta">Date Range</div>
       <div class="work-desc">Short description</div>
     </div>
   </a>
   ```

### Modifying Styles

Edit the `static/style.css` file to change colors, typography, spacing, and other design elements.

from flask import render_template, request, redirect, url_for, Blueprint
import markdown
import os

def setup_routes(app):
    @app.route('/')
    @app.route('/home')
    def home():
        return render_template('home.html', title='HOME')

    @app.route('/about')
    def about():
        return render_template('about.html', title='ABOUT')

    @app.route('/projects')
    def projects():
        return render_template('projects.html', title='PROJECTS')

    @app.route('/contact')
    def contact():
        return render_template('contact.html', title='CONTACT')

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html', title='404'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html', title='500'), 500

    @app.route('/upload_markdown')
    def index():
        return render_template('upload.html')

    @app.route('/upload', methods=['POST'])
    def upload_file():
        if 'file' not in request.files:
            return 'No file part'
        
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        
        if file and file.filename.endswith('.md'):
            file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads', file.filename)
            file.save(file_path)

            # Convert markdown to HTML
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                html_content = markdown.markdown(content)

            # Save the HTML content to a file
            html_filename = file.filename.rsplit('.', 1)[0] + '.html'
            html_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'articles', html_filename)
            with open(html_file_path, 'w', encoding='utf-8') as html_file:
                html_file.write(html_content)

            return redirect(url_for('articles'))
        
        return 'Invalid file format. Only .md files are allowed.'

    @app.route('/articles')
    def articles():
        # List all articles
        articles_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'articles')
        articles_list = os.listdir(articles_folder)
        return render_template('articles.html', articles=articles_list, title='ARTICLES')

    @app.route('/articles/<filename>')
    def article(filename):
        articles_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'articles')
        file_path = os.path.join(articles_folder, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return render_template('article.html', content=content)
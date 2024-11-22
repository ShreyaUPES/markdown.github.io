from flask import Flask, render_template, request
import markdown

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        markdown_text = request.form["markdown_text"]
        
        # Enable markdown extensions for strikethrough, superscript, subscript
        extensions = ['markdown.extensions.extra', 'markdown.extensions.toc']
        
        # Convert the Markdown to HTML with the given extensions
        html_content = markdown.markdown(markdown_text, extensions=extensions)
        
        return render_template("index.html", html_content=html_content, markdown_text=markdown_text)
    
    return render_template("index.html", html_content=None)

if __name__ == "__main__":
    app.run(debug=True)

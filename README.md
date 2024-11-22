# Markdown to HTML Converter

This project provides a simple web application to convert **Markdown** text into **HTML**. The application uses **Flask** for the backend and renders the result with HTML and CSS for the frontend. The app supports various Markdown features like headers, bold, italic, strikethrough, superscript, and subscript.

**Screenshots**
1- The UI
![image](https://github.com/user-attachments/assets/158df622-d1f3-4aca-a5b6-225c39d4d8a0)

2- The Input
![image](https://github.com/user-attachments/assets/73e8864e-3173-4211-bec0-3718ba305a63)

3- The Output
![image](https://github.com/user-attachments/assets/898e7746-f629-4dc0-b2bb-4ac8e13440f6)


## Features
- Convert Markdown to HTML instantly.
- Support for basic Markdown formatting:
  - Headers (`#`, `##`, `###`, etc.)
  - Bold (`**bold**`)
  - Italic (`*italic*`)
  - Strikethrough (`~~strikethrough~~`)
  - Superscript (`^superscript^`)
  - Subscript (`~subscript~`)
  - Links (`[text](URL)`)
  - Images (`![alt text](image URL)`)
- Clean and modern design with the **Quicksand** font.
- Instructions on how to use Markdown syntax.
- All text rendered in **black** for better readability.

## Demo

![Screenshot of the app](screenshot.png)

You can try out the app by entering your Markdown text in the provided text box and clicking "Convert". The corresponding HTML output will be displayed below.

## Requirements

- Python 3.x
- Flask
- markdown library

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/markdown-to-html-converter.git
    cd markdown-to-html-converter
    ```

2. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Open your browser and go to `http://127.0.0.1:5000` to use the Markdown converter.

## File Structure

The project follows this file structure:

```plaintext
markdown-to-html-converter/
│
├── app.py                    # Main Python file with Flask backend
├── templates/                
│   └── index.html            # HTML template for the frontend
├── static/
│   └── style.css             # CSS for styling the page
└── README.md                 # Project description and setup instructions
```

app.py: Contains the backend logic using Flask to render HTML and handle Markdown to HTML conversion.
templates/index.html: The HTML template that provides the frontend for the app.
static/style.css: The CSS file for styling the page and ensuring a modern, colorful UI.

**How to Use**
Type or paste your Markdown text in the text area.
Click the Convert button.
The HTML output will be displayed below the form.

**Markdown Syntax Guide**
# for headers (e.g., # Header 1 for a large header).
**bold** for bold text.
*italic* for italic text.
~~strikethrough~~ for strikethrough text.
^superscript^ for superscript text.
~subscript~ for subscript text.
1. for ordered lists.
* or - for unordered lists.
[Link Text](URL) for hyperlinks.
![Image](image URL) for images.

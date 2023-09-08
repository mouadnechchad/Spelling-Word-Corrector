from flask import Flask, render_template, request, jsonify
from words_spelling import best_corrections

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        selected_choice = request.form.get("word_choices")
        print(f"User Input: {user_input}")
        print(f"Selected Choice: {selected_choice}")  # Debugging line
        if selected_choice is not None:
            selected_choice = int(selected_choice)  # Convert to an integer
            corrected_text = best_corrections(user_input, selected_choice)
            return jsonify(corrected_text=corrected_text)
    
    # For GET requests, render and return the HTML page
    return render_template("interface2.html")

if __name__ == "__main__":
    app.run(debug=True)

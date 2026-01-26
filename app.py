from flask import Flask, request, render_template

app = Flask(__name__)

# Define the correct major scale (e.g., C major)
CORRECT_SCALE = ["C", "D", "E", "F", "G", "A", "B"]

@app.route("/", methods=["GET", "POST"])
def scales_test():
    if request.method == "POST":
        user_input = request.form.getlist("notes")
        correct_count = sum(1 for note, correct_note in zip(user_input, CORRECT_SCALE) if note == correct_note)
        return f"<h1>You got {correct_count} out of {len(CORRECT_SCALE)} notes correct!</h1>"
    return '''
        <form method="post">
            <p>Enter the notes of the C major scale in order:</p>
            <input type="text" name="notes" placeholder="Note 1">
            <input type="text" name="notes" placeholder="Note 2">
            <input type="text" name="notes" placeholder="Note 3">
            <input type="text" name="notes" placeholder="Note 4">
            <input type="text" name="notes" placeholder="Note 5">
            <input type="text" name="notes" placeholder="Note 6">
            <input type="text" name="notes" placeholder="Note 7">
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, render_template_string, url_for

app = Flask(__name__)

# Define major scales
SCALES = {
    "C Major": ["C", "D", "E", "F", "G", "A", "B"],
    "G Major": ["G", "A", "B", "C", "D", "E", "F#"],
    "D Major": ["D", "E", "F#", "G", "A", "B", "C#"],
    "A Major": ["A", "B", "C#", "D", "E", "F#", "G#"],
    "E Major": ["E", "F#", "G#", "A", "B", "C#", "D#"],
    "B Major": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
    "F# Major": ["F#", "G#", "A#", "B", "C#", "D#", "E#"],
    "C# Major": ["C#", "D#", "E#", "F#", "G#", "A#", "B#"],
    "F Major": ["F", "G", "A", "Bb", "C", "D", "E"],
    "Bb Major": ["Bb", "C", "D", "Eb", "F", "G", "A"],
    "Eb Major": ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
    "Ab Major": ["Ab", "Bb", "C", "Db", "Eb", "F", "G"],
    "Db Major": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"],
    "Gb Major": ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"],
    "Cb Major": ["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb"], 
    # Add more scales as needed
}

@app.route("/", methods=["GET", "POST"])
def scales_test():
    if request.method == "POST":
        selected_scale = request.form.get("scale")
        user_input = request.form.getlist("notes")
        correct_scale = SCALES[selected_scale]
        correct_count = sum(1 for note, correct_note in zip(user_input, correct_scale) if note == correct_note)
        return render_template_string('''
            <h1>You got {{ correct_count }} out of {{ total_notes }} notes correct for the {{ scale }} scale!</h1>
            <a href="/">Try again</a>
        ''', correct_count=correct_count, total_notes=len(correct_scale), scale=selected_scale)

    return render_template_string('''
        <head>
        <title>Scales Test</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
        </head>
        <div class="form-container">
        <h1>Major Scales Test</h1>
        <form method="post">
            <p>Select a scale to try:</p>
            <select name="scale" class="scale-select">
                {% for scale in scales %}
                    <option value="{{ scale }}">{{ scale }}</option>
                {% endfor %}
            </select>
            <p>Enter the notes of the selected scale in order:</p>
            <p>Use "#" for sharps and "b" for flats. All notes need to be uppercase or it will
            not be marked as correct.</p>
            <div class="notes-input">
            {% for i in range(7) %}
                <input type="text" name="notes" placeholder="Note {{ i + 1 }}" required>
            {% endfor %}
            <button type="submit">Submit</button>
            </div>
        </form>
        </div>
    ''', scales=SCALES.keys())

if __name__ == "__main__":
    app.run(debug=True)

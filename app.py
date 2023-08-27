from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    # Preprocess tasks to include both task and index
    processed_tasks = [{'index': index, 'task': task} for index, task in enumerate(tasks)]
    return render_template('index.html', tasks=processed_tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

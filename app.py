from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.id}>"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/todo", methods=["GET", "POST"])
def todo():
    if request.method == "POST":
        task_content = request.form["content"]
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/todo")
        except:
            return "There was an issue adding your task."
    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template("todo.html", tasks=tasks)


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/todo")
    except:
        return "There was a problem deleting that task."


@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    task_to_update = Todo.query.get_or_404(id)
    new_content = request.form["updated_content"]

    try:
        task_to_update.content = new_content
        db.session.commit()
        return redirect("/todo")
    except:
        return "There was a problem updating that task."


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

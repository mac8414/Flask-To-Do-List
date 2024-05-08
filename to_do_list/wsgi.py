from flask import Flask

"""
Simple To Do List using Flask.
Author: M. McKay Hunter
February, 2024
"""

app = Flask(__name__)

@app.route("/")
def to_do_list():
    h1 = "<h1 style='text-align:center; font-size:300%; margin-top: 50px;'> To do list</h1>"
    b1 = """<div id="taskList" style='text-align:center; margin-top: 20px;'>
        <form id="taskForm">
            <label for="task1"></label>
            <input type="checkbox" id="task1Checkbox" name="task1Checkbox" onchange="toggleStrikeThrough('task1Text', this.checked)">
            <input type="text" id="task1Text" name="task1Text" onkeypress="addTaskOnEnter(event, 'task1Text')"><br>
        </form>
    </div>
    <div style="text-align: center;">
        <button onclick="addTask()">Add Task</button>
    </div>

    <script>
        var taskCount = 1;

        function addTaskOnEnter(event, inputId) {
            if (event.keyCode === 13) {
                event.preventDefault();
                var input = document.getElementById(inputId);
                addTask();
                input.focus();
            }
        }

        function addTask() {
            taskCount++;
            var taskList = document.getElementById("taskList");
            var newForm = document.createElement("form");
            newForm.innerHTML = `
                <label for="task${taskCount}"></label>
                <input type="checkbox" id="task${taskCount}Checkbox" name="task${taskCount}Checkbox" onchange="toggleStrikeThrough('task${taskCount}Text', this.checked)">
                <input type="text" id="task${taskCount}Text" name="task${taskCount}Text" onkeypress="addTaskOnEnter(event, 'task${taskCount}Text')"><br>
            `;
            taskList.appendChild(newForm);
        }
        function removeTask(){
        var tasklist = docu
        }
        function toggleStrikeThrough(elementId, isChecked) {
            var element = document.getElementById(elementId);
            if (isChecked) {
                element.style.textDecoration = "line-through";
            } else {
                element.style.textDecoration = "none";
            }
        }
    </script>"""
    return h1 + b1

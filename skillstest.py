from pyscript import document

attendance_records = []

def save_attendance(e):

    name = document.getElementById("name").value.strip()

    day = document.getElementById("day").value

    status = document.getElementById("status").value

    message = document.getElementById("message")

    if not name:

        message.innerHTML = """
        <span style='color:red'>
        Please enter a student name.
        </span>
        """

        return

    attendance_records.append({

        "name": name,
        "day": day,
        "status": status

    })

    message.innerHTML = """
    <span style='color:green'>
    Attendance Saved!
    </span>
    """

    document.getElementById("name").value = ""

    display_records()

def display_records():

    records = document.getElementById("records")

    records.innerHTML = ""

    for student in attendance_records:

        if student["status"] == "Present":
            status_class = "present"

        else:
            status_class = "absent"

        records.innerHTML += f"""

        <div class='record'>

            <div class='student-name'>
                {student["name"]}
            </div>

            <div>
                Day: {student["day"]}
            </div>

            <div class='status {status_class}'>
                {student["status"]}
            </div>

        </div>

        """
from pyscript import document

class Classmate:

    def __init__(self, name, section, subject):

        self.name = name
        self.section = section
        self.subject = subject

    def introduce(self):

        return f"{self.section} • Favorite Subject: {self.subject}"

classmates = [

    Classmate("Alex", "Ruby", "Science"),
    Classmate("Daniella", "Ruby", "Social Studies"),
    Classmate("Sasha", "Ruby", "English"),
    Classmate("Dylan", "Ruby", "Science"),
    Classmate("Tristan", "Ruby", "Science")

]

def add_classmate(e):

    name = document.getElementById("name").value.strip()

    section = document.getElementById("section").value.strip()

    subject = document.getElementById("subject").value.strip()

    message = document.getElementById("message")

    if not name or not section or not subject:

        message.innerHTML = """
        <span style='color:red'>
        Fill all fields.
        </span>
        """

        return

    classmates.append(
        Classmate(name, section, subject)
    )

    message.innerHTML = """
    <span style='color:green'>
    Classmate Added!
    </span>
    """

    document.getElementById("name").value = ""
    document.getElementById("section").value = ""
    document.getElementById("subject").value = ""

    show_classmates(None)

def delete_classmate(e):

    index = int(
        e.target.getAttribute("data-index")
    )

    classmates.pop(index)

    show_classmates(None)

def show_classmates(e):

    output = document.getElementById("output")

    output.innerHTML = ""

    for i, s in enumerate(classmates):

        output.innerHTML += f"""

        <div class='list-item'>

            <div>

                <div class='student-name'>
                    {s.name}
                </div>

                <div class='student-info'>
                    {s.introduce()}
                </div>

            </div>

            <button class='delete-btn'
            py-click='delete_classmate'
            data-index='{i}'>
            ✖
            </button>

        </div>

        """

def search_classmates(e):

    keyword = document.getElementById("search").value.lower()

    output = document.getElementById("output")

    output.innerHTML = ""

    for i, s in enumerate(classmates):

        if keyword in s.name.lower():

            output.innerHTML += f"""

            <div class='list-item'>

                <div>

                    <div class='student-name'>
                        {s.name}
                    </div>

                    <div class='student-info'>
                        {s.introduce()}
                    </div>

                </div>

                <button class='delete-btn'
                py-click='delete_classmate'
                data-index='{i}'>
                ✖
                </button>

            </div>

            """

show_classmates(None)
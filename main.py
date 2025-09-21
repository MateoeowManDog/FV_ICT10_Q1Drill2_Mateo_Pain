from pyscript import document

def generate_message(event):
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    message = f"""
🎓 Student Profile
Name   : {name}
Age    : {age}
School : {school}
Notes:
{name} is {age} years old and studies at {school}.
    """
    output = document.getElementById("output")
    output.innerText = message.strip()

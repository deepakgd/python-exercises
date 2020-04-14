first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"
print("old method")
print("Hello, %s %s. You are %s. You are a %s. You were a member of %s." % (first_name, last_name, age, profession, affiliation))
#'Hello, Eric Idle. You are 74. You are a comedian. You were a member of Monty Python.'

print("new method")
print(f"Hello, {first_name} {last_name}.  You are {age}. You are a {profession}. You were a member of {affiliation}.")

print(F"Hello, {first_name}. You are {age}.")
print(f"{2 * 37}")
print(f"{first_name.lower()} is funny.")

message = (
    f"Hi {first_name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
)
print(message)

message = f"""
     Hi {first_name}. 
     You are a {profession}. 
     You were in {affiliation}.
 """

print(message)

# Ref - https://realpython.com/python-f-strings/
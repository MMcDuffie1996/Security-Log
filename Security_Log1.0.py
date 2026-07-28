import json #this will load Python's built-in Json module so that I can convert dictionaries into Json strings later
from datetime import datetime, timezone #this will pull the date and time class and timezone class directly out of the datetime module, so that I can call upon datetime.now(timezone.utc) without extra prefixes


#validation Tuples
valid_outcome = "Success", "Failure", "Denied"
valid_status = "Active", "Inactive", "Retired"
valid_roles = "admin", "specialist","guest"
valid_priority = "Info","Warning","Critical", "Error"
#Each of these creates a tuple (comma-separated values with no brackets still makes a tuple in Python).
#These act as "allow lists" — later code checks whether a given value is in one of these tuples to validate input.

#Class Definition/Blueprint
#Defines a blueprint called SecurityRecords. Every time you create one, it will have the structure defined inside.
class SecurityRecords:
    def __init__(self, username, email, status, roles, action, outcome, priority):#__init__ runs automatically whenever you create a new SecurityRecords object. self refers to this specific instance being built. The rest are the parameters you must supply — username, email, status, roles, action, outcome, priority.
        if status not in valid_status:#these are validation checks
            raise ValueError(f"Invalid status: {status}")#Checks if the status argument passed in is one of ("Active", "Inactive", "Retired"). If it's not, the program stops immediately and raises a ValueError with a message showing exactly what invalid value was given.
        if roles not in valid_roles:#Same idea — checks roles against ("admin", "specialist", "guest"). This is correctly using roles consistently now (the mismatch from before is fixed).
            raise ValueError(f"Invalid role: {roles}")
        if outcome not in valid_outcome:
            raise ValueError(f"Invalid outcome: {valid_outcome}")
        if priority not in valid_priority:#Checks priority against the allowed tuple — correct, and correctly references priority in the message
            raise ValueError(f"Invalid priority: {priority}")
#In otherwords, def function serves as a form of construction worker on the blueprint
        #Assigning (=) selfs not comparing
#Assigning values to the object
#Each line stores the incoming argument onto the object itself (self.___), so it can be accessed later (e.g., record.username). This is = (assignment), not == (comparison) — correct usage.
        self.username = username
        self.email = email
        self.status = status
        self.roles = roles
        self.action = action
        self.outcome = outcome
        self.priority = priority
        self.timestamp = datetime.now(timezone.utc).isoformat()
#Automatically generates the current UTC time the moment the object is created, and converts it into a standard ISO 8601 string format (like "2026-07-27T18:42:03.912481+00:00").
    #Builds and returns a regular Python dictionary containing all the stored fields below
    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "username": self.username,
            "email": self.email,
            "status": self.status,
            "roles": self.roles,
            "action": self.action,
            "outcome": self.outcome,
            "priority": self.priority
            }
#converting back to Json
    def to_json(self):
        return json.dumps(self.to_dict())
#Calls to_dict() to get the dictionary, then uses json.dumps() to turn it into a JSON-formatted string
#The usage    
record = SecurityRecords(
    username="jdoe",
    email="jdoe@example.com",
    status="Active",
    roles="admin",
    action="login",
    outcome="Failure",
    priority="Warning" 
)#This creates a real SecurityRecords object, automatically running __init__. Each value gets checked against the valid tuples: "Active", "admin", "Failure", "Warning"

print(f"The following information is a log in the last hour")#Prints a static message. The f prefix is unnecessary since there's no {variable} inside
print(record.to_json())#Calls to_json() on your record object, converting it to a JSON string, and prints it

class Supervisor:
    def __init__(self, supervisor_id, first_name, last_name, email, department):
        self.supervisor_id = supervisor_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.department = department

    def __str__(self):
        return f"Supervisor [ID: {self.supervisor_id}] - Prof. {self.first_name} {self.last_name} ({self.department})"
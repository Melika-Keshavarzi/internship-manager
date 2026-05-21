class Activity:
    def __init__(self, activity_id, activity_type, title, topic, start_date, end_date, status, student, supervisor):
        self.activity_id = activity_id
        self.activity_type = activity_type
        self.title = title
        self.topic = topic
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.student = student
        self.supervisor = supervisor

    def __str__(self):
        return (f"Activity [ID: {self.activity_id}] ({self.activity_type.upper()})\n"
                f"Title: {self.title}\n"
                f"Status: {self.status.upper()}\n"
                f"Assigned to: {self.student.get_full_name()} (ID: {self.student.student_id})\n"
                f"Supervised by: Prof. {self.supervisor.last_name}")
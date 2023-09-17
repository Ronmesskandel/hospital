import random
import string

class HospitalETicketSystem:
    def __init__(self):
        self.tickets = {}

    def generate_ticket(self, patient_name, doctor_name, appointment_date, appointment_time):
        ticket_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        self.tickets[ticket_id] = {
            "patient_name": patient_name,
            "doctor_name": doctor_name,
            "appointment_date": appointment_date,
            "appointment_time": appointment_time
        }
        return ticket_id

    def get_ticket_info(self, ticket_id):
        if ticket_id not in self.tickets:
            return None
        return self.tickets[ticket_id]

    def cancel_ticket(self, ticket_id):
        if ticket_id not in self.tickets:
            return None
        del self.tickets[ticket_id]

if __name__ == "__main__":
    system = HospitalETicketSystem()

    # Generate a ticket
    ticket_id = system.generate_ticket("John Doe", "Dr. Smith", "2023-09-16", "10:00 AM")

    # Get ticket info
    ticket_info = system.get_ticket_info(ticket_id)
    print(ticket_info)

    # Cancel ticket
    system.cancel_ticket(ticket_id)

    # Get ticket info again
    ticket_info = system.get_ticket_info(ticket_id)
    print(ticket_info)
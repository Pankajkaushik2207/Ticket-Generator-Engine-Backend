import mysql.connector
from random import sample

# Step 1: Set Up Database Connection
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pankaj34@",  # Replace with your MySQL password
        database="tambola"
    )

# Step 2: Generate Tambola Tickets
def generate_tickets(num_sets):
    conn = connect_to_database()
    cursor = conn.cursor()

    tickets = {}
    for set_id in range(11, 11 + num_sets):
        ticket_list = []
        for ticket_id in range(1, 7):
            numbers = sample(range(1, 91), 15)
            ticket_list.append(numbers)

            # Insert ticket into the database
            cursor.execute(
                "INSERT INTO tambola_tickets (set_id, ticket_id, numbers) VALUES (%s, %s, %s)",
                (set_id, ticket_id, str(numbers))
            )
            conn.commit()

        tickets[str(set_id)] = ticket_list

    cursor.close()
    conn.close()

    return tickets

# Main Program
if __name__ == "__main__":
    num_sets = int(input("Enter the number of sets to generate: "))
    new_tickets = generate_tickets(num_sets)

    print("Newly created tickets:")
    print(new_tickets)

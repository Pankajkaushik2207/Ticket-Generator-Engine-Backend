CREATE DATABASE tambola;


USE tambola;
CREATE TABLE tambola_tickets (
    set_id INT,
    ticket_id INT,
    numbers TEXT,
    PRIMARY KEY (set_id, ticket_id)
);
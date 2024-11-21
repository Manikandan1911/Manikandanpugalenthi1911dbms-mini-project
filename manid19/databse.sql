CREATE DATABASE bus_ticket_bookings1;
USE bus_ticket_booking1;

-- Table for storing bus information
CREATE TABLE buses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),        -- Bus name or title
    description TEXT,         -- Description of the bus
    image_url VARCHAR(255),   -- Bus image URL
    rating DECIMAL(3,2)       -- Average bus rating
);

-- Table for storing user bookings
CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bus_id INT,                           -- Reference to the bus
    user_name VARCHAR(255),               -- Name of the user
    email VARCHAR(255),                   -- User email
    phone VARCHAR(15),                    -- User phone number
    seats VARCHAR(255),                   -- Seats booked
    departure_station VARCHAR(255),       -- Departure location
    destination_station VARCHAR(255),     -- Destination location
    booking_time DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Time of booking
    FOREIGN KEY (bus_id) REFERENCES buses(id)         -- Foreign key constraint
);

-- Inserting sample buses into the 'buses' table
INSERT INTO buses (name, description, image_url, rating) VALUES
('MURAHARA', 'Fast and comfortable inter-city bus service.', 'city_express.jpg', 4.5),
('TRANS GHOST', 'Experience scenic routes with our mountain trail buses.', 'mountain_trail.jpg', 4.8),
('LUXURY CRUSIER', 'Premium travel with luxury seating and amenities.', 'luxury_line.jpg', 4.9),
('GALAXY', 'Affordable travel for everyone.', 'budget_rider.jpg', 3.7),
('NIGHT RIPPER', 'Overnight travel with sleeping arrangements.', 'night_owl.jpg', 4.2),
('KALLADA', 'Quick shuttle services for daily commuters.', 'express_shuttle.jpg', 4.0),
('Coastal Cruiser', 'Travel along coastal routes with picturesque views.', 'coastal_cruiser.jpg', 4.6),
('VOLVO CRUSIER', 'Get closer to nature with our safari buses.', 'safari_connect.jpg', 4.3),
('ONENESS JET', 'Connecting city centers with convenience.', 'metro_mover.jpg', 4.4),
('TAMIL CRUSIER', 'Enjoy the calm countryside during your travel.', 'countryside_comfort.jpg', 4.1);

-- Inserting sample bookings into the 'bookings' table
INSERT INTO bookings (bus_id, user_name, email, phone, seats, departure_station, destination_station) VALUES
(1, 'Hari', 'hari.velu@gmail.com', '123-456-7890', 'A1, A2', 'Netherland', 'Kerala'),
(2, 'Sakthivel', 'sakthivel@gmail.com', '234-567-8901', 'B3, B4', 'Erode', 'Hosur'),
(3, 'Ezhil', 'ezhil@gmail.com', '345-678-9012', 'C5, C6', 'Kerala', 'Mysore'),
(4, 'Bob Brown', '@gmail.com', '456-789-0123', 'D7, D8', 'Mysore', 'Delhi'),
(5, 'Charles', 'charles@gmail.com', '567-890-1234', 'E9, E10', 'Kollam', 'Dharamashala'),
(6, 'Dave', 'dave@gmail.com', '678-901-2345', 'F11, F12', 'Mysore', 'Goa'),
(7, 'Kowsik', 'Kowsik@gmail.com', '789-012-3456', 'G13, G14', 'Delhi', 'Solaphur'),
(8, 'Guru', 'guru@gmail.com', '890-123-4567', 'H15, H16', 'Chennai', 'Hyderabad'),
(9, 'Dharma', 'Dharma@gmail.com', '901-234-5678', 'I17, I18', 'Hyderabad', 'Banglore'),
(10, 'Tamil', 'Tamil@gmail.com', '012-345-6789', 'J19, J20', 'Kerala', 'Banglore');

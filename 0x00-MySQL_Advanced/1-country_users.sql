-- Create the 'users' table if it does not already exist
CREATE TABLE IF NOT EXISTS users (
    -- 'id' column: An integer that cannot be NULL and auto-increments for each new record
    id INT NOT NULL AUTO_INCREMENT,
    
    -- 'email' column: A string up to 255 characters, must be unique and cannot be NULL
    email VARCHAR(255) NOT NULL UNIQUE,
    
    -- 'name' column: A string up to 255 characters, can be NULL
    name VARCHAR(255),


    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    
    -- Set 'id' as the primary key for the table
    PRIMARY KEY (id)
);






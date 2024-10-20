-- Creates a trigger that decreases the quantity
-- of an item after adding a new order.
 -- Only reset valid_email if the email has changed
DROP trigger IF EXISTS reset_valid_email;
CREATE trigger  reset_valid_email;
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
   
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
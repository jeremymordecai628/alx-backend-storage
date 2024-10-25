-- SafeDiv function
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
  -- Return 0 if divisor is zero, otherwise return the division
  IF b = 0 THEN
    RETURN 0;
  ELSE
    RETURN a / b;
  END IF;
END $$

DELIMITER ;

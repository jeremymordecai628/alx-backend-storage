-- AddBonus procedure to add a correction
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
  DECLARE project_id INT;

  -- Check if the project exists, if not, create it
  SET @existing_project = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
  IF @existing_project IS NULL THEN
    INSERT INTO projects (name) VALUES (project_name);
    SET project_id = LAST_INSERT_ID();
  ELSE
    SET project_id = @existing_project;
  END IF;

  -- Insert the correction
  INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END $$

DELIMITER ;

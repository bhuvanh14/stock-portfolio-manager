CREATE TRIGGER default_settings_for_user
AFTER INSERT ON Users
FOR EACH ROW
BEGIN
    INSERT INTO Settings (user_id, email_notifications, sms_notifications)
    VALUES (NEW.user_id, TRUE, FALSE);
END;

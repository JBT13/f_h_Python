BEGIN;
CREATE OR REPLACE FUNCTION NewAthlete(
    IN aname VARCHAR(50),
    IN agender CHAR(2),
    IN aheight FLOAT
)
RETURNS INTEGER
AS $$
BEGIN
  INSERT INTO Athletes (name, gender, height)
  VALUES (aname, agender, aheight);
  RETURN lastval();
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

BEGIN;
CREATE OR REPLACE FUNCTION NewCompetition(
    IN aplace VARCHAR(50),
    IN aheld DATE
)
RETURNS INTEGER
AS $$
BEGIN
  INSERT INTO Competitions (place, held)
  VALUES (aplace, aheld);
  RETURN lastval();
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;



-- SECURITY DEFINER allows execute privileges to public, which is too open for most cases, so we revoke this instantly
REVOKE ALL ON FUNCTION NewAthlete FROM public;
GRANT EXECUTE ON FUNCTION NewAthlete TO editor;
GRANT ALL ON FUNCTION NewAthlete TO theone;
GRANT ALL ON FUNCTION NewCompetition TO viewer;
END;

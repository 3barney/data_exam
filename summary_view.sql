CREATE OR REPLACE VIEW public."Records Summary"
 AS
SELECT minimum, maximum, average, median, date
FROM records_summary;

ALTER TABLE public."Records Summary"
    OWNER TO gepp_user;
SELECT species_name , experiment_id, CAST(is_predator as BOOLEAN)
, (CASE WHEN is_predator = 't' THEN score * 1.2 
WHEN is_predator = 'f' THEN score * 1 END ) AS score
FROM experiment AS ex
JOIN subject AS sb USING(subject_id)
JOIN species AS sp USING(species_id)
ORDER BY score DESC; 
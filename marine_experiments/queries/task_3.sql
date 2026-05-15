SELECT ext.type_name , sp.species_name , 
ROUND(AVG(ex.score),2) AS average_score
FROM experiment AS ex
JOIN experiment_type AS ext USING(experiment_type_id)
JOIN subject AS sb USING(subject_id)
JOIN species AS sp ON(sb.species_id = sp.species_id)
GROUP BY ext.type_name, sp.species_name 
HAVING AVG(ex.score) > 5
ORDER BY average_score DESC;

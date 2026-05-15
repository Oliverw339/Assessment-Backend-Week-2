SELECT ex.experiment_id, sb.subject_id , sp.species_name AS species
    , ex.experiment_date, ext.type_name as experiment_type
    , CONCAT(cast(ROUND((ex.score * 100 / MAX(ex.score) OVER(PARTITION BY ext.type_name)),2) AS varchar) , '%') as score
FROM experiment AS ex
JOIN subject AS sb USING(subject_id)
JOIN experiment_type AS ext USING(experiment_type_id)
JOIN species AS sp ON(sb.species_id = sp.species_id)
ORDER BY ex.experiment_date DESC;

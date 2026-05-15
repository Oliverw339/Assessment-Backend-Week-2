SELECT  sb.subject_id , sb.subject_name , sp.species_name , 

CONCAT(cast(EXTRACT(YEAR FROM sb.date_of_birth) as varchar) , '-' ,
cast(EXTRACT(MONTH FROM sb.date_of_birth) as varchar)) AS date_of_birth 

FROM subject AS sb
JOIN species AS sp ON(sb.species_id = sp.species_id)
ORDER BY date_of_birth DESC;

-- Task: Rank country origins of bands, ordered by the number of non-unique fans
-- This query ranks the origins of bands by the total number of fans, in descending order

SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

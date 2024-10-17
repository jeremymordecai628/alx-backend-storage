-- List all bands with Glam rock as their main style, ranked by longevity

SELECT 
    name AS band_name,
    CASE
        WHEN split IS NULL THEN 2022 - formed
        ELSE split - formed
    END AS lifespan
FROM 
    bands
WHERE 
    style = 'Glam rock'
ORDER BY 
    lifespan DESC;

-- calling a CTE to make the table name actually readable

WITH data AS (
SELECT 
  * 
FROM 
  `chess-371023.chessPuzzles.puzzlesClean`
)

SELECT
  week,
  year,
  theme,
  SUM(score) AS score,
  COUNT(*) AS puzzles,
  ROUND(SUM(score)/COUNT(*)*100,2) AS pct
FROM 
  data
GROUP BY
  week,
  year,
  theme
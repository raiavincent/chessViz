SELECT
  puzzleID,
  date,
  theme,
  score,
  EXTRACT(year FROM date) AS year,
  EXTRACT(month FROM date) AS month,
  EXTRACT(week FROM date) AS week,
  CONCAT(EXTRACT(year FROM date),"-",EXTRACT(month FROM date)) AS dateCode,
  CONCAT(EXTRACT(week FROM date),"-",EXTRACT(month FROM date)) AS weekCode
FROM 
  `chess-371023.chessPuzzles.puzzleHistory`
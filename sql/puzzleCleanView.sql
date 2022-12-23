SELECT
  puzzleID,
  date,
  theme,
  score,
  EXTRACT(year FROM date) AS year,
  EXTRACT(month FROM date) AS month,
  CONCAT(EXTRACT(year FROM date),"-",EXTRACT(month FROM date)) AS dateCode
FROM 
  `chess-371023.chessPuzzles.puzzleHistory`
SELECT R.result FROM (
SELECT A.row_num AS i, B.col_num AS j, SUM(A.value * B.value) AS result
FROM A, B
WHERE A.col_num = B.row_num
GROUP BY a.row_num, B.col_num
) R
WHERE R.i=2 AND R.j=3;


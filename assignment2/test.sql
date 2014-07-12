--SELECT * FROM frequency
--WHERE docid='9795_txt_trade';

CREATE VIEW search_view AS
    SELECT * FROM frequency
    UNION
    SELECT 'q' AS docid, 'washington' AS term, 1 AS count
    UNION
    SELECT 'q' AS docid, 'taxes' AS term, 1 AS count
    UNION
    SELECT 'q' AS docid, 'treasury' AS term, 1 AS count;

SELECT R.docid1, R.docid2, sum(result) AS sim FROM (
SELECT f1.docid AS docid1, f1.term AS term1,f1.count, f2.docid AS docid2, f2.term AS term2, f2.count, (f1.count * f2.count) AS result
FROM search_view f1, search_view f2
WHERE f1.term = f2.term
AND f1.docid = 'q' AND f2.docid != 'q'
GROUP BY f2.docid
ORDER BY f2.docid, result DESC
) R
GROUP BY docid2
ORDER BY sim DESC
LIMIT 10;

CREATE VIEW search_view AS 
    SELECT * FROM frequency
    UNION
    SELECT 'q' AS docid, 'washington' AS term, 1 AS count
    UNION
    SELECT 'q' AS docid, 'taxes' AS term, 1 AS count
    UNION
    SELECT 'q' AS docid, 'treasury' AS term, 1 AS count;

SELECT sum(result) AS sim FROM (
SELECT f1.docid AS docid1, f1.term AS term1,f1.count, f2.docid AS docid2, f2.term AS term2, f2.count, (f1.count * f2.count) AS result
FROM search_view f1, search_view f2
WHERE f1.term = f2.term
AND f1.docid = 'q' AND f2.docid != 'q'
GROUP BY f2.docid
ORDER BY f2.docid, result DESC
) R
GROUP BY docid2
ORDER BY sim DESC
LIMIT 1;


--SELECT R.term2, sum(R.result) AS similarity FROM (
--SELECT f1.docid, f1.term AS term1, f1.count, f2.docid AS simDocId, f2.term AS term2, f2.count, (f1.count * f2.count) AS result
--FROM search_view f1, search_view f2
--WHERE f1.term = f2.term
--AND f1.docid = 'q' AND f2.docid != 'q'
--GROUP BY f2.docid, f2.term
--) R
--GROUP BY R.term2
--ORDER BY similarity DESC
--LIMIT 100;


SELECT sum(result) FROM (
SELECT f1.term AS term1,f1.count, f2.term AS term2, f2.count, (f1.count * f2.count) AS result
FROM frequency f1, frequency f2
WHERE f1.term = f2.term
AND f1.docid < f2.docid
AND f1.docid = '10080_txt_crude' AND f2.docid = '17035_txt_earn'
GROUP BY f1.term, f2.term
) R;


SELECT COUNT(*) FROM (
SELECT DISTINCT * FROM frequency f1, frequency f2
WHERE f1.docid=f2.docid AND
f1.term='transactions' AND f2.term='world'
);



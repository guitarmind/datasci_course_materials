SELECT COUNT(*) FROM (
SELECT docid, sum(count) AS term_count FROM frequency
GROUP BY docid
HAVING term_count > 300
ORDER BY docid ASC
);



SELECT
    CONCAT(CEIL(MONTH(DIFFERENTIATION_DATE) / 3), 'Q') QUARTER,
    COUNT(ID) ECOLI_COUNT
FROM
    ECOLI_DATA
GROUP BY
    QUARTER
ORDER BY
    QUARTER

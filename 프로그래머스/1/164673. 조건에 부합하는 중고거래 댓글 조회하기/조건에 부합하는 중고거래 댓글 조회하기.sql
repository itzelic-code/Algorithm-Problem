SELECT 
    b.TITLE,
    b.BOARD_ID,
    r.REPLY_ID,
    r.WRITER_ID,
    r.CONTENTS,
    DATE_FORMAT(r.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM 
    USED_GOODS_BOARD b
JOIN 
    USED_GOODS_REPLY r ON b.BOARD_ID = r.BOARD_ID
WHERE 
    YEAR(b.CREATED_DATE) = 2022 AND MONTH(b.CREATED_DATE) = 10
ORDER BY 
    r.CREATED_DATE ASC, 
    b.TITLE ASC;
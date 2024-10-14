SELECT
	ANIMAL_TYPE,
	COALESCE(NAME, 'No name') AS NAME,
	SEX_UPON_INTAKE
FROM
	ANIMAL_INS
ORDER BY
	ANIMAL_ID ASC;
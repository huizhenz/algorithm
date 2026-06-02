-- 코드를 작성해주세요
SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 2) = 0 AND (GENOTYPE & 5) > 0;
# SQL 문법 + 연산자 우선순위 기반 수정
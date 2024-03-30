--- Link query GCP :
https://console.cloud.google.com/bigquery?sq=42932859399:46bfae07a7a64141938e4f0618c0d2e4

--- eksplorasi(1)
SELECT AVG(mentor_satisfaction_score) AS rata_rata_kepuasan_mentor
FROM `task12-eksplorasi.dataset1.survey` ;

--- eksplorasi(2)
SELECT AVG(cs_satisfaction_score) AS rata_rata_kepuasan_cs 
FROM `task12-eksplorasi.dataset1.survey` ;

--- eksplorasi(3)
SELECT AVG(mentor_satisfaction_score) AS rata_rata_kepuasan_mentor_courseA
FROM `task12-eksplorasi.dataset1.survey`
WHERE course_name='Course A';

---eksplorasi(4)
SELECT MIN(learning_satisfaction_score) AS score_terendah
FROM `task12-eksplorasi.dataset1.survey`
WHERE course_name='Course C';

---eksplorasi(5)
SELECT MAX(cs_satisfaction_score) AS score_max
FROM `task12-eksplorasi.dataset1.survey`
WHERE course_name='Course B';

---eksplorasi(6)
SELECT course_name 
FROM `task12-eksplorasi.dataset1.survey`
GROUP BY course_name
ORDER BY AVG(mentor_satisfaction_score) DESC
LIMIT 1;

---eksplorasi(7)
SELECT course_name 
FROM `task12-eksplorasi.dataset1.survey`
GROUP BY course_name
ORDER BY AVG(learning_satisfaction_score) DESC
LIMIT 1;
SELECT a.APNT_NO,p.PT_NAME,p.PT_NO, a.MCDP_CD, d.DR_NAME,a.APNT_YMD 
FROM APPOINTMENT a JOIN PATIENT p ON a.PT_NO = p.PT_NO
JOIN DOCTOR d ON a.MDDR_ID = d.DR_ID
WHERE a.MCDP_CD = 'CS' AND a.APNT_CNCL_YN = 'N' AND LEFT(a.APNT_YMD,10) = '2022-04-13' 
ORDER BY 6
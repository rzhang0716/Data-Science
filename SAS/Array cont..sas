/*Array continues*/

proc import datafile = "/folders/myfolders/score_data_miss999" 
DBMS = xlsx out = scoredata0 replace ;
run;

data scoredata1;
set scoredata0;
   ARRAY old (3) score1 score2 score3;    
   ARRAY new (3) score1n score2n score3n; 
   DO i = 1 TO 3;                       
      IF old(i) = 999 THEN new(i) =.;   
      Else if old(i) NE 999 then new(i) = old(i);
   END;  
/* when i = 1:
IF old(1) = 999 THEN new(1) =.;   
      Else if old(1) NE 999 then new(1) = old(1);

SAME AS
IF score1 = 999 THEN score1n =.;   
      Else if score1 NE 999 then score1n = score1;
*/

drop i;
run;

PROC PRINT data = scoredata1;
title "missing values converted from 999 to .";
run;
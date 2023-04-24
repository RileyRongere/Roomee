DROP TABLE IF EXISTS USER;

CREATE TABLE IF NOT EXISTS USER (
   UserID      int(11)  NOT NULL AUTO_INCREMENT                    ,
   UserName    char(12) NOT NULL                                   ,
   Passcode    char(30) NOT NULL                                   ,
   FirstName   char(25) NOT NULL                                   ,
   LastName    char(25) NOT NULL                                   ,
   Gender      int      NOT NULL                                   ,
               CONSTRAINT CHECK (GENDER IN (0,1))                  ,
               CONSTRAINT PRIMARY KEY (UserID)                                 
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS QUESTION (
   QuestionID    int(11) NOT NULL AUTO_INCREMENT                   ,
   Question      char(200) NOT NULL                                ,
               PRIMARY KEY (QuestionID)                             
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS ANSWER (
   AnswerID      int(11)  NOT NULL AUTO_INCREMENT                  ,
   QuestionID    int(11)  NOT NULL REFERENCES QUESTION(QuestionID) ,
   UserID        int(11)  NOT NULL REFERENCES USER(UserID)         ,
   Answer        int(1)   NOT NULL                                 ,
               CONSTRAINT CHECK (Answer >= 0 AND Answer <= 5)      ,
               CONSTRAINT PRIMARY KEY (AnswerID)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS MATCHES (
   MatchID      int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY          ,
   User_1       int(11) NOT NULL REFERENCES USER(UserID)             ,
   User_2       int(11) NOT NULL REFERENCES USER(UserID)             ,
   PercentMatch float(2) NOT NULL                                      
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;


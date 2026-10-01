# Student Result Analyzer
hindi=int(input("enter the marks of hindi:"))
english=int(input("enter the marks of english:"))
maths=int(input("enter the marks of maths:"))
science=int(input("enter the marks of science:"))
social_science=int(input("enter the marks of social science:"))
marks=hindi+english+maths+science+social_science
total=500

if marks>280:
 if marks>=480 and marks<=500:
    print(f"Marks:{marks} grade=A+\nremarks:outstanding")
 elif marks>=400 and marks<480:
    print(f"Marks:{marks} grade=A\nremarks:excellent")
 elif marks>=380 and marks<400:
    print(f"Marks:{marks} grade=B+\nremarks:very good")
 elif marks>=350 and marks<380:
    print(f"Marks:{marks} grade=B\nremarks:good")
 elif marks>=300 and marks<350:
    print(f"Marks:{marks} grade=C\nremarks:Satisfactory")
else:
   print(f"marks:{marks} fail,repeat the class again")

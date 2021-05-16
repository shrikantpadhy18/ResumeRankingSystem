<h1>CV ANALYSIS AND RANKING SYSTEM </h1>
<hr>

<h1>About This Project</h1>
This Project has three Componenents viz<br>
1)Candidate: Candidate can create their profile in this system and upload their CV. They can see the ongoing drives.
<br>
2)Company: Company can enter into the system by creating their own credentials. They can post job description tag as per their job requirements. After hitting the ranking button the rank of candidate will get generated. The candidates with percentage lesser than 50% will recieved a rejection mail describing of why they got rejected.
<br>
3)Algorithm: Algorithm Used Here is (TFIDF+BOW),that runs over all the CV's present in the system and produces their respective TFIDF score with respect to the job tags made by the company. The CV's uploaded by the candidate will remain in one single folder. The database mysql will contain the mapping of candidates email,CV,location of CV etc.

<hr>
<h1>Working Of Algorithm</h1>
Step 1: Calculate TF (Term Frequency) Term Frequency (TF) - Number of times a keyword
appeared in a document is calculated by Term Frequency. TF (‘keyword’) =number of times
‘keyword’ appears in document /Total number of keywords in the document. Here, the term
‘keyword’ signifies any job specific skill which the algorithm is searching for.<br>
Step 2: Calculate IDF (Inverse Document Frequency) value. The problem of rare and
frequent words is resolved. This helps our system to give more priority to the required word
or skills.
IDF sets the log value=1 for the required CV as per skill sets and log value=0 for the
unwanted CV. IDF (‘keyword’) =log (total number of CV/Number of document with term
‘keyword’)<br>
Step 3: Calculate TF-IDF weight Weight= TF (‘keyword’)*IDF (‘keyword’) Higher the
weight, more relevant is the CV and lower the weight, less or no relevance of the CV for the
selection process [9].
This step returns the CV with highest and lowest weight values which is further useful for
classification [9]. The system determines the candidate on the score obtained. The highfrequency of some keywords may impact on candidate overall score. TF -IDF is widely used
in text mining techniques [10].
The algorithm takes into account the effect of high-frequency keywords and negates the
lowfrequency keywords
<br>
<h1>Software Required</h1>
FRAMEWORK:DJANGO<BR>
DATABASE:MYSQL<br>
MACHINE LEARNING LIBRARY:SKLEARN<br>



<hr>
<h1>Steps for Installation</h1>
1)Clone The Repository to your system.<br>
2)Make Sure Python is installed. Install  Django,its required modules. Install Mysql driver( have attached mysql wheel using which driver can be installed based on system architecture 32 bit or 64 bit).<br>
3)After all this installation run this two commands.<br>
    -a)python manage.py makemigrations
    -b)python manage.py migrate
4)Start the server by using below command
    python manage.py runserver
<hr>

<h1>Result</h1>
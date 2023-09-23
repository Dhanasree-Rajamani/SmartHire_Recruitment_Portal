<p align="center">
  <img width="300" alt="smarthire-logo" src="https://github.com/Dhanasree-Rajamani/SmartHire_Recruitment_Portal/assets/111466424/3863b308-de03-4cac-8f69-3de6cc7fe8fc">
</p>

SmartHire is an all-in-one solution for enterprise recruitment, streamlining the process and reducing costs by automating candidate shortlisting and interview scheduling. It also offers skill-based candidate scoring for efficient candidate selection.

## Problems with Recruitment process
Recruitment is a tedious process that enterprise organizations have to go through to acquire the right talent. The process of recruitment takes a lot of effort, time and cost for the organization with the below mentioned concerns

1. Shortlisting the right profiles from a wide pool of applicants without right qualifications
2. Scheduling interviews according to the interviewer and the candidates convenience
3. To figure out how appropriate is the candidate for the role that he/she has applied for

## Why SmartHire?
SmartHire is the solution for enterprise organizations to make the recruitment process efficient and effective by automating the functionalities involved in recruitment. It is a one-stop solution where shortlisting the candidates and scheduling the interviews with the candidates can be done easily with a single tool.

It eliminates the need for a third party organization, therefore reducing cost. It is a user-friendly tool for the recruiters to view, shortlist, interview, provide feedback and select/reject the candidate, while ensuring that the data is secure(Access to confidential data is role based).

We provide the organization with a feature of scoring the profiles of the candidates based on their skillset and their work experience on that particular skill which makes it easier to shortlist the right candidates from the large pool of candidates.

## System Architecture
<img width="655" alt="Screenshot 2023-09-23 at 11 08 11 AM" src="https://github.com/Dhanasree-Rajamani/SmartHire_Recruitment_Portal/assets/111466424/cfa0d132-f381-4547-acdc-afad7a65d4a2">

## Technologies/Frameworks Used
- **Flask** : It is python microframework used to develop the web application. We have used packages like flask_login, flask_wtf for login management and handling Form requests.

- **MySQL** : MySQL relational database is used to store the applicant data parsed from the resumes into the candidate table. Some of the tables used in MySQL are tbl_employees, tbl_candidate_resume, tbl_open_roles, tbl_shortlisted_candidates etc.

- **Python** : Parsing the resumes and obtaining the candidate details is done using a python library pyreparser. Other functionalities such as shortlisting candidates, assigning a relevancy score, scheduling interviews for candidates with relevant interviewers are also done with Python. 

- **Amazon S3** : S3 holds all the resumes of candidates that have applied for the open roles.

- **AWS** : The application has been hosted on AWS EC2.

- **HTML,CSS & Javascript** : Used to develop the web pages and adding several styles using bootstrap CSS.

- **NLTK** : Natural Language Toolkit is a python package used in the pyreparser package for parsing resumes.

More info: [SmartHire ReadMe](https://github.com/Dhanasree-Rajamani/SmartHire_Recruitment_Portal/blob/main/SmartHire1/SmartHire%20ReadMe.pdf)

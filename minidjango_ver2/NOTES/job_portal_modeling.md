# PRIMARY KEY <--> FOREIGN KEY
- Foreign key is a constraint used to establish relationship between 2 tables
- It's a field in one table that refers to a primary key from another table

# Portal 
- name 
- description

# JobTitle
(JobTitle will have association with multiple portals)

- title
- last_updated
- portal (FK)

# JobDescription
- role
- description_text
- pub_date

# Applicant
- job_description (FK)
- cover_letter
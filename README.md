# HIRED-PhD: Highly Informative Repository of Employment Data for PhDs

This is a way to collect and store placement data for PhD students by institution, discipline, and research group. Use of this information will aid current and prospective grad students in their career planning endeavors.

## Entity Tables
### university_info
The university_info table is adapted from the US Accreditation Files available here: http://ope.ed.gov/accreditation/GetDownLoadFile.aspx. The column names have been changed, and some unnecessary information was removed. The variables are as follows:

univ_id (unchanged from source):
Database Specific Identification Number for Institution

univ_name:
Full name of the university.

univ_city

univ_state

univ_zip

OPEID:
Identification number used by the U.S. Department of Education's Office of Postsecondary Education (OPE) to identify schools that have Program Participation Agreements (PPA).

IPEDS_unit_id:
A unique identification number for institutions that participate in the Integrated Postsecondary Education Data System Survey.

### student_info

This table contains information about individual students enrolled in graduate programs. The variables are:

student_id:
Arbitrary ID number assigned for uniqueness.

student_firstname

student_lastname

grad_year:
The year the student graduated or left the program.

degree:
The degree obtained upon exiting the graduate program; phd/ms/ma/bs/ba.

dept_id:
ID number that corresponds to the student's department of study.

### dept_info
Information on departments contained within a given university. Ranking information may be available. Variables:

dept_id:
Arbitrary ID number assigned for uniqueness.

dept_name:
Full name of the department

univ_id (FK)

ranking:
Department ranking (integer)

rank_source:
Source of the ranking listed.

### research_groups
Details on individual labs/groups.

group_id:
Arbitrary ID assigned for uniqueness.

PI_firstname:
The principal investigator's first name.

PI_lastname:
The principal investigator's first name.

start_year:
Year the principal investigator began their independent research career.

### institutions
The companies, universities, or other institutions at which students acheive gainful employment.

institution_id:
Arbitrary ID number assigned for uniqueness.

institution_name:
Full name of the institution.

industry:
General industry category into which the institution falls (Academia, Government, Pharma, etc.)

size:
Number of worldwide employees.

year_founded:
Year the institution was founded.

## Relationship Tables

### group_departments
#### Departmental affiliations of principal investigators. Some PIs have appointments in multiple departments.

dept_id (FK)

group_id (FK)

join_date

leave_date

### advisors
#### Advisor-advisee relationships. Some grad students are jointly advised by two PIs.

student_id (FK)

group_id (FK)

### works_at

student_id (FK)

institution_id (FK)

start_date

end_date

inst_city

inst_state

inst_country


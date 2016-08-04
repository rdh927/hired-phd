# hired-phd
HIRED-PhD: Highly Informative Repository of Employment Data for PhDs

This is a way to collect and store placement data for PhD students by institution, discipline, and research group. Use of this information will aid current and prospective grad students in their career planning endeavors.

## Entity Tables
### univ_info
The univ_info table is adapted from the US Accredidation Files available here: http://ope.ed.gov/accreditation/GetDownLoadFile.aspx. The column names have been changed, and some unnecessary information was removed. The variables are as follows:

univ_id (unchanged from source)
Database Specific Identification Number for Institution

univ_name

univ_city

univ_state

univ_zip

OPEID
Identification number used by the U.S. Department of Education's Office of Postsecondary Education (OPE) to identify schools that have Program Participation Agreements (PPA).

IPEDS_unit_id
A unique identification number for institutions that participate in the Integrated Postsecondary Education Data System Survey.

### student_info
This table contains information about individual students enrolled in graduate programs. The variables are:

student_id

student_firstname

student_lastname

grad_year
The year the student graduated or left the program.

degree
phd/ms/ma/bs/ba

dept_id

### dept_info
Information on departments contained within a given university. Ranking information may be available. Variables:

dept_id

dept_name

univ_id (FK)

ranking

rank_source

### research_groups

### institutions

## Relationship Tables
### group_departments
### advisors
### works_at

# Consultant model
The Python object that will be mapped to the SQL database. In this case, each row in the master consultants table will be an instance of the consultant object. Fields in the table are attributes for the model and may be manipulated in Python using standard syntax

Some fields will be populated directly by the consultant (or the OPM staff member who is entering the data), others will be computed automatically in the backend, and others will be populated by the database maintainers/admins

## Consultant populated fields
      - First name
      - Last name
      - Years of experience
      - Area of expertise tags (to be selected from a multiselect dropdown)
      - CV (stored as a file, linked to DB row)

## Computed fields
    - Date of entry into database 
    - CV Screening?
    
## Admin/OPM populated fields
    - References/review of prior work


## <<entry.company>>, <<entry.position>>

((* if entry.date_string *))- <<entry.date_string>>
((* endif *))
((* if entry.location *))- <<entry.location>>
((* endif *))
((* for item in entry.highlights *))
- <<item>>
((* endfor *))

((* if entry.projects *))
### Projects:

((* for project in entry.projects *))
#### **Customer**: *<<project.customer>>*

- **Project**: *<<project.title>>*

  - **Technologies**: _<<project.technologies|join(" - ")>>_

  - **Highlights**:
  ((* for highlight in project.highlights *))
  - <<highlight>>
  ((* endfor *))

((* endfor *))
((* endif *))
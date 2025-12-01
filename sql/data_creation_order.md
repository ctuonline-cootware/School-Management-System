| Order | Table                              | Depends On                                      | Can Create Independently? |
|-------|------------------------------------|-------------------------------------------------|---------------------------|
| 1     | `SCHOOL.JOB`                       | –                                               | Yes                       |
| 2     | `SCHOOL.DEPARTMENT`                | –                                               | Yes                       |
| 3     | `SCHOOL.FACULTY`                   | `JOB`, `DEPARTMENT`                             | No                        |
| 4     | `SCHOOL.COURSE`                    | –                                               | Yes                       |
| 5     | `SCHOOL.ACADEMIC_PROGRAM`          | `DEPARTMENT`                                    | No                        |
| 6     | `SCHOOL.STUDENT`                   | `ACADEMIC_PROGRAM`                              | No                        |
| 7     | `SCHOOL.COURSE_INSTANCE`           | `COURSE`, `FACULTY`                             | No                        |
| 8     | `SCHOOL.ASSIGNMENT`                | –                                               | Yes                       |
| 9     | `SCHOOL.PROGRAM_COURSE_REQUIREMENT`| `ACADEMIC_PROGRAM`, `COURSE`                    | No                        |
| 10    | `SCHOOL.COURSE_ASSIGNMENT`         | `COURSE_INSTANCE`, `ASSIGNMENT`, `STUDENT`      | No                        |
| 11    | `SCHOOL.ROLES`                     | –                                               | Yes                       |
| 12    | `SCHOOL.USERS`                     | –                                               | Yes                       |
| 13    | `SCHOOL.USER_ROLES`                | `USERS`, `ROLES`                                | No                        |
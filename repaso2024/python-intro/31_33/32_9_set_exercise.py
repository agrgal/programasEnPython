# Set up sets
exam = {'Andrew', 'Kirsty', 'Beth', 'Emily', 'Sue'}
project = {'Kirsty', 'Emily', 'Ian', 'Stuart'}

# Estudiantes que hicieron el examen
print("Examen: ",exam)
# Estudiantes que hicieron el proyecto
print("Proyecto: ",project)

# Which students took both the exam and submitted a project?
print("Ambos, examen y proyecto: ", exam & project)
# Which students only took the exam?
print ("Solo hicieron el examen: ", exam - project)
# Which students only submitted the project?
print ("Solo hicieron el proyecto: ", project-exam)
# List all students who took either (or both) of the exam and the project.
print("O bien hicieron el examen o el proyecto o ambos: ", exam | project)
# List all students who took either (but not both) of the exam and the project.
print ("O hicieron el examen o el proyecto, pero no los dos a la vez: ", exam ^ project)
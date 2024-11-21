def final_grade(exam, projects):
    # si exam > 50 o las tareas son x<2 -> 75
    # si exam > 75 o tareas >=5 -> 90
    # si exam > 90 o tareas >=10 -> 100
    
    if exam>90 or projects>10:
        return 100
    
    elif 90>exam>75 and projects>=5:
        return 90
    
    elif exam>50 and projects>=2:
        return 75
    
    else:
        return 0
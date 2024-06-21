course_name = 'Python'
tasks_count = 12
hours_count = 1.5

average_time = hours_count / tasks_count
print(course_name + ',',
      'всего заданий:', tasks_count.__str__() + ',',
      'затрачено часов:', hours_count.__str__() + ',',
      'среднее время выполнения:', average_time.__str__() + ' часа')

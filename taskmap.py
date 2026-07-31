class TaskManager:
  def __init__(self):
    self.map = {}

  def addTask(self, task, tags):
    task = task.lower()
    seta ={}
    if task not in self.map: 
      self.map[task] = set(tags)
    else:
      seta = self.map[task] | set(tags)
      self.map[task] = seta       

  def printTasks(self):
    return self.map
  
myTaskManager = TaskManager()
myTaskManager.addTask("Comprar leche", ["compras", "urgente"])
myTaskManager.addTask("Sacar al perro", ["mascotas"])
myTaskManager.addTask("Hacer ejercicio", ["salud"])

print(myTaskManager.printTasks())
print("\n ------------- \n")

myTaskManager = TaskManager()
myTaskManager.addTask("Comprar leche", ["compras", "urgente"])
myTaskManager.addTask("Sacar al perro", ["mascotas"])
myTaskManager.addTask("Hacer ejercicio", ["salud"])
myTaskManager.addTask("Comprar leche", ["lacteos"])

print(myTaskManager.printTasks())
print("\n ------------- \n")
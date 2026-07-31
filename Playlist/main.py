from node import Node

class Playlist:
  def __init__(self):
    self.top = None
    self.bottom = None 
    self.length = 0
 

  def addSong(self, song):
    node_value = Node(song)
    if self.length == 0: 
      self.top = node_value
      self.bottom = node_value 
    else: 
      node_value.next = self.top 
      self.top = node_value
    self.length += 1  


  def playSong(self):
    current = self.top
    if self.length == 0: 
      raise Exception ("No hay canciones en la lista") 
    elif self.top == self.bottom:
      self.top = None
      self.bottom = None
    else:
      self.top = current.next
    self.length -= 1  
    return current.value
    

      
  def getPlaylist(self):
    canciones = []
    if self.bottom == None:
      raise Exception ("No hay canciones en la lista.")
    else:
      current = self.top
      while current is not None:
        canciones.append(current.value)
        current = current.next  
      return  canciones 
  



playlist = Playlist()

playlist.addSong("Bohemian Rhapsody")
playlist.addSong("Stairway to Heaven")
playlist.addSong("Hotel California")


print(playlist.playSong())
print(playlist.playSong())
print(playlist.playSong())


print(playlist.getPlaylist())   
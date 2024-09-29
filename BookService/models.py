from sqlalchemy import Column, String, Float, Integer,ForeignKey , Date,Text
from database import Base
from sqlalchemy.orm import relationship

################## Models #########################
#Ci-dessous vous trouverez le model (Table SQL) dans la quelle vous representez les données necessaires (les champs , les relations )
#!!!!!! Il faut toujouts placer les models dans l'order pere puis fils (comme en sql) sinon ca va cree des problemes au niveau de migrations
class Author(Base):

    __tablename__ = 'auteurs'

    id = Column(Integer, primary_key=True,index=True) # Coulumn == ligne(champs) , primary_key = true == cle primaire , index = champs indexe
    nom = Column(String(25), nullable=False) #String(25)  == varchar(25)
    prenom = Column(String(25), nullable=False)
    dateNaissance = Column(Date, nullable=False)#Date = date

    books = relationship("Book",back_populates='author') # c'est la relations entre table Author -> Books un champs et rendus pour afficher les donnes des Livres concernants l'auteur chercher ou les auteurs

class Book(Base):

    __tablename__ = 'books'

    isbn = Column(String(25), primary_key=True,index=True)
    titre = Column(String(70))
    description = Column(Text)
    #auteur = Column(String(100)) #Nom et Prenom
    prix = Column(Float) #Float == float
    anneeEdition = Column(String(4))
    author_id = Column(Integer, ForeignKey('auteurs.id')) ##ForeignKey('auteurs.id') = foreignKey author_id references auteurs(id)

    author = relationship("Author",back_populates='books') ##La relation dans laquelle on ajoute les donnes de l'auteurs

    def __repr__(self):
        return f'<Book> isbn: {self.isbn}, titre: {self.titre}, description: { self.description} ,auteur: {self.auteur} , prix: {self.prix} , anneeEdition: {self}'
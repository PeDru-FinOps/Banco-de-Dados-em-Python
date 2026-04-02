from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

# Criar o banco de dados ou conectar existente

db = create_engine("sqlite:///banco.db")

# Criar uma sessão para acessar o banco
Session = sessionmaker(bind=db)

# Inicializa a sessão
session = Session()

# Criar tabelas
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    #Sintaxe - Column(nome_campo, tipo)
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome= Column("nome", String)
    email= Column("email", String)
    senha= Column("senha", String)
    status= Column("status", Boolean)

    def __init__(self, nome, email, senha, status=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.status = status

class Livro(Base):
    __tablename__ = "livros"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo= Column("titulo", String)
    paginas=Column("paginas", Integer)
    dono= Column("dono", ForeignKey("usuarios.id"))

    def __init__(self, titulo, paginas, dono):
        self.titulo = titulo
        self.paginas = paginas
        self.dono = dono

Base.metadata.create_all(bind=db)

# CREATE

usuario = Usuario(nome="Pedro Drumond", email="pedros@gmail.com", senha="comeabacatebem")
session.add(usuario)
session.commit()

# READ

#lista_usuarios = session.query(Usuario).all()
usuario_dono = session.query(Usuario).filter_by(email="pedros@gmail.com").first()

livro = Livro(titulo="Nome da Rosa", paginas=600, dono=usuario_dono.id)
session.add(livro)
session.commit()

# UPDATE

usuario_dono.nome = "Zé das Couves"
session.add(usuario_dono)
session.commit()

# DELETE
session.delete(usuario)
session.commit()
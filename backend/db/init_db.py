def init_db():
    from db.models import Base
    from db.session import engine

    Base.metadata.create_all(engine)
    print("Tabelas criadas com sucesso")

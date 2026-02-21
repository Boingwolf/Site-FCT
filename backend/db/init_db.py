def init_db():
    from backend.db.models import Base
    from backend.db.session import engine

    Base.metadata.create_all(engine)
    print("Tabelas criadas com sucesso")

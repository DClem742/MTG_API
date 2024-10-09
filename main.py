from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from database import get_session
from models import cards, colors, collections, collection_cards

app = FastAPI()

@app.get("/cards")
def get_cards(session: Session = Depends(get_session)):
    query_result = session.exec(select(cards)).all()
    return query_result

@app.get("/cards/{card_id}")
def get_card(card_id: int, session: Session = Depends(get_session)):
    card = session.get(cards, card_id)
    return card if card else {"message": "Card not found"}

@app.get("/collections")
def get_collections(session: Session = Depends(get_session)):
    collections = session.exec(select(collections)).all()
    return collections

@app.get("/collections/{collection_id}")
def get_collection(collection_id: int, session: Session = Depends(get_session)):
    collection = session.get(collections, collection_id)
    return collection if collection else {"message": "Collection not found"}

@app.post("/collections/{collection_id}/cards")
def add_card_to_collection(collection_id: int, card_id: int, quantity: int = 1, foil: bool = False, condition: str = None, session: Session = Depends(get_session)):
    collection = session.get(collections, collection_id)
    card = session.get(cards, card_id)
    if not collection or not cards:
        return {"message": "Collection or Card not found"}
    
    link = collection_cards(collection_id=collection_id, card_id=card_id, quantity=quantity, foil=foil, condition=condition)
    session.add(link)
    session.commit()
    return {"message": "Card added to collection successfully"}

@app.get("/colors")
def get_colors(session: Session = Depends(get_session)):
    colors = session.exec(select(colors)).all()
    return colors

from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

class CardColorLink(SQLModel, table=True):
    card_id: Optional[int] = Field(default=None, foreign_key="card.id", primary_key=True)
    color_id: Optional[int] = Field(default=None, foreign_key="color.id", primary_key=True)

class CollectionCardLink(SQLModel, table=True):
    collection_id: Optional[int] = Field(default=None, foreign_key="collection.id", primary_key=True)
    card_id: Optional[int] = Field(default=None, foreign_key="card.id", primary_key=True)
    quantity: int = Field(default=1)
    foil: bool = Field(default=False)
    condition: Optional[str] = None

class Card(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    mana_cost: Optional[str] = None
    cmc: Optional[float] = None
    type_line: Optional[str] = None
    oracle_text: Optional[str] = None
    power: Optional[str] = None
    toughness: Optional[str] = None
    rarity: Optional[str] = None
    set_code: Optional[str] = None
    collector_number: Optional[str] = None
    image_url: Optional[str] = None

    colors: List["Color"] = Relationship(back_populates="cards", link_model=CardColorLink)
    collections: List["Collection"] = Relationship(back_populates="cards", link_model=CollectionCardLink)

class Color(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    color: str

    cards: List[Card] = Relationship(back_populates="colors", link_model=CardColorLink)

class Collection(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = None
    name: str

    cards: List[Card] = Relationship(back_populates="collections", link_model=CollectionCardLink)

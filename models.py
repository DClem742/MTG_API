from typing import Optional
from sqlmodel import Field, SQLModel, Relationship

class cards(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    mana_cost: Optional[str] = None
    cmc: Optional[float] = None
    type_line: str
    oracle_text: Optional[str] = None
    power: Optional[str] = None
    toughness: Optional[str] = None
    rarity: str
    set_code: str
    collector_number: str

class colors(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    color: str

class card_colors(SQLModel, table=True):
    card_id: Optional[int] = Field(default=None, foreign_key="cards.id", primary_key=True)
    color_id: Optional[int] = Field(default=None, foreign_key="colors.id", primary_key=True)

class collections(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    name: str

class collection_cards(SQLModel, table=True):
    collection_id: Optional[int] = Field(default=None, foreign_key="collections.id", primary_key=True)
    card_id: Optional[int] = Field(default=None, foreign_key="cards.id", primary_key=True)
    quantity: int = Field(default=1)
    foil: bool = Field(default=False)
    condition: Optional[str] = None

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password_hash: str

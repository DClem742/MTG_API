from sqlmodel import Field, SQLModel

class cards(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    mana_cost: str = None
    cmc: float = None
    type_line: str
    oracle_text: str = None
    power: str = None
    toughness: str = None
    rarity: str
    set_code: str
    collector_number: str
    colors: str = None


class collections(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int
    name: str
    

class collection_cards(SQLModel, table=True):
    collection_id: int = Field(default=None, foreign_key="collections.id", primary_key=True)
    card_id: int = Field(default=None, foreign_key="cards.id", primary_key=True)
    quantity: int = Field(default=1)
    foil: bool = Field(default=False)
    condition: str = None
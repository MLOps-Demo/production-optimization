from pydantic import BaseModel, Field

feature_names = [
    'iron_feed', 
    'starch_flow',
    'amina_flow',
    'ore_pulp_flow',
    'ore_pulp_ph',
    'ore_pulp_density',
    'flotation_column_01_air_flow',
    'flotation_column_02_air_flow',
    'flotation_column_04_air_flow',
    'flotation_column_05_air_flow',
    'flotation_column_06_air_flow',
    'flotation_column_07_air_flow',
    'flotation_column_01_level',
    'flotation_column_02_level',
    'flotation_column_03_level',
    'flotation_column_04_level',
    'flotation_column_05_level',
    'flotation_column_06_level',
    'flotation_column_07_level',
    'iron_concentrate'
]


class Production(BaseModel):
    iron_feed: float
    starch_flow: float
    amina_flow: float
    ore_pulp_flow: float
    ore_pulp_ph: float
    ore_pulp_density: float
    flotation_column_01_air_flow: float
    flotation_column_02_air_flow: float
    flotation_column_04_air_flow: float
    flotation_column_05_air_flow: float
    flotation_column_06_air_flow: float
    flotation_column_07_air_flow: float
    flotation_column_01_level: float
    flotation_column_02_level: float
    flotation_column_03_level: float
    flotation_column_04_level: float
    flotation_column_05_level: float
    flotation_column_06_level: float
    flotation_column_07_level: float
    iron_concentrate: float


class Rating(BaseModel):
    quality: float = Field(..., ge=0, le=6, description="wine quality grade ranging from 0 (very bad) to 6 (excellent)")

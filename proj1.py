#complete your tasks in this file
#task1 creating classes
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class GlobeRect:
    lo_lat: float
    hi_lat: float
    west_long: float
    east_long: float

@dataclass(frozen=True)
class Region:
    rect: GlobeRect
    name: str
    terrain: str

@dataclass(frozen=True)
class RegionCondition:
    region: Region
    year: int
    pop: int
    ghg_rate: float

#task2 creating example data
region_conditions = [RegionCondition(Region(GlobeRect(34.0, 35.0, -118.0, -117.0), 'Los Angeles', 'other'), 2026, 3869890, 430), RegionCondition(Region(GlobeRect(33,34,151, 152), 'Sydney', 'other'), 2026, 5312640, 400), RegionCondition(Region(GlobeRect(0, 1, 160, 161), 'Pacific Ocean', 'ocean'), 2026, 0, 0), RegionCondition(Region(GlobeRect(35, 38, 120, 39), 'Paso Robles', 'mountains'), 2026, 30, 32)]

#task3
#precondtions:
#postconditions:
#calculates the tons of Co2 that is emitted per person in a region
def emissions_per_capita(rc: RegionCondition)-> float:
    if rc.pop == 0:
        return 0.0
    if rc.pop > 0:
        return rc.ghg_rate / rc.pop
    return emissions_per_capita(rc)
#check this one

#preconditions:
#postconditions:
#calculates the estimated surface area of the region in square kilometers
def area(gr: GlobeRect) -> float:
    pass
    #if bleh:
        #return a * b * c
    #return area(gr)

#preconditions:
#postconditions:
#calculates the tons of Co2-equivalent per square kilometer using the area function
def emissions_per_square_km(rc: RegionCondition) -> float:
    pass

#preconditions:
#postconditions:
#returns region with the highest population density
def densest(rc_list: list[RegionCondition]) -> Region|None:
    if len(rc_list) == 0:
        return None
    if rc_list[0].pop / area(rc_list[0].region) > 0:
        return rc_list[0].region
#check this


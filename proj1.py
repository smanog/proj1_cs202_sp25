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
region_conditions = [RegionCondition(Region(GlobeRect(34.0, 35.0, -118.0, -117.0), 'Los Angeles', 'other'), 2026, 3869890, 430), RegionCondition(Region(GlobeRect(33,34,151, 152), 'Sydney', 'other'), 2026, 5312640, 520), RegionCondition(Region(GlobeRect(0, 1, 160, 161), 'Pacific Ocean', 'ocean'), 2026, 13, 0), RegionCondition(Region(GlobeRect(35, 38, 120, 39), 'Paso Robles', 'other'), 2026, 30, 100)]

#task3
#inputs a RegionCondition
#outputs a float
#calculates the tons of Co2 that is emitted per person in a region
def emissions_per_capita(rc: RegionCondition)-> float:
    if rc.pop == 0:
        return 0.0
    if rc.pop > 0:
        return rc.ghg_rate / rc.pop
    return emissions_per_capita(rc)


#inputs a GlobeRect
#outputs a float
#calculates the estimated surface area of the region in square kilometers
def area(gr: GlobeRect) -> float:
    r = 6378.1 ** 2
    we_long = abs((gr.east_long * (math.pi / 180)) - (gr.west_long * (math.pi / 180)))
    if we_long < 0:
        we_long += 2 * math.pi
    lh_lat = abs((math.sin((gr.hi_lat * (math.pi / 180))) - (math.sin((gr.lo_lat * (math.pi / 180))))))
    if lh_lat < 0:
        lh_lat += 2 * math.pi
    return r * we_long * lh_lat


#inputs a RegionCondition
#outputs a float
#calculates the tons of Co2-equivalent per square kilometer using the area function
def emissions_per_square_km(rc: RegionCondition) -> float:
    a = area(rc.region.rect)
    return rc.ghg_rate / a


#inputs a list of RegionConditions and an idx
#returns region with the highest population density
def densest(rc_list: list[RegionCondition], idx = 1) -> str:
    if len(rc_list) == 1:
        return rc_list[0].region.name
    if idx == len(rc_list) - 1:
        return rc_list[idx].region.name
    dense = rc_list[0].pop / area(rc_list[0].region.rect)
    if rc_list[idx].pop / area(rc_list[idx].region.rect) > dense:
        dense = rc_list[idx]
        return dense.region.name
    return densest(rc_list, idx + 1)


#task4
#helper function for project_condition
#inputs a RegionCondition and years
#outputs an int
#applies annual growth rate depending on terrain
def growth_rate(rc: RegionCondition, years: int) -> int:
    if rc.region.terrain == 'ocean':
        return int(rc.pop * (years * 0.0001))
    if rc.region.terrain == 'mountains':
        return int(rc.pop * (years * 0.0005))
    if rc.region.terrain == 'forest':
        return int(rc.pop * (years * (-0.00001)))
    if rc.region.terrain == 'other':
        return int(rc.pop * (years * 0.0003))
    return growth_rate(rc, years)

#helper function for project_condition
#inputs a RegionCondition and years
#outputs a float
#scales emissions proportionately with the population
def scale_ghg(rc: RegionCondition, years: int) -> float:
     ghg = rc.ghg_rate + (emissions_per_capita(rc) * growth_rate(rc, years))
     return ghg

#inputs a RegionCondition and years
#outputs a new RegionCondition
#Creates a new RegionCondition using projected data after a certain amount of years
def project_condition(rc: RegionCondition, years: int) -> RegionCondition:
    new_pop = growth_rate(rc, years)
    new_ghg = scale_ghg(rc, years)
    new_rc = RegionCondition(Region(GlobeRect(rc.region.rect.hi_lat, rc.region.rect.lo_lat, rc.region.rect.west_long, rc.region.rect.east_long), rc.region.name, rc.region.terrain), rc.year + years, new_pop, new_ghg)
    return new_rc

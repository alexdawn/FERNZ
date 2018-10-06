from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='tyre_plant',
                             processed_cargos_and_output_ratios=[('RUBR', 6), ('SULP', 2)],
                             combined_cargos_boost_prod=True,
                             prod_cargo_types=['VPTS'],
                             prob_in_game='3',
                             prob_random='5',
                             prod_multiplier='[0, 0]',
                             map_colour='143',
                             name='string(STR_IND_TYRE_PLANT)',
                             nearby_station_name='string(STR_STATION_RUBBER_COMPANY)',
                             fund_cost_multiplier='130',
                             intro_year=1832)

industry.economy_variations['STEELTOWN'].enabled = True

industry.add_tile(id='tyre_plant_tile_1',
                  animation_length=71,
                  animation_looping=True,
                  animation_speed=2,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))


spriteset_ground = industry.add_spriteset(
    type='concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 90, -31, -58)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 90, -31, -58)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 90, -31, -58)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 90, -31, -58)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -32)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -32)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 31, -31, 0)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 31, -31, 0)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type='white_smoke_small',
    xoffset=-3,
    yoffset=0,
    zoffset=54,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type='white_smoke_small',
    xoffset=-3,
    yoffset=-3,
    zoffset=54,
)

industry.add_spritelayout(
    id='tyre_plant_spritelayout_silos',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='tyre_plant_spritelayout_building_large_door',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='tyre_plant_spritelayout_building_roof_chimneys',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='tyre_plant_spritelayout_boilerhouse',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='tyre_plant_spritelayout_horizontal_tanks',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='tyre_plant_spritelayout_gatehouse',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='tyre_plant_spritelayout_tyres_1',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='tyre_plant_spritelayout_tyres_2',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=['nw', 'ne', 'se', 'sw']
)

industry.add_industry_layout(
    id='tyre_plant_industry_layout_1',
    layout=[(0, 0, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_building_roof_chimneys'),
            (0, 1, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_building_roof_chimneys'),
            (0, 2, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_boilerhouse'),
            (0, 3, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_1'),
            (1, 0, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_building_large_door'),
            (1, 1, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_building_large_door'),
            (1, 2, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_horizontal_tanks'),
            (1, 3, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_gatehouse'),
            (2, 0, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_building_roof_chimneys'),
            (2, 1, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_silos'),
            (2, 2, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_1'),
            (2, 3, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_2'),
            ]
)
industry.add_industry_layout(
    id='tyre_plant_industry_layout_2',
    layout=[(0, 0, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_building_large_door'),
            (0, 1, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_building_large_door'),
            (0, 2, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_boilerhouse'),
            (1, 0, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_building_roof_chimneys'),
            (1, 1, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_building_roof_chimneys'),
            (1, 2, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_horizontal_tanks'),
            (2, 0, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_building_large_door'),
            (2, 1, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_1'),
            (2, 2, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_1'),
            (3, 0, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_silos'),
            (3, 1, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_1'),
            (3, 2, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_2'),
            (4, 0, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_1'),
            (4, 1, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_2'),
            (4, 2, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_gatehouse'),
            ]
)
industry.add_industry_layout(
    id='tyre_plant_industry_layout_3',
    layout=[(0, 0, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_building_large_door'),
            (0, 1, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_building_large_door'),
            (0, 2, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_building_large_door'),
            (0, 3, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_boilerhouse'),
            (0, 4, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_1'),
            (1, 0, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_silos'),
            (1, 1, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_building_roof_chimneys'),
            (1, 2, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_building_roof_chimneys'),
            (1, 3, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_horizontal_tanks'),
            (1, 4, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_1'),
            (2, 0, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_1'),
            (2, 1, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_2'),
            (2, 2, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_gatehouse'),
            (2, 3, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_2'),
            ]
)
